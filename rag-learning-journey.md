# rag-agent · Spec-Driven 精读 + 面试准备卡

> **单文件自包含**：任何 AI 读到本文件都能无缝接手陪学；学员自己更新进度。
> **当前阶段**：全图精读（**Spec-Driven Learning 闯关式**）
> **🎯 终极目标**：通关后能 ① 用 Spec 集口述自己项目的完整设计，② 回答 RAG 技术面试不卡壳，③ 用 Spec 驱动 AI 扩展或重构本项目。
> **源码位置**：`/Users/ys/code/git/rag-agent/`（导入图 7 节点 + 查询图 7 节点）
> **配套文档**：
> - 错题本：[./rag-mistake-book.md](./rag-mistake-book.md)
> - 进度日志：[./_learn/进度日志.md](./_learn/进度日志.md)
> - 已通关参考：[./kb-learning-journey.md](./kb-learning-journey.md)（knowledge_base 精读，L4.5 已通关）

---

## 🤖 AI 接手协议（切换会话后必读）

**如果你是新会话中的 AI，接到类似「继续学习 rag-agent」的指令，请按下面 7 步执行，不要跳步**：

1. **先读本文件完整一遍**，重点看 §1 Spec-Driven 方法、§4 进度快照、§5 10 关、§8 Spec 归档集
2. **锁定当前关卡**：从 §4 拿到 `IN_PROGRESS` 关卡编号
3. **读该关卡的 Preview + Question**，并读 §4 里记录的「上次学员答案」和「遗留追问」
4. **按 §2 的 5 步循环**决定当前该抛哪个问题（优先出 Spec 型题，少出记忆型题）：
   - 学员还没开始回答 → 复述该关卡的 Question
   - 学员答了一半 → 按 §3 Feedback 规范点评 + 用「判断力 5 法」追问深层问题
   - 学员表示「过了」→ 先要求学员补齐节点 Spec（50-80 字），合格后更新 §4 + §8
5. **每次回复结束**，提醒学员在 §4 手动更新：`当前关卡`、`上次提问`、`时间戳`
6. **出现 ❌ / ⚠️ 错题 → 立即登记**到 [rag-mistake-book.md](./rag-mistake-book.md) §1
7. **严守 §3 禁止事项**：不要代读代码、不要直接给答案、不要只问记忆型问题

> ⚠️ **本项目特殊点**：这是学员自己写的项目，不是外部参考代码。所以问题重心在「解释你的设计决策」而非「读懂别人的实现」。优先问「你为什么这样设计」「和 knowledge_base 相比你做了什么选择」「面试时你会怎么解释」，而不是「代码里写了什么」。

---

## 🧠 §1 学习方法：Spec-Driven Learning（规格驱动学习）

### 🌟 核心三角

```
  Spec（产物）         ← 节点功能 / 约束 / 取舍的结构化描述
     ↓
  判断力（能力）       ← 能看出设计在特定场景有没有坑
     ↓
  面试表达（结果）     ← 用 Spec 驱动 60 秒口述，让面试官听懂
```

**本项目的学习目标不是「记住自己写了什么代码」，而是「能描述设计决策 + 能解释为什么」**。

### 🔄 每关的 5 步循环

```
📍 Preview    AI 给定位（源码文件 + 2-3 句背景）
       ↓
❓ Question   AI 抛 Spec 型问题：为什么 / 和 kb 比 / 面试怎么说 / 场景代入
       ↓
🗣 Explain    学员用自己的话答 + 写一段节点 Spec（50-80 字）
       ↓
🔧 Feedback   AI 按「描述力」「判断力」两维度点评 + 追问 1 个反例/面试追问
       ↓
📐 Spec 落库   学员写的 Spec 归档（通关后全部 Spec 拼成面试答案集）
       ↓
   重复直到满足通关标准 → 进下一关
```

### 📚 两类知识维度

