#uvicorn main:app --reload

#importacção de dependencias
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#importacção de pastas
from auth_routes import auth_routes
from order_routes import order_routes

app = FastAPI(
   
)
app.include_router(auth_routes)
app.include_router(order_routes)



