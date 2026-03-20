from fastapi import APIRouter

auth_routes = APIRouter(prefix="/auth", tags=["Auth"])


@auth_routes.get("/")
async def autenticar():
    """
    rota padrao para pedidos, todas precisam de auth
    """
    return {"mensagem":"Area para auth"}