| 维度 | 含义 | 漏洞标签 |
|---|---|---|
| **描述力** | 能清晰描述需求/约束让 AI 准确生成；面试能说清楚 | `📝描述力漏洞` |
| **判断力** | 能识别方案在特定场景的坑；能比较方案 A vs B | `🔍判断力漏洞` / `📐参数直觉漏洞` / `⚖️取舍盲区` |

### 🏋 判断力训练 5 法（AI 追问时按此出题）

| 方法 | 典型问法 |
|---|---|
| ① **反例法** | 「如果不做 X / 参数改成 Y 会怎样？」 |
| ② **对比法** | 「你选了方案 A，为什么不选 B？各适合什么场景？」 |
| ③ **预言法** | 「读代码前先预测：你预期它会怎么实现这里？对照后哪里不同？」 |
| ④ **场景代入法** | 「这个设计代入信贷合规文档场景，哪里会翻车？」 |
| ⑤ **面试口述法** | 「面试官问你这个节点，你用 30-60 秒怎么说？」 |

### 📏 硬约束（AI 必须遵守）

- 每次只围绕 **1 个概念** 展开，多概念强制拆轮
- 学员说「明白了」→ 回复「用你自己的话说说看」，先复述再通关
- AI 连续输出超 **3 段** 前，必须先停下抛 1 个检查问题
- **Question 种子优先出 Spec 型题**，少出「代码第几行写了什么」的记忆型题

### 🎯 通关标准（必须同时满足前 3 条）

1. ✅ 回答命中核心因果链（能解释「做什么 / 为什么这样做 / 边界在哪」）
2. ✅ **写出该关节点的 Spec（50-80 字，包含「做什么 / 不做什么 / 关键取舍」）**
3. ✅ **⚡ 实战小任务完成**（能说出任务里要求的具体数字/位置/结果）
4. ✅（可选）能对 AI 的反例追问给出合理回应（判断力层）

---

## 🔄 §2 每关 5 步循环（SOP）

**Preview（定位） → Question（Spec 型题） → Explain（答题 + 写 Spec） → Feedback（双维度点评 + 反例/面试追问） → Spec 落库（归档到 §8）**

---

## 🤝 §3 AI 互动规范

### ✅ AI 该做的

- 优先问「你为什么这样设计」「和 knowledge_base 相比你做了什么选择」「面试怎么说」
- 学员答对 → 用关键词确认，然后用「面试口述法」或「反例法」追问 1 个判断力题
- 学员答错 → 不直接给答案，用反例/对比/「去源码看第 X 行」提示学员自己发现
- **学员说「明白了」** → 回复「用你自己的话说说看」，听完复述再决定是否过关
- **每关通关前必做**：让学员写 **50-80 字的节点 Spec**（做什么/不做什么/关键取舍）
- **错题自动登记**：每轮 Feedback 后，如出现 ❌不会 / ⚠️答错，直接写入 [rag-mistake-book.md](./rag-mistake-book.md) §1

### ❌ 禁止事项

- ❌ 不要把标准答案直接贴出来
- ❌ 不要跨关卡预热下一关内容
- ❌ 不要改动学员维护的 §4 进度记录
- ❌ 不要因为学员某处漏讲就自行补全——用追问让学员自己补

### 💬 Feedback 回复模板

```
【打分】✅核心对 / ⚠️部分对 / ❌偏差大
【点评】对的：xxx | 漏的：xxx | 偏的：xxx
【追问】（只问 1 个）xxx？
【建议】继续补答 / 进入下一关 / 面试口述训练
```

---

## 📍 §4 当前进度快照（⚠️ 学员每次收工自己更新）

```yaml
当前关卡: L0
关卡名称: 架构俯瞰
状态: IN_PROGRESS
上次提问时间: 2026-05-27
上次 AI 提的问题: （未开始）
上次学员回答摘要: （未开始）
遗留追问: （无）
下一步: 开始 L0，说「开始学习」即可
```

---

## 📋 §5 10 关详情

