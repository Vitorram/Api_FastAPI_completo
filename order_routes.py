from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import pegar_sessao, verificar_token
from schemas import PedidoSchema, itemPedidoSchema
from models import Pedido, Usuario, ItensPedido
order_routes = APIRouter(prefix="/order", tags=["Pedidos"], dependencies=[Depends(verificar_token)])

@order_routes.get("/")
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

@order_routes.post("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    
    
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=403, detail="Acesso negado para cancelar este pedido")
    pedido.status = "CANCELADO"
    session.commit()
    return {"Mensagem":f"Pedido {pedido.id} cancelado com sucesso",
            "pedido": pedido
        }

@order_routes.get("/listar")
async def listar_pedidos(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    if usuario.admin == False:
        raise HTTPException(status_code=403, detail="Acesso negado para listar pedidos")
    pedidos = session.query(Pedido).all()
    return {"pedidos": pedidos}

@order_routes.post("/pedido/adicionar_item/{id_pedido}")
async def adicionar_item_pedido(item_schema: itemPedidoSchema, id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail="Acesso negado para adicionar item a este pedido")
    item_pedido = ItensPedido(
        quantidade=item_schema.quantidade,
        sabor=item_schema.sabor,
        tamanho=item_schema.tamanho,
        preco_unitario=item_schema.preco_unitario,
        pedido=pedido.id
    )
    session.add(item_pedido)
    session.commit()

    itens_do_pedido = session.query(ItensPedido).filter(ItensPedido.pedido == id_pedido).all()
    pedido.calcular_preco_total(itens_do_pedido)
    session.commit()

    return {"Mensagem":f"Item adicionado ao pedido {pedido.id} com sucesso",
            "pedido": pedido.id,
            "itens": itens_do_pedido
        }


@order_routes.delete("/pedido/remover/{id_item_pedido}")
async def remover_item_pedido(id_item_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    item = session.query(ItensPedido).filter(ItensPedido.id == id_item_pedido).first()
    if not item:    
        raise HTTPException(status_code=404, detail="Item do pedido não encontrado")
    pedido = session.query(Pedido).filter(Pedido.id == item.pedido).first()
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=403, detail="Acesso negado para remover item deste pedido")
    pedido.preco -= item.quantidade * item.preco_unitario
    session.delete(item)
    session.commit()
    return {"Mensagem":f"Item {id_item_pedido} removido do pedido {pedido.id} com sucesso"}

#finalizar pedido
@order_routes.post("/pedido/finalizar/{id_pedido}")
async def finalizar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=403, detail="Acesso negado para finalizar este pedido")
    pedido.status = "FINALIZADO"
    session.commit()
    return {"Mensagem":f"Pedido {pedido.id} finalizado com sucesso",
            "pedido": pedido
        }

#Visualizar 1 pedido
@order_routes.get("/pedido/{id_pedido}")
async def visualizar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=403, detail="Acesso negado para visualizar este pedido")
    itens_do_pedido = session.query(ItensPedido).filter(ItensPedido.pedido == id_pedido).all()

    return {"pedido": pedido,
            "itens": itens_do_pedido
        }

#Listar pedidos do usuário
@order_routes.get("/meus_pedidos")
async def listar_meus_pedidos(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    pedidos = session.query(Pedido).filter(Pedido.usuario == usuario.id).all()
    return {"pedidos": pedidos}

