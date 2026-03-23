from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context


auth_routes = APIRouter(prefix="/auth", tags=["Auth"])


@auth_routes.get("/")
async def home():
    """
    rota padrao para pedidos, todas precisam de auth
    """
    return {"mensagem":"Area para auth"}

@auth_routes.post("/create_user")
async def create_user(nome: str, email: str,senha: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return{"mensagem":"User ja cadastrado com este email"}
    else:
        #criar carinhas
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem":"User Cadastrado"}
    
    