> ⭐ = 重点关卡（面试高频）｜ ⏱ 预估耗时

### ✅ 通关记录（学员自更新）

- [ ] **L0** 架构俯瞰 ⏱10min
- [ ] **L1** ⭐ 导入图：节点链 + 条件路由 ⏱20min
- [ ] **L2** PDF处理链：node_pdf_to_md + node_md_img ⏱15min
- [ ] **L3** ⭐ 2段切片策略 ⏱20min
- [ ] **L4** ⭐ BGE-M3 混合向量化 ⏱20min
- [ ] **L5** 导入收尾：item_name识别 + Milvus入库 ⏱15min
- [ ] **L6** ⭐ 查询图：路由 + item_name_confirm ⏱20min
- [ ] **L7** ⭐ 3路并行召回 ⏱20min
- [ ] **L8** ⭐ RRF融合 + Cross-Encoder精排 ⏱20min
- [ ] **L9** SSE流式回答 + 对话历史 ⏱15min
- [ ] **Final** Spec集 + 面试模拟 ⏱30min

---

### L0 · 架构俯瞰 ⏱10min

**📍 Preview**
rag-agent 有完整的导入图和查询图。读：
- `app/import_process/agent/main_graph.py`（133行）
- `app/query_process/agent/main_graph.py`（46行）

**❓ Question 种子**
1. rag-agent 导入图和查询图各有几个节点？节点名和 knowledge_base 相比有哪些异同？
2. 你的项目里 Milvus / MongoDB / MinIO / Neo4j 分别存什么？和 knowledge_base 的三级存储分工有什么差异？
3. **面试口述**：面试官问「介绍一下你的 RAG 系统的整体架构」，你用 60 秒怎么说？

**⚡ 实战小任务**
只看 `import_process/agent/main_graph.py` 和 `query_process/agent/main_graph.py`，不翻其他文件，在纸上或文本里画出两张图的完整节点流向（含条件路由分支和并行 fan-out）。
→ 预期：导入图 7 节点连接顺序画对，查询图 3 路 fan-out 结构画对。画错的节点就是还没真正读进去的节点。

**🎯 核心点**（仅供 AI 核对，不直接读给学员）
- 导入图：node_entry → [node_pdf_to_md → ] node_md_img → node_document_split → node_item_name_recognition → node_bge_embedding → node_import_milvus
- 查询图：node_item_name_confirm → 3路并行（node_search_embedding / node_search_embedding_hyde / node_web_search_mcp）→ node_rrf → node_rerank → node_answer_output
- 特殊点：rag-agent 比 knowledge_base 多了 Neo4j（知识图谱），查询图结构基本一致

---

### L1 · ⭐ 导入图：节点链 + 条件路由 ⏱20min

**📍 Preview**
导入图的入口节点 `node_entry` 判断文件类型，决定走哪条路径。读：
- `app/import_process/agent/nodes/node_entry.py`（58行）
- `app/import_process/agent/main_graph.py`（133行）

**❓ Question 种子（Spec 型）**
1. `node_entry` 的路由逻辑是什么？PDF 和 Markdown 两路在哪个节点合流？如果是其他格式呢？
2. **为什么**选择在 `node_entry` 做类型判断，而不是在 API 层或 `main_graph.py` 的条件边里直接判断？有什么设计上的好处？
3. LangGraph 的 `add_conditional_edges` 接收的路由函数，返回值和下一个节点名的映射关系是怎么工作的？

**🏋 判断力追问（AI 按需投放）**
- 反例：如果不在 node_entry 做类型判断、让每个节点自己判断文件格式，会出什么问题？
- 对比：`add_conditional_edges` vs `add_edge`，各自适合什么场景？
- 场景代入：如果要新增支持 Word (.docx) 格式，你需要改哪里？

