#uvicorn main:app --reload

#importacção de dependencias
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITIM = os.getenv("ALGORITIM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

#importacção de pastas
from auth_routes import auth_routes
from order_routes import order_routes
from dependencies import bcrypt_context

from fastapi import FastAPI

app = FastAPI(
    title="API de Pedidos de Pizzas",
    description="API para gerenciamento de pedidos de pizzas, incluindo autenticação e autorização.",
    version="1.0.0"
)

app.include_router(auth_routes)
app.include_router(order_routes)



