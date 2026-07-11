from fastapi import FastAPI, Request, Response, status
import os

app = FastAPI(title="SocioUnido - Bot Conversacional (MS NLP)")

# Token de verificación que configuraremos en el panel de Meta (puedes inventar uno por ahora)
VERIFY_TOKEN = "sociounido_token_secreto_123"

@app.get("/")
async def root():
    return {"message": "Microservicio de Bot Conversacional Operativo"}

@app.get("/webhook")
async def verify_webhook(request: Request):
    """
    Este endpoint es llamado por Meta (WhatsApp) una sola vez para verificar 
    la autenticidad de nuestra conexión.
    """
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("WEBHOOK VERIFICADO CORRECTAMENTE")
            return Response(content=challenge, status_code=status.HTTP_200_OK)
        else:
            return Response(status_code=status.HTTP_403_FORBIDDEN)
    
    return Response(status_code=status.HTTP_400_BAD_REQUEST)

@app.post("/webhook")
async def receive_message(request: Request):
    """
    Este endpoint recibirá todos los mensajes que los socios envíen al bot.
    """
    body = await request.json()
    
    # Imprimimos el contenido del mensaje en la consola para confirmar que llega
    print("Mensaje recibido desde WhatsApp:")
    print(body)
    
    # Por ahora simplemente respondemos OK para que Meta sepa que recibimos el mensaje.
    # En el futuro, aquí conectaremos el IntentRecognizer (LangChain).
    return Response(status_code=status.HTTP_200_OK)
