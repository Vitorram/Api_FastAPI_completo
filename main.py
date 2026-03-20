#uvicorn main:app --reload

#importacção de dependencias
from fastapi import FastAPI

#importacção de pastas
from auth_routes import auth_routes
from order_routes import order_routes

app = FastAPI(
   
)
app.include_router(auth_routes)
app.include_router(order_routes)



