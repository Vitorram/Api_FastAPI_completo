from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from main import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITIM, SECRET_KEY
from dependencies import pegar_sessao, bcrypt_context, verificar_token
from schemas import UsuarioSchema, LoginSchema
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone



auth_routes = APIRouter(prefix="/auth", tags=["Auth"])

def criar_token(id_usuario, duracao= int(ACCESS_TOKEN_EXPIRE_MINUTES)):
    # id_usuario
    # data_expedicao
    
   # Use as classes diretamente, sem o prefixo "datetime."
    data_expiração = datetime.now(timezone.utc) + timedelta(minutes=int(duracao))
    dic_info = {
        "sub":id_usuario,
        "exp": data_expiração
    }
    jwt_token = jwt.encode(dic_info, SECRET_KEY, algorithm=ALGORITIM)
    return jwt_token

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario




@auth_routes.get("/")
async def home():
    """
    rota padrao para pedidos, todas precisam de auth
    """
    return {"mensagem":"Area para auth"}

@auth_routes.post("/create_user")
async def create_user(usuario_request: UsuarioSchema, session = Depends(pegar_sessao)):
    usuario_no_banco = session.query(Usuario).filter(Usuario.email == usuario_request.email).first()
    
    if usuario_no_banco:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    

    senha_criptografada = bcrypt_context.hash(usuario_request.senha)
    
    novo_usuario = Usuario(
        nome=usuario_request.nome, 
        email=usuario_request.email, 
        senha=senha_criptografada
    )
    
    session.add(novo_usuario)
    session.commit()
    
    raise HTTPException(status_code=200, detail="Usuário criado com sucesso")
    
    
# login -> email senha -> criar token JWT 

@auth_routes.post("/login")
async def Login(login_squema: LoginSchema, session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_squema.email, login_squema.senha, session)
    
    if not usuario:
        raise HTTPException(status_code=401, detail="E-mail ou senha inválidos") # 401 é mais correto para falha de auth
    
    # Gerando os tokens
    access_token = criar_token(usuario.email)
    
    # Para o refresh token, passamos o tempo em minutos (7 dias = 10080 minutos)
    tempo_refresh_minutos = 7 * 24 * 60
    refresh_token = criar_token(usuario.email, duracao=tempo_refresh_minutos)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token, 
        "token_type": "bearer"
    }

@auth_routes.get("/refresh")
async def refresh_token(usuario: Usuario = Depends(verificar_token)):
    #verificar token
    usuario = verificar_token(refresh_token)
    acces_token = criar_token(usuario.id)
    return {
        "access_token": acces_token,
        "token_type": "bearer"
    }
