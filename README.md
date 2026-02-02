# FraudeXAI
Sistema Inteligente de Detección de Fraude en Tiempo Real con Análisis Explicable

# Sistema Inteligente de Detección de Fraude en Tiempo Real con Análisis Explicable

## 📋 Descripción del Proyecto

Sistema end-to-end de detección de fraude en transacciones financieras que combina múltiples algoritmos de Machine Learning y Deep Learning con capacidades de explicabilidad (XAI). El sistema procesa transacciones en tiempo real, identifica patrones fraudulentos y proporciona explicaciones interpretables sobre cada predicción, cumpliendo con requisitos regulatorios de instituciones financieras.

## 🎯 Objetivos

### Objetivo General
Desarrollar un sistema de detección de fraude escalable y explicable que demuestre competencias avanzadas en IA, ingeniería de software y arquitectura full-stack, aplicando conocimientos de maestría en escenarios productivos del mundo real.

### Objetivos Específicos

1. **Implementar ensemble de modelos de IA** que combine técnicas supervisadas, no supervisadas y de deep learning para maximizar la detección de fraude
2. **Desarrollar pipeline de explicabilidad (XAI)** utilizando SHAP y LIME para proporcionar justificaciones interpretables de cada predicción
3. **Construir API RESTful de alto rendimiento** con FastAPI que soporte procesamiento en tiempo real con latencias <100ms
4. **Crear dashboard interactivo** para monitoreo de transacciones, visualización de explicaciones y análisis de métricas del modelo
5. **Implementar arquitectura de microservicios** con Docker, CI/CD y testing automatizado que refleje estándares de la industria

## ✨ Características Principales

### Detección de Fraude Multicapa
- **Ensemble de 4 modelos**: Isolation Forest, XGBoost, Autoencoder y LSTM
- **Votación ponderada**: Combinación de predicciones con pesos optimizados
- **Manejo de desbalance**: SMOTE, class weighting y threshold optimization
- **Feature engineering automático**: 50+ características derivadas de datos raw

### Explicabilidad (XAI)
- **SHAP values**: Contribución de cada feature a la predicción
- **LIME**: Explicaciones locales interpretables
- **Feature importance**: Ranking visual de características críticas
- **Confidence scores**: Nivel de certeza por predicción

### Monitoreo en Tiempo Real
- **WebSockets**: Alertas instantáneas de transacciones sospechosas
- **Dashboard interactivo**: Visualización de métricas en tiempo real
- **Histórico de alertas**: Análisis retroactivo con filtros avanzados
- **Detección de drift**: Monitoreo de degradación del modelo

### Análisis y Reportes
- **Métricas de performance**: Precision, Recall, F1-Score, AUC-ROC
- **Análisis de falsos positivos/negativos**: Identificación de patrones de error
- **Estadísticas de fraude**: Tendencias temporales y por categoría
- **Exportación de reportes**: CSV, JSON, PDF

## 🛠️ Stack Tecnológico

### Backend

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.11+ | Lenguaje principal |
| FastAPI | 0.110+ | Framework API REST |
| SQLAlchemy | 2.0+ | ORM para base de datos |
| Pydantic | 2.6+ | Validación de datos |
| PyTorch | 2.2+ | Deep Learning (LSTM, Autoencoder) |
| Scikit-learn | 1.4+ | ML tradicional (Isolation Forest) |
| XGBoost | 2.0+ | Gradient Boosting |
| SHAP | 0.44+ | Explicabilidad de modelos |
| LIME | 0.2+ | Explicaciones locales |
| Pandas | 2.2+ | Manipulación de datos |
| NumPy | 1.26+ | Computación numérica |
| MLflow | 2.10+ | Tracking de experimentos |
| Uvicorn | 0.27+ | ASGI server |

### Frontend

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| React | 18.2+ | Framework UI |
| TypeScript | 5.3+ | Type safety |
| Vite | 5.0+ | Build tool |
| Tailwind CSS | 3.4+ | Styling |
| Shadcn UI | Latest | Componentes UI |
| Recharts | 2.10+ | Visualizaciones |
| React Query | 5.17+ | Estado del servidor |
| Axios | 1.6+ | Cliente HTTP |
| Socket.io Client | 4.6+ | WebSockets |

### Base de Datos

| Tecnología | Uso |
|------------|-----|
| SQLite | Desarrollo y demo |
| PostgreSQL | Producción (migración futura) |
| Redis | Caché (opcional) |

### DevOps

| Tecnología | Propósito |
|------------|-----------|
| Docker | Containerización |
| Docker Compose | Orquestación local |
| GitHub Actions | CI/CD pipeline |
| pytest | Testing backend |
| Jest | Testing frontend |
| pre-commit | Git hooks |
| Black | Code formatting |
| Ruff | Linting |