**⚡ 实战小任务**
打开 `node_entry.py`，找到路由判断的那几行，回答：`.txt` 文件会走哪条路径？如果要新增支持 `.docx`，最少改几行、改在哪个文件的哪个位置？
→ 预期：能精确定位判断条件，确认只需改 `node_entry.py` 里的类型判断部分，不需要动 `main_graph.py`。

**🎯 核心点**（仅供 AI 核对）
- 路由：PDF → node_pdf_to_md → node_md_img；MD → 直接 node_md_img；其他 → END（容错不报错）
- node_md_img 是两路合流点
- node_entry 集中处理类型判断是单一职责原则：路由逻辑集中在一处，后续节点不需要再判断格式

---

### L2 · PDF 处理链：node_pdf_to_md + node_md_img ⏱15min

**📍 Preview**
读：
- `app/import_process/agent/nodes/node_pdf_to_md.py`（330行）
- `app/import_process/agent/nodes/node_md_img.py`（384行）

**❓ Question 种子（Spec 型）**
1. MineRU API 的调用方式是什么？是一次请求立即返回，还是提交任务后轮询状态？解析结果最终落到 state 的哪些字段？
2. `node_md_img` 处理图片的核心步骤是什么？LLM 的输入是什么？回填到 Markdown 里的意义是什么（为什么不把图片单独索引）？
3. **面试口述**：「你的系统怎么处理 PDF 里的图片？为什么这样设计？」30 秒版

**🏋 判断力追问（AI 按需投放）**
- 反例：如果跳过 node_md_img 直接切片，图片内容会发生什么？
- 对比：MineRU 和 pdfplumber 解析 PDF 的核心区别是什么？你为什么选 MineRU？
- 场景代入：如果 MineRU API 超时（网络问题），你的节点会怎么处理？

**⚡ 实战小任务**
打开 `node_pdf_to_md.py`，找到轮询逻辑，回答三个具体数字：最多轮询几次？每次间隔多少秒？超过次数上限后，代码抛出什么（raise/return/写 state）？
→ 预期：能说出具体参数值，而不是「有个重试」。参数值背后的等待上限就是你的系统对 MineRU 最长容忍时间。

**🎯 核心点**（仅供 AI 核对）
- MineRU 是异步任务 API：提交 → 轮询 task_id → 下载结果（非一次性返回）
- node_pdf_to_md 落到 state：md_path（本地 md 文件路径）、md_content（全文内容）
- node_md_img：提取 `![]()` 占位符 → 调 VLM 描述图片 → 将描述回填到 md 正文（这样切片时图片语义变成文本，能被 embedding 索引）

---

### L3 · ⭐ 2段切片策略 ⏱20min

**📍 Preview**
切片质量直接决定 RAG 召回质量。读：
- `app/import_process/agent/nodes/node_document_split.py`（341行）

重点看：语义切分函数（按 `#` 标题切）和尺寸精修函数（大块再切 / 小块合并）。

**❓ Question 种子（Spec-Driven 版）**
1. **为什么先按语义（标题）切、再按尺寸调**？如果直接按固定字数切会丢什么？
2. **chunk_size 500-2000 的三股力拉扯**：召回精度 / LLM 生成质量 / token 成本，各自希望 chunk 偏大还是偏小？你的项目参数最终怎么定的？
3. 代码里如何防止代码块（` ``` ` 包裹）内的 `#` 被误判为标题？
4. **📐 Spec 产出**：写一段 node_document_split 的 Spec（50-80 字，含做什么 / 不做什么 / 关键取舍）

**🏋 判断力追问（AI 按需投放）**
- 反例：overlap=0 / chunk_size=200 / 不防护代码块 的 3 个翻车场景
- 场景代入：你的 rag-agent 如果要处理信贷合规文档（政策条文，每条 100-200 字），现在的 chunk_size 下界 500 合不合适？要调吗？

