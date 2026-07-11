from app.utils.config import settings

class WebhookService:
    def __init__(self):
        self.secret_token = settings.VERIFY_TOKEN

    def verify_meta_token(self, mode: str, token: str) -> bool:
        """Valida que el webhook provenga legítimamente de Meta."""
        return mode == "subscribe" and token == self.secret_token

    async def handle_incoming_message(self, payload: dict) -> bool:
        """
        Procesa el JSON enviado por WhatsApp.
        En el futuro, este componente invocará al IntentRecognizer y ActionOrchestrator.
        """
        print("--- NUEVO MENSAJE DESDE WHATSAPP ---")
        print(payload)
        print("------------------------------------")
        return True
