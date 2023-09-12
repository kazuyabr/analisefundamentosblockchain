import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from src.routes.main import router as mainRouter

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")

# CORS
origins = [
    'https://zapsign-gpt-client-production.up.railway.app',
    'https://zapsign-gpt-client-production.up.railway.app:443'
    ]



description = """
Ola meus queridos, criamos essa API para melhor gerenciarmos os bots de nosso sistema. 🚀

## Items

Você pode **ler tudo**.

## Users

Você podera criar seus bots, documentos e associa-los:

* **Projeto iniciado** (_Versão MVP_).
"""

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Analise Fundamentalista - API",
        description=description,
        version="0.0.1",
        terms_of_service="https://jogatinando.com/#terms",
        routes=app.routes,
        contact={
        "name": "Sulivan T. Leite",
        "url": "https://jogatinando.com/#contact",
        "email": "contato@jogatinando.com",
    },    
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Adicionando documentação da API de forma personalizada
app.openapi = custom_openapi

# Proteção de CORS
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas
app.include_router(mainRouter, tags=["Principal"])

# Iniciação da comunicação com o banco de dados
# @app.on_event("startup")
# async def startup():
#     await database.connect()
    
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
    