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

app = FastAPI(
)

app.include_router(auth_routes)
app.include_router(order_routes)