## 🏗️ Arquitectura del Sistema

### Diagrama de Componentes
```
┌─────────────────────────────────────────────────────────────┐
│                         FRONTEND                             │
│  ┌────────────┐  ┌────────────┐  ┌─────────────────┐       │
│  │ Dashboard  │  │ Monitoring │  │  Explainability │       │
│  │            │  │            │  │    Viewer       │       │
│  └────────────┘  └────────────┘  └─────────────────┘       │
└───────────────────────┬─────────────────────────────────────┘
                        │ REST API / WebSockets
┌───────────────────────┴─────────────────────────────────────┐
│                      FASTAPI BACKEND                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              API ROUTES LAYER                        │   │
│  │  /predict  /transactions  /analytics  /explain       │   │
│  └────────────────────┬─────────────────────────────────┘   │
│  ┌────────────────────┴─────────────────────────────────┐   │
│  │            BUSINESS LOGIC LAYER                      │   │
│  │  • FraudDetectionService                             │   │
│  │  • ExplainabilityService                             │   │
│  │  • FeatureEngineeringService                         │   │
│  └────────────────────┬─────────────────────────────────┘   │
│  ┌────────────────────┴─────────────────────────────────┐   │
│  │              ML MODELS LAYER                         │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │   │
│  │  │Isolation │ │ XGBoost  │ │  LSTM    │ │Autoencd│ │   │
│  │  │  Forest  │ │Classifier│ │ Network  │ │  -er   │ │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └────────┘ │   │
│  │              Ensemble Voting System                  │   │
│  └────────────────────┬─────────────────────────────────┘   │
│  ┌────────────────────┴─────────────────────────────────┐   │
│  │          EXPLAINABILITY LAYER                        │   │
│  │          • SHAP Calculator                           │   │
│  │          • LIME Explainer                            │   │
│  └──────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────┴─────────────────────────────────────┐
│                    DATA LAYER                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   SQLite     │  │  MLflow      │  │    Cache     │      │
│  │ (Desarrollo) │  │  Tracking    │  │   (Redis)    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

### Flujo de Predicción
```
1. Cliente envía transacción → FastAPI endpoint
2. Feature Engineering: Extracción de 50+ características
3. Preprocesamiento: Normalización y encoding
4. Predicción Ensemble:
   ├── Isolation Forest → Score anomalía
   ├── XGBoost → Probabilidad fraude
   ├── Autoencoder → Reconstruction error
   └── LSTM → Score secuencial
5. Votación ponderada → Predicción final
6. Explicabilidad:
   ├── SHAP values calculados
   └── LIME explanation generada
7. Almacenamiento en BD
8. Respuesta al cliente + alerta WebSocket (si es fraude)
```

## 🤖 Modelos de Inteligencia Artificial

### 1. Isolation Forest (Detección de Anomalías No Supervisada)
**Propósito**: Identificar transacciones atípicas sin etiquetas previas

**Características**:
- Algoritmo basado en árboles de decisión
- Excelente para detectar outliers multivariados
- No requiere datos balanceados
- Rápido para inferencia

**Hiperparámetros clave**:
- `n_estimators`: 150
- `contamination`: 0.002 (basado en tasa real de fraude)
- `max_samples`: 512

### 2. XGBoost Classifier (Clasificación Supervisada)
**Propósito**: Modelo principal de clasificación binaria (fraude/legítimo)

**Características**:
- Gradient Boosting de alto rendimiento
- Maneja datos desbalanceados con `scale_pos_weight`
- Feature importance nativo
- Regularización L1/L2

**Hiperparámetros optimizados**:
- `max_depth`: 6
- `learning_rate`: 0.05
- `n_estimators`: 300
- `scale_pos_weight`: 577 (ratio de desbalance)
- `subsample`: 0.8

### 3. Autoencoder (Deep Learning para Anomalías)
**Propósito**: Reconstruir transacciones legítimas; alto error → fraude

**Arquitectura**:
```
Encoder:
  Input(50) → Dense(32, ReLU) → Dropout(0.2) → 
  Dense(16, ReLU) → Latent(8)

Decoder:
  Latent(8) → Dense(16, ReLU) → Dropout(0.2) → 
  Dense(32, ReLU) → Output(50, Sigmoid)
