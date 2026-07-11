import os

class Settings:
    VERIFY_TOKEN: str = os.getenv("VERIFY_TOKEN", "sociounido_token_secreto_123")
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
