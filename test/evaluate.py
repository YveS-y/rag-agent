"""
P3 评估脚本骨架：批量调用 query_server /query 接口，对比关键词覆盖率。

用法：
    python test/evaluate.py --qa-file docs_test/eval_qa_pairs.json --base-url http://127.0.0.1:8001

前置条件：
    1. docs_test/eval_qa_pairs.json 中的 TODO 已替换为真实问题和真实关键词（依赖文档已导入完成）
    2. query_server 已启动（scripts/start.sh）
"""
import argparse
import json
import sys
from pathlib import Path

import requests

from app.core.logger import logger


def load_qa_pairs(qa_file: str) -> list[dict]:
    with open(qa_file, "r", encoding="utf-8") as f:
        return json.load(f)


def is_todo(qa: dict) -> bool:
    return "TODO" in qa["question"] or any("TODO" in kw for kw in qa["reference_keywords"])


def ask(base_url: str, question: str) -> str:
    resp = requests.post(
        f"{base_url}/query",
        json={"query": question, "is_stream": False},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json().get("answer", "") or ""


def score_one(qa: dict, answer: str) -> dict:
    keywords = qa["reference_keywords"]
    hit = [kw for kw in keywords if kw in answer]
    coverage = len(hit) / len(keywords) if keywords else 0.0
    return {
        "id": qa["id"],
        "category": qa["category"],
        "question": qa["question"],
        "answer": answer,
        "hit_keywords": hit,
        "missed_keywords": [kw for kw in keywords if kw not in hit],
        "coverage": coverage,
    }


def run(qa_file: str, base_url: str, output: str):
    qa_pairs = load_qa_pairs(qa_file)

    skipped = [qa for qa in qa_pairs if is_todo(qa)]
    runnable = [qa for qa in qa_pairs if qa not in skipped]

    if skipped:
        logger.warning(
            f"跳过 {len(skipped)} 条仍含 TODO 的问答对（先在 {qa_file} 中补齐真实问题/关键词）："
            f"{[qa['id'] for qa in skipped]}"
        )

    results = []
    for qa in runnable:
        try:
            answer = ask(base_url, qa["question"])
        except Exception as e:
            logger.exception(f"调用 {qa['id']} 失败：{e}")
            results.append({**score_one(qa, ""), "error": str(e)})
            continue
        results.append(score_one(qa, answer))

    by_category = {}
    for r in results:
        by_category.setdefault(r["category"], []).append(r["coverage"])

    print("\n===== 评估结果 =====")
    for r in results:
        print(f"[{r['id']}] coverage={r['coverage']:.0%}  missed={r['missed_keywords']}")

    print("\n===== 分类统计 =====")
    for category, coverages in by_category.items():
        avg = sum(coverages) / len(coverages) if coverages else 0.0
        print(f"{category}: 平均关键词覆盖率 = {avg:.0%}  (n={len(coverages)})")

    Path(output).write_text(
        json.dumps({"results": results, "skipped_ids": [qa["id"] for qa in skipped]}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    logger.info(f"详细结果已写入 {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--qa-file", default="docs_test/eval_qa_pairs.json")
    parser.add_argument("--base-url", default="http://127.0.0.1:8001")
    parser.add_argument("--output", default="test/eval_results.json")
    args = parser.parse_args()
    run(args.qa_file, args.base_url, args.output)