**⚡ 实战小任务**
自己写一段 5-10 行的 Markdown，里面包含：一个二级标题（`## 正常标题`）、一个代码块（块内有一行 `# 这是注释`）。在 Python 里直接调用切分函数，看输出几个 chunk，确认代码块内的 `#` 没有触发切分。
→ 预期：输出 2 个 chunk（标题前后各一个），代码块不被切开。如果代码块内的 `#` 触发了切分，说明防护逻辑没生效，需要 debug。

**🎯 核心点**（仅供 AI 核对）
- 同 knowledge_base L3：step_2 按标题切 / step_3 大块再切（>2000 chars）+ 小块合并（<500 chars 且同 parent_title）
- 召回精度希望 chunk 偏小（语义集中，向量不被稀释）；LLM 生成质量希望 chunk 偏大（信息完整）；这是对立方向，500-2000 是帕累托区间

---

### L4 · ⭐ BGE-M3 混合向量化 ⏱20min

**📍 Preview**
读：
- `app/import_process/agent/nodes/node_bge_embedding.py`（83行）
- `app/lm/embedding_utils.py`（BGE-M3 单例封装）

**❓ Question 种子**
1. BGE-M3 同时输出稠密向量和稀疏向量，代码里如何调用？两种向量分别存入 Milvus 的哪个字段？
2. chunk 写入 Milvus 前，文本格式为什么要拼 `item_name`（如：「万用表：内容...」），而不是直接用 chunk 原文？
3. **batch_size 三股力**：GPU 显存 / 吞吐效率 / 失败重试成本，各自希望 batch 偏大还是偏小？你设了多少？

**🏋 判断力追问（AI 按需投放）**
- 反例：batch_size 设 100 会出什么问题？只用稠密向量（不用稀疏）在关键词精确匹配场景会怎样？
- 对比：稠密向量（余弦相似度）vs 稀疏向量（BM25 关键词权重）各自擅长什么场景？

**⚡ 实战小任务**
打开 `node_bge_embedding.py`，找到 batch_size 的值（记下具体数字）。再打开 `embedding_utils.py`，找到 `encode` 调用，确认 `return_dense` 和 `return_sparse` 两个参数是否都显式传了 `True`。
→ 预期：能说出 batch_size 的具体数值；如果两个参数里有一个没有传或默认是 False，就说明这关还没真正读懂。

**🎯 核心点**（仅供 AI 核对）
- 同 knowledge_base L4：`encode(return_dense=True, return_sparse=True)`，dense_vector / sparse_vector 两字段
- item_name 前置：BGE-M3 对前 128 token 赋予更高权重，前置标识符提升检索准确率

---

### L5 · 导入收尾：item_name 识别 + Milvus 入库 ⏱15min

**📍 Preview**
读：
- `app/import_process/agent/nodes/node_item_name_recognition.py`（358行）
- `app/import_process/agent/nodes/node_import_milvus.py`（212行）

**❓ Question 种子（Spec 型）**
1. `item_name` 为什么要**单独一个节点用 LLM 识别**，而不是在切片时直接从文件名取？一份文档切成 200 个 chunk，它们的 `item_name` 是 200 个不同值还是 1 个广播？
2. Milvus Collection schema 里至少需要哪些字段？稠密向量字段和稀疏向量字段是同一列还是两列？各建什么类型的索引？
3. 批量写 Milvus 失败时（如网络抖动），你的实现怎么处理？全回滚 / 跳过失败 chunk / 整批重试？

**⚡ 实战小任务**
打开 `node_import_milvus.py`，找到创建 collection 的那行，确认是否有幂等保护（如 `if_not_exists=True` 或先检查再创建）。然后回答：如果同一份文档跑两次导入，Milvus 里会有重复的 chunk 吗？代码里有没有去重逻辑？
→ 预期：能说出幂等保护的具体位置；关于重复 chunk，答案取决于代码里有没有 `chunk_id` 去重——这是真实的设计决策，不是有标准答案的题目。

