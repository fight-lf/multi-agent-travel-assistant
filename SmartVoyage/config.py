import os


project_root = os.path.dirname(os.path.abspath(__file__))


class Config:
    """从环境变量读取运行配置，避免在源码中保存凭据。"""

    def __init__(self):
        self.base_url = os.getenv(
            "LLM_BASE_URL",
            "https://dashscope.aliyuncs.com/compatible-mode/v1",
        )
        self.api_key = os.getenv("LLM_API_KEY", "")
        self.model_name = os.getenv("LLM_MODEL_NAME", "qwen-plus")

        self.host = os.getenv("MYSQL_HOST", "127.0.0.1")
        self.user = os.getenv("MYSQL_USER", "root")
        self.password = os.getenv("MYSQL_PASSWORD", "")
        self.database = os.getenv("MYSQL_DATABASE", "smart_voyage")

        self.log_file = os.getenv(
            "LOG_FILE",
            os.path.join(project_root, "logs", "app.log"),
        )
