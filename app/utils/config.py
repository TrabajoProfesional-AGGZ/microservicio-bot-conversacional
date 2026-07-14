import os

class Settings:
    VERIFY_TOKEN: str = os.getenv("VERIFY_TOKEN", "sociounido_token_secreto_123")
    ENV: str = os.getenv("ENV", "development")
    WHATSAPP_TOKEN: str = os.getenv("WHATSAPP_TOKEN", "pega_tu_token_aqui")
    WHATSAPP_PHONE_ID: str = os.getenv("WHATSAPP_PHONE_ID", "pega_tu_phone_id_aqui")

settings = Settings()
