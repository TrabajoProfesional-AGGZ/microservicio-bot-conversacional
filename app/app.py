from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import webhook

app = FastAPI(
    title="SocioUnido - Microservicio Bot Conversacional",
    description="Microservicio encargado de procesar mensajes de WhatsApp y orquestar interacciones.",
    version="1.0.0",
    openapi_url="/api/v1/openapi/bot-conversacional.json"
)

origenes_permitidos = [
    "http://localhost:5173",
    "https://aplicacion-ruddy.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origenes_permitidos,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webhook.router, prefix="/webhook", tags=["Meta Webhook"])

@app.get("/health", tags=["Health"])
def health_check():
    """Endpoint para verificar que el microservicio está funcionando correctamente."""
    return {"status": "ok", "service": "ms-bot-conversacional"}