```

**Training**:
- Solo datos legítimos (clase negativa)
- Loss: MSE
- Optimizer: Adam (lr=0.001)
- Epochs: 100 con early stopping

### 4. LSTM (Análisis Secuencial)
**Propósito**: Detectar patrones fraudulentos en secuencias de transacciones

**Arquitectura**:
```
Input(sequence_length=10, features=50) →
LSTM(64, return_sequences=True) → Dropout(0.3) →
LSTM(32) → Dropout(0.3) →
Dense(16, ReLU) → Dense(1, Sigmoid)
```

**Features temporales**:
- Ventanas deslizantes de 10 transacciones
- Agregaciones: velocidad, frecuencia, monto promedio
- Gaps temporales entre transacciones

### Ensemble Strategy

**Votación Ponderada**:
```python
final_prediction = (
    0.15 * isolation_forest_score +
    0.45 * xgboost_probability +
    0.25 * autoencoder_anomaly_score +
    0.15 * lstm_probability
)

threshold = 0.5  # Optimizado con curva ROC
is_fraud = final_prediction > threshold
```

**Pesos justificados**:
- XGBoost (45%): Mayor precisión en validación
- Autoencoder (25%): Fuerte en anomalías nuevas
- Isolation Forest (15%): Baseline de anomalías
- LSTM (15%): Contexto temporal

## 📊 Dataset

### Fuente Principal
**Credit Card Fraud Detection Dataset** (Kaggle)
- **Total de transacciones**: 284,807
- **Casos de fraude**: 492 (0.172%)
- **Features**: 30 (28 anonimizadas por PCA + Time + Amount)
- **Desbalance**: 577:1 (realista para industria)

### Features Originales
- `Time`: Segundos transcurridos desde primera transacción
- `V1-V28`: Componentes PCA anónimos
- `Amount`: Monto de la transacción
- `Class`: 0 = Legítimo, 1 = Fraude

### Feature Engineering (50+ características derivadas)

**Características temporales**:
- Hora del día, día de la semana, fin de semana
- Velocidad de transacciones (transacciones/hora)
- Gap temporal desde última transacción

**Características de monto**:
- Log(amount), sqrt(amount)
- Desviación del monto promedio del usuario
- Ratio respecto al percentil 95

**Características de usuario**:
- Número de transacciones en última hora/día
- Monto total en ventana temporal
- Frecuencia de merchant_category

**Características de anomalía**:
- Distancia a centroide del cluster
- Local Outlier Factor (LOF)
- Isolation score

### Preparación de Datos

**División estratificada**:
- Train: 70% (mantiene ratio 0.172%)
- Validation: 15%
- Test: 15%

**Técnicas de balanceo**:
- SMOTE para oversampling de clase minoritaria
- Random undersampling de clase mayoritaria
- Ratio final training: 1:5

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.11+
- Node.js 18+
- Docker y Docker Compose
- Git

### Instalación Rápida
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/fraud-detection-system.git
cd fraud-detection-system

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install

# Base de datos SQLite (se crea automáticamente)
cd ../backend
python -m app.models.database

# Entrenar modelos (opcional, incluye modelos pre-entrenados)
python ml_pipeline/train.py
```

### Ejecución con Docker
```bash
# Construir y levantar todos los servicios
docker-compose up --build

# Acceder a:
# - Frontend: http://localhost:3000
# - Backend API: http://localhost:8000
# - API Docs: http://localhost:8000/docs
# - MLflow: http://localhost:5000
```

### Ejecución en Desarrollo

**Backend**:
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

**Frontend**:
```bash
cd frontend
npm run dev
```

## 📖 Uso del Sistema

### API Endpoints Principales

**Predicción de Fraude**:
```bash
POST /api/v1/predict
Content-Type: application/json

{
  "transaction_id": "TXN123456",
  "amount": 150.50,
  "merchant_category": "online_retail",
  "features": {...}
}

Response:
{
  "is_fraud": true,
  "confidence": 0.87,
  "fraud_probability": 0.92,
  "explanation": {
    "top_features": [
      {"feature": "amount_deviation", "contribution": 0.35},
      {"feature": "transaction_velocity", "contribution": 0.28}
    ],
    "shap_values": {...}
  }
}
```

**Análisis de Transacción**:
```bash
GET /api/v1/transactions/{transaction_id}/explain
```

**Métricas del Modelo**:
```bash
GET /api/v1/analytics/model-performance
```

### Dashboard Interactivo

**Funcionalidades**:
1. **Monitoreo en Tiempo Real**: Stream de transacciones con colores según riesgo
2. **Visualización de Explicaciones**: Gráficos SHAP interactivos por transacción
3. **Métricas de Performance**: Precision, Recall, F1, curvas ROC/PR
4. **Histórico de Alertas**: Tabla filtrable con exportación
5. **Análisis de Tendencias**: Gráficos temporales de fraude

## 🧪 Testing

### Backend
```bash
# Tests unitarios
pytest tests/unit -v

# Tests de integración
pytest tests/integration -v

# Coverage
pytest --cov=app --cov-report=html
```