**🎯 核心点**（仅供 AI 核对）
- item_name 是**文档级不变量**，一份文档所有 chunk 共享同一个 item_name（一次 LLM 识别后广播）
- 文件名不等于业务知识条目名（文件名常含版本/日期噪声）
- 两字段两索引：dense_vector → HNSW（ANN）；sparse_vector → SPARSE_INVERTED_INDEX（倒排，只处理非零维）

---

### L6 · ⭐ 查询图：路由 + item_name_confirm ⏱20min

**📍 Preview**
读：
- `app/query_process/agent/main_graph.py`（46行）
- `app/query_process/agent/nodes/node_item_name_confirm.py`（316行）

**❓ Question 种子（Spec 型）**
1. `node_item_name_confirm` 做什么？为什么查询前先确认 item_name，而不是直接全库检索？
2. 用户问题对应 item_name 时有哪几种情况（确认 / 模糊 / 找不到）？每种情况图的走向是什么？
3. 查询图中的 3 路并行，LangGraph 里用什么机制实现「并发执行多个节点」？

**🏋 判断力追问（AI 按需投放）**
- 反例：如果不做 item_name 过滤，直接全库向量检索，信贷合规 + 催收话术混在一个 collection 里会发生什么？
- 对比：`node_item_name_confirm` 里 LLM 用 JSON 输出确认结果 vs 直接用相似度阈值过滤，哪个更可靠？各自缺点是什么？

**⚡ 实战小任务**
在 `node_item_name_confirm.py` 里找到「找不到匹配 item_name」时写入 state 的字段名和值，再在 `query main_graph.py` 里找到根据这个字段做路由的条件边，追踪完整链路：无匹配 → state 写了什么 → 条件边怎么判断 → 走到哪个节点。
→ 预期：能连续说出这条链路上的 3 个具体细节（字段名、字段值、目标节点名）。说不出其中一个就说明链路没追通。

**🎯 核心点**（仅供 AI 核对）
- node_item_name_confirm：LLM 从对话上下文提取 item_name，用于 WHERE 过滤，防跨文档噪声
- LangGraph fan-out：`graph.add_node` 多个并行节点 + 用 `Send` API 或 map-reduce 实现并发

---

### L7 · ⭐ 3路并行召回 ⏱20min

**📍 Preview**
读：
- `app/query_process/agent/nodes/node_search_embedding.py`（93行）—— BGE-M3 混合检索
- `app/query_process/agent/nodes/node_search_embedding_hyde.py`（117行）—— HyDE 增强
- `app/query_process/agent/nodes/node_web_search_mcp.py`（112行）—— MCP 联网搜索

**❓ Question 种子（Spec 型）**
1. `node_search_embedding` 的检索输入是什么？`item_names` 在检索里充当查询向量还是过滤条件？
2. HyDE 的核心思路是什么？`node_search_embedding_hyde` 比直接检索多了什么步骤？什么场景下值得付这个额外 LLM 调用成本？
3. `node_web_search_mcp` 接入的是什么服务？它在 3 路里是主路还是兜底路？

**🏋 判断力追问（AI 按需投放）**
- 反例：ranker_weights=(0.9, 0.1)（稠密 0.9 / 稀疏 0.1），代入催收话术场景合不合适？为什么？
- 对比：3路都跑 vs 只跑 1 路（稠密检索），多路并行的代价和收益各是什么？

**⚡ 实战小任务**
打开 `node_search_embedding.py`，找到 `generate_embeddings`（或 encode）的调用，确认传入的是 `rewritten_query` 还是 `item_names`。再找到 `item_names` 被用在哪里（Milvus expr 过滤表达式）。把这两行代码位置记下来。
→ 预期：能指出「向量化的是 query，item_names 在 expr 里」这个区别在代码里的具体行数。这是很多人说「懂了」但指不出来的地方。

