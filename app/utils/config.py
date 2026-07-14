import os

class Settings:
    VERIFY_TOKEN: str = os.getenv("VERIFY_TOKEN", "")
    ENV: str = os.getenv("ENV", "development")
    WHATSAPP_TOKEN: str = os.getenv("WHATSAPP_TOKEN", "")
    WHATSAPP_PHONE_ID: str = os.getenv("WHATSAPP_PHONE_ID", "")

settings = Settings()