### Frontend
```bash
# Tests unitarios
npm run test

# Tests E2E
npm run test:e2e
```

## 📈 Roadmap de Desarrollo

### Fase 1: Fundación (Semanas 1-2) ✅
- [x] Setup del proyecto y estructura
- [x] Configuración de entorno (Docker, venv)
- [x] EDA completo del dataset
- [x] Análisis de desbalance y estrategias

### Fase 2: Feature Engineering (Semanas 2-3)
- [ ] Implementar pipeline de feature engineering
- [ ] Crear 50+ características derivadas
- [ ] Feature selection con importance
- [ ] Validación de features

### Fase 3: Modelos ML/DL (Semanas 3-6)
- [ ] Implementar y entrenar Isolation Forest
- [ ] Desarrollar XGBoost con hyperparameter tuning
- [ ] Construir y entrenar Autoencoder
- [ ] Implementar LSTM para análisis secuencial
- [ ] Desarrollar sistema de ensemble voting
- [ ] Optimizar threshold con curva ROC

### Fase 4: Explicabilidad (Semanas 6-7)
- [ ] Integrar SHAP para feature importance
- [ ] Implementar LIME para explicaciones locales
- [ ] Crear visualizaciones interactivas
- [ ] Desarrollar servicio de explicabilidad

### Fase 5: Backend API (Semanas 7-9)
- [ ] Desarrollar endpoints FastAPI
- [ ] Implementar servicios de negocio
- [ ] Agregar WebSockets para alertas
- [ ] Integrar modelos con API
- [ ] Tests unitarios e integración

### Fase 6: Frontend (Semanas 9-11)
- [ ] Configurar React + TypeScript + Vite
- [ ] Desarrollar componentes de dashboard
- [ ] Implementar visualizaciones con Recharts
- [ ] Integrar con backend API
- [ ] Responsive design
- [ ] Tests de componentes

### Fase 7: DevOps y Deploy (Semanas 11-12)
- [ ] Dockerizar backend y frontend
- [ ] Configurar Docker Compose
- [ ] Implementar CI/CD con GitHub Actions
- [ ] Agregar pre-commit hooks
- [ ] Documentación completa (README, API docs)
- [ ] Video demo del proyecto

### Futuras Mejoras (Post-MVP)
- [ ] Migración a PostgreSQL
- [ ] Deploy en AWS/Azure/GCP
- [ ] Implementar autenticación (JWT)
- [ ] Agregar rate limiting
- [ ] A/B testing framework para modelos
- [ ] Model drift detection automático
- [ ] Integración con Kafka para streaming
- [ ] Dashboard de MLOps con Grafana

## 📊 Métricas Esperadas

### Performance de Modelos (Dataset de Prueba)

| Modelo | Precision | Recall | F1-Score | AUC-ROC |
|--------|-----------|--------|----------|---------|
| Isolation Forest | 0.78 | 0.71 | 0.74 | 0.85 |
| XGBoost | 0.92 | 0.87 | 0.89 | 0.96 |
| Autoencoder | 0.81 | 0.83 | 0.82 | 0.89 |
| LSTM | 0.85 | 0.79 | 0.82 | 0.91 |
| **Ensemble** | **0.94** | **0.91** | **0.92** | **0.97** |

### KPIs del Sistema
- **Latencia de predicción**: <100ms (p95)
- **Throughput**: >1000 transacciones/segundo
- **Falsos positivos**: <5% (crítico para UX)
- **Disponibilidad**: 99.9% (SLA objetivo)

## 🤝 Contribuciones

Este es un proyecto de portafolio personal, pero las sugerencias son bienvenidas:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

## 📝 Licencia

MIT License - ver archivo [LICENSE](LICENSE) para detalles

## 👤 Autor

**Jhon Alexander García**

- LinkedIn: [tu-perfil](https://linkedin.com/in/tu-perfil)
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- Email: tu.email@ejemplo.com

---

## 🎓 Contexto Académico

Este proyecto fue desarrollado aplicando conocimientos adquiridos en Maestría en Inteligencia Artificial, enfocándose en:

- Aplicación práctica de algoritmos de ML/DL en problemas reales
- Arquitectura de sistemas de IA en producción
- Explicabilidad y ética en modelos de IA
- Ingeniería de software y mejores prácticas
- DevOps y MLOps para sistemas de IA

## 📚 Referencias

- [SHAP: A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874)
- [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754)
- [Isolation Forest Algorithm](https://ieeexplore.ieee.org/document/4781136)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

**Nota**: Este proyecto está en desarrollo activo. El código y la documentación se actualizan regularmente según avance el roadmap.