**🎯 核心点**（仅供 AI 核对）
- item_names 是 expr 过滤条件（WHERE），不是查询向量；查询向量是 rewritten_query 的 embedding
- HyDE：先用 LLM 生成假设答案 → 用假设答案向量检索（而非原始问题向量），弥补"问法与答法向量距离远"的问题
- node_web_search_mcp：通过 MCP 协议接入联网搜索，是知识库无结果时的兜底

---

### L8 · ⭐ RRF融合 + Cross-Encoder精排 ⏱20min

**📍 Preview**
读：
- `app/query_process/agent/nodes/node_rrf.py`（123行）
- `app/query_process/agent/nodes/node_rerank.py`（266行）

**❓ Question 种子**
1. **RRF 公式**：`score = Σ 1/(k + rank_i)`，常数 k=60 的作用是什么？如果改成 k=10 会怎样？
2. 3 路召回结果里同一个 chunk_id 出现多次，代码里怎么去重并累加得分？
3. Cross-Encoder Reranker 和 Bi-Encoder（BGE-M3）的核心区别是什么？为什么 Reranker 只能做精排不能做召回？

**🏋 判断力追问（AI 按需投放）**
- 反例：不做 RRF、直接把 3 路结果按原始分数 concat 排序，会出什么问题？（分数量纲不同）
- 场景代入：精排候选集送入 Reranker 前，你的代码取了多少条（top_k）？这个值如果设 500 会怎样？

**⚡ 实战小任务**
打开 `node_rrf.py`，找到 k 常数的具体值，然后手算两个数字：当 k 是代码里的值时，rank=1 的 score 是多少？把 k 改成 10，rank=1 的 score 变成多少？比较这两个数字，感受 k 对头部结果的影响。
→ 预期：能说出两个具体的 score 值（保留两位小数）。算完之后「k 越小头部优势越大」这句话就不再是背的结论，而是你算出来的。

**🎯 核心点**（仅供 AI 核对）
- RRF 按排名而非分数合并，解决不同召回路量纲不一致的问题
- k=60 平滑常数：防止 rank=1 分数过大（头部垄断），k 越小头部优势越大
- Cross-Encoder：问题+文档拼接后一起编码，精确但 O(n)；Bi-Encoder：分别编码用向量距离，快但不能精确建模交互

---

### L9 · SSE 流式回答 + 对话历史 ⏱15min

**📍 Preview**
读：
- `app/query_process/agent/nodes/node_answer_output.py`（351行）
- `app/utils/sse_utils.py`（SSE 工具）
- `app/clients/mongo_history_utils.py`（对话历史）

**❓ Question 种子**
1. LLM 流式输出 token 怎么转成 SSE 事件？FastAPI 里用什么类型的 Response 包装？
2. 对话历史从 MongoDB 取多少轮（limit 是多少）？取出来后以什么格式放入 LLM 的 system/user/assistant 消息？
3. **面试口述**：「你的系统怎么实现流式输出？」30 秒版

**🏋 判断力追问（AI 按需投放）**
- 对比：SSE vs WebSocket，你选 SSE 的理由是什么？什么场景应该用 WebSocket？
- 反例：对话历史不做 limit 限制（无限取历史），会出什么问题？

**⚡ 实战小任务**
打开 `node_answer_output.py`，找到两个具体内容：① MongoDB 取对话历史的 limit 参数是多少；② yield token 那行的完整字符串格式（把那行代码抄下来）。
→ 预期：能说出具体的 limit 数字；能一字不差地说出 SSE 事件格式。这两个细节说不出来，面试时「用了 SSE 流式输出」这句话就是空话。

**🎯 核心点**（仅供 AI 核对）
- `yield f"data: {token}\n\n"` + `StreamingResponse(generator, media_type="text/event-stream")`
- SSE：HTTP 单向推送（服务端 → 客户端），实现简单，适合问答流式输出
- 对话历史：MongoDB 取最近 N 轮，拼成 `[{"role": "user", "content": "..."}, ...]` 格式

---

### Final · Spec集 + 面试模拟 ⏱30min

