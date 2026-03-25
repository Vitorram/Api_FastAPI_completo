from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


db = create_engine("sqlite:///banco.db")

# base
Base = declarative_base()


# criando as classes 
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("name", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("adm", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo, admin):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedido(Base):
    __tablename__ = "pedidos"


    id = Column("id", Integer, primary_key=True, autoincrement=True)
    usuario = Column("usuario", Integer, ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    status = Column("status", String, default="PENDENTE")

    
    itens = relationship("ItensPedido", backref="pedido_obj")

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
    
    def calcular_preco_total(self, itens):
        total = 0
        for item in itens:
            total += item.quantidade * item.preco_unitario
        self.preco = total


class ItensPedido(Base):
    __tablename__ = "itens_pedidos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", Integer, ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido