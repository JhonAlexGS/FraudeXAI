"""
Configuración central de la aplicación.

Este archivo define todas las configuraciones que puede necesitar
nuestra app (URLs de BD, secrets, etc.)
"""

from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    """
    Clase de configuración usando Pydantic.
    
    Pydantic valida automáticamente los tipos y puede leer
    valores desde variables de entorno.
    """
    
    # Información de la aplicación
    APP_NAME: str = "Fraud Detection System"
    VERSION: str = "1.0.0"
    DEBUG: bool = True  # True en desarrollo, False en producción
    
    # Base de datos
    # sqlite:/// significa base de datos SQLite local
    # ./data/fraud_detection.db es la ruta del archivo
    DATABASE_URL: str = "sqlite:///./data/fraud_detection.db"
    
    # API
    API_V1_PREFIX: str = "/api/v1"  # Todas las rutas empezarán con /api/v1
    
    # CORS (Cross-Origin Resource Sharing)
    # Permite que el frontend (React) hable con el backend
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",  # React dev server
        "http://localhost:5173",  # Vite dev server
    ]
    
    class Config:
        """
        Configuración de Pydantic.
        env_file: leerá valores desde archivo .env si existe
        """
        env_file = ".env"

# Crear instancia única de Settings
# Se usa en toda la app: from app.core.config import settings
settings = Settings()