**场 1 · Spec 集终极考核 ⭐**
- 打开 §8 归档的 10 段节点 Spec，合上项目源码
- 把 10 段 Spec 拼成一份完整 Spec 文档，交给**干净的 AI 会话**（新开窗口）
- 让 AI 根据 Spec 生成整个 rag-agent 项目骨架（至少导入图 + 查询图的函数签名 + 核心逻辑）
- **检查 AI 产出**：函数签名对不对？节点顺序对不对？关键阈值/防护有没有缺？

**场 2 · 面试口述（10 分钟）**
- 问题集（依次口述，每题 ≤60 秒）：
  1. 「介绍你的 RAG 系统整体架构」
  2. 「切片策略怎么设计的？为什么这样分？」
  3. 「BGE-M3 的稠密和稀疏向量各有什么用？」
  4. 「三路召回是怎么融合的？」
  5. 「Cross-Encoder Reranker 和 Embedding 模型有什么区别？」

**场 3 · 扩展设计挑战**
- 「如果要把 rag-agent 改造成支持多租户（每个客户的文档完全隔离），你会怎么设计？」
- 「如果文档更新了（原 PDF 改了一段内容），如何做增量更新，而不是全量重导？」

**通关标准**（必须全中）：
- ✅ AI 根据你的 Spec 产出的代码大方向正确
- ✅ 5 道面试题口述不卡壳
- ✅ 能指出 AI 扩展设计方案的 1-2 处坑

---

## 🔗 §6 关联文档

| 文件 | 作用 |
|---|---|
| `app/import_process/agent/main_graph.py` | 导入图（7节点 + 条件路由）|
| `app/import_process/agent/nodes/` | 导入节点实现 |
| `app/query_process/agent/main_graph.py` | 查询图（7节点 + 并行召回）|
| `app/query_process/agent/nodes/` | 查询节点实现 |
| `app/lm/embedding_utils.py` | BGE-M3 单例 |
| `app/lm/reranker_utils.py` | BGE-Reranker |
| `app/utils/sse_utils.py` | SSE 流式工具 |
| `app/clients/` | 数据库客户端单例 |
| [./kb-learning-journey.md](./kb-learning-journey.md) | knowledge_base 参考学习记录（L4.5 已通关）|

---

## 📝 §7 学员使用提示

1. **每次开新会话**：把本文件 @ 给 AI，说「继续学习 rag-agent」即可
2. **每次收工**：更新 §4 进度快照
3. **每过一关**：勾选 §5 通关记录 + 把节点 Spec 归档到 §8
4. **全部通关后**：执行 Final 三场考核，通过后在 `_learn/进度日志.md` 追加「rag-agent 精读收官」

> 💬 遇到 AI 直接给答案 → 引用 §3 禁止事项提醒。
> 💬 遇到 AI 只问「代码里写了什么」的记忆题 → 提醒用 §1「判断力训练 5 法」里的「面试口述法」升级问法。

---

## 📐 §8 Spec 归档集（学员每关通关后追加一段）

> **格式**：每关一段，50-80 字，三要素：**做什么 / 不做什么 / 关键取舍**
> **用途**：Final 关把全部段落拼起来喂 AI，验证能否重现项目；同时作为面试口述的素材库

### L0 · 架构俯瞰（待学员补写）

### L1 · 导入图路由（待学员补写）

### L2 · PDF处理链（待学员补写）

### L3 · node_document_split（待学员补写）

### L4 · node_bge_embedding（待学员补写）

### L5 · 导入收尾（node_item_name_recognition + node_import_milvus）（待学员补写）

### L6 · 查询图路由 + node_item_name_confirm（待学员补写）

### L7 · 3路并行召回（待学员补写）

### L8 · node_rrf + node_rerank（待学员补写）

### L9 · node_answer_output + SSE（待学员补写）

---

> 🏁 **毕业线**：§8 的 10 段 Spec 全部补齐 + Final 三场考核通过 = rag-agent 精读收官。
