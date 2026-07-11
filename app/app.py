from fastapi import FastAPI
from app.controllers import webhook

app = FastAPI(
    title="SocioUnido - Microservicio Bot Conversacional (MS NLP)",
    description="Estructura base del bot conversacional de WhatsApp",
    version="1.0.0"
)

# Inclusión de rutas modulares
app.include_router(webhook.router, prefix="/webhook", tags=["Meta Webhook"])

@app.get("/", tags=["Root"])
async def root():
    return {"service": "microservicio-bot-conversacional", "status": "active"}
