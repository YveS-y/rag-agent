#!/usr/bin/env bash
# 停止本机开发环境：两个 FastAPI 服务 + Docker 容器（数据保留）
cd "$(dirname "$0")/.."

echo "==> 停止导入服务（端口 8000）"
lsof -ti:8000 | xargs -r kill

echo "==> 停止查询服务（端口 8001）"
lsof -ti:8001 | xargs -r kill

echo "==> 停止 Docker 容器（数据保留，不会丢）"
docker compose stop

echo "==> 完成。"
