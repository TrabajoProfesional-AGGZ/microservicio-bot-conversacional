import httpx
from app.utils.config import settings

class WebhookService:
    def __init__(self):
        self.secret_token = settings.VERIFY_TOKEN

    def verify_meta_token(self, mode: str, token: str) -> bool:
        return mode == "subscribe" and token == self.secret_token

    async def handle_incoming_message(self, payload: dict) -> bool:
        try:
            entry = payload.get("entry", [])[0]
            changes = entry.get("changes", [])[0]
            value = changes.get("value", {})
            if "messages" in value:
                message = value["messages"][0]
                numero_cliente = message["from"]
                texto_recibido = message["text"]["body"]
                print(f"✅ Mensaje de {numero_cliente}: {texto_recibido}")
                respuesta = f"¡Hola! Soy el bot de SocioUnido. Recibí tu mensaje: '{texto_recibido}'. En breve tendré IA."
                await self.send_whatsapp_message(numero_cliente, respuesta)
                
        except Exception as e:
            print(f"Error procesando el mensaje o no es un texto: {e}")
            
        return True

    async def send_whatsapp_message(self, to_number: str, message_text: str):
        """Función que se comunica con la API de Meta para enviar la respuesta"""
        url = f"https://graph.facebook.com/v18.0/{settings.WHATSAPP_PHONE_ID}/messages"
        
        headers = {
            "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "text",
            "text": {"body": message_text}
        }
        
        async with httpx.AsyncClient() as client:
            respuesta_meta = await client.post(url, headers=headers, json=data)
            print(f"Estado del envío: {respuesta_meta.status_code}")
