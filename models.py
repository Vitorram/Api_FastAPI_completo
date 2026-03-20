from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy import declarative_base



#crinado a conexção
db = create_engine("sqlite:///banco.db")

#base
Base = declarative_base()

#criando as classes 
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column ("name", String)
    email = Column ("email", String, nullable=False)
    senha = Column ("senha", String)
    ativo = Column ("ativo", Boolean)
    admin = Column ("adm", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
        
#Pedido
#ItensPedidos
#

#exectando metadados