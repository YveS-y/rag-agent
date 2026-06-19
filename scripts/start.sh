#!/usr/bin/env bash
# 启动本机开发环境：Docker(Milvus/MinIO/MongoDB) + 两个 FastAPI 服务
set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> 启动 Docker 容器（Milvus / MinIO / MongoDB）"
docker compose up -d

echo "==> 启动导入服务（端口 8000）"
nohup uv run python -m app.import_process.api.import_server > /tmp/import_server.log 2>&1 &
echo "import_server pid: $!"

echo "==> 启动查询服务（端口 8001）"
nohup uv run python -m app.query_process.api.query_server > /tmp/query_server.log 2>&1 &
echo "query_server pid: $!"

echo "==> 完成。访问：导入页 http://127.0.0.1:8000/import ，聊天页 http://127.0.0.1:8001/chat.html"
echo "==> 日志：/tmp/import_server.log 、 /tmp/query_server.log"
