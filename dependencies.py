from models import Usuario, db
from sqlalchemy.orm import sessionmaker, Session
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from main import SECRET_KEY, ALGORITIM
from jose import jwt, JWTError

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def pegar_sessao():
    try:
        session = sessionmaker(bind=db)
        session = session()
        yield session
    finally:
        session.close()

from dotenv import load_dotenv
import os
from passlib.context import CryptContext # Se ainda não estiver aí

load_dotenv()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
outh_2 = OAuth2PasswordBearer(tokenUrl="auth/login")
# ... suas outras funções
    
def verificar_token(token:str = Depends(outh_2), session = Depends(pegar_sessao)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITIM])
        id_usuario = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return usuario
