"""
Entry point de la aplicación FastAPI.

Este es el archivo principal que inicia el servidor web.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# Crear instancia de FastAPI
app = FastAPI(
    title=settings.APP_NAME,           # Nombre en la documentación
    version=settings.VERSION,           # Versión de la API
    description="Sistema de detección de fraude con IA explicable",
    docs_url="/docs",                   # Swagger UI en /docs
    redoc_url="/redoc",                 # ReDoc en /redoc
)

# Configurar CORS (permite peticiones desde el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  # Orígenes permitidos
    allow_credentials=True,                   # Permite cookies
    allow_methods=["*"],                      # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],                      # Permite todos los headers
)

# Ruta raíz (http://localhost:8000/)
@app.get("/")
def root():
    """
    Endpoint de bienvenida.
    
    Returns:
        dict: Información básica de la API
    """
    return {
        "message": "Fraud Detection API",
        "version": settings.VERSION,
        "status": "operational",
        "docs": "/docs"
    }

# Health check (para monitoreo)
@app.get("/health")
def health_check():
    """
    Endpoint para verificar que la API está funcionando.
    
    Útil para:
    - Load balancers
    - Monitoreo automático
    - DevOps
    
    Returns:
        dict: Estado de salud del servicio
    """
    return {
        "status": "healthy",
        "service": settings.APP_NAME
    }

# Este bloque solo se ejecuta si corres este archivo directamente
# No se ejecuta cuando Uvicorn importa la app
if __name__ == "__main__":
    import uvicorn
    
    # Correr servidor
    uvicorn.run(
        "app.main:app",      # Ruta a la app de FastAPI
        host="0.0.0.0",      # Escuchar en todas las interfaces
        port=8000,           # Puerto
        reload=True          # Auto-reload cuando cambies código
    )