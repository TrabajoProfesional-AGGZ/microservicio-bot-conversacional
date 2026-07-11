from fastapi import APIRouter, Request, Response, status
from app.services.webhook import WebhookService

router = APIRouter()
webhook_service = WebhookService()

@router.get("")
async def verify_webhook(request: Request):
    """Punto de verificación requerido por Meta al configurar el bot por primera vez."""
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode and token:
        if webhook_service.verify_meta_token(mode, token):
            return Response(content=challenge, status_code=status.HTTP_200_OK)
        return Response(status_code=status.HTTP_403_FORBIDDEN)
        
    return Response(status_code=status.HTTP_400_BAD_REQUEST)

@router.post("")
async def receive_message(request: Request):
    """Recibe las notificaciones de mensajes en tiempo real."""
    payload = await request.json()
    await webhook_service.handle_incoming_message(payload)
    return Response(status_code=status.HTTP_200_OK)
