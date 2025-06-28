from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.scan import router as scan_router

app = FastAPI(
    title="Vigilant WebGuard",
    description="Plataforma avanzada de análisis ofensivo web",
    version="1.0.0"
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enrutadores
app.include_router(scan_router, prefix="/api")
