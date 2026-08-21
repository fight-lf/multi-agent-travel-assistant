# 多智能体旅行助手系统

一个面向旅行场景的多智能体协作项目。系统通过意图识别将用户请求分发给票务查询、天气查询和订单处理 Agent，并同时提供 A2A 与 MCP 两套服务实现，以及 Streamlit 交互界面。

## 核心能力

- 多意图识别与任务路由
- 机票、火车票和演出信息查询
- 天气查询与行程辅助
- 多服务协作和订单处理
- A2A Agent Card 与 MCP 工具服务
- Streamlit 可视化交互

## 项目结构

```text
SmartVoyage/
├── a2a_server/       # A2A 票务、天气和订单 Agent
├── mcp_server/       # MCP 工具服务
├── sql/              # 数据库表结构
├── utils/            # 通用工具
├── app.py            # Streamlit 应用
├── main.py           # 命令行入口与调度逻辑
└── main_prompts.py   # Agent 提示词
```

## 快速开始

```bash
python -m venv .venv
pip install -r requirements.txt
```

复制 `.env.example` 为 `.env`，填写自己的大模型与 MySQL 配置，然后按需启动对应的 A2A/MCP 服务，最后运行：

```bash
streamlit run SmartVoyage/app.py
```

## 数据与安全说明

本仓库仅展示系统核心实现。真实 API 密钥、数据库凭据、运行日志和业务数据均未提交；所有敏感配置均通过环境变量读取。
