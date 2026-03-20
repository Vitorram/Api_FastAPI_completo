from fastapi import APIRouter

order_routes = APIRouter(prefix="/order", tags=["Pedidos"])

@order_routes.get("")
async def listar():
    return {"Mensagem":"Rota de pedidos"}