from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido
order_routes = APIRouter(prefix="/order", tags=["Pedidos"])

@order_routes.get("")
async def listar():
    return {"Mensagem":"Rota de pedidos"}

@order_routes.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(
        usuario=pedido_schema.usuario
    )
    session.add(novo_pedido)
    session.commit()
    return {"Mensagem":f"Pedido criado com sucesso: {novo_pedido.id}"}