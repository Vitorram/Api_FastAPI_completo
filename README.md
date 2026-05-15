# FastAPI Project

API desenvolvida com FastAPI utilizando autenticação JWT, SQLAlchemy, Alembic e arquitetura escalável para aplicações modernas.

---

# Tecnologias

- Python
- FastAPI
- SQLAlchemy
- Alembic
- JWT Authentication
- MySQL
- Docker
- Uvicorn

---

# Instalação

## 1. Clone o projeto

```bash
git clone <repository_url>
```

---

## 2. Crie o ambiente virtual

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# Requirements

```txt
alembic==1.18.4
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.12.1
bcrypt==5.0.0
cffi==2.0.0
click==8.3.1
cryptography==46.0.5
ecdsa==0.19.1
fastapi==0.135.1
greenlet==3.3.2
h11==0.16.0
idna==3.11
Mako==1.3.10
MarkupSafe==3.0.3
passlib==1.7.4
pyasn1==0.6.3
pycparser==3.0
pydantic==2.12.5
pydantic_core==2.41.5
python-dotenv==1.2.2
python-jose==3.5.0
python-multipart==0.0.22
rsa==4.9.1
six==1.17.0
SQLAlchemy==2.0.48
SQLAlchemy-Utils==0.42.1
starlette==0.52.1
typing-inspection==0.4.2
typing_extensions==4.15.0
uvicorn==0.42.0
```

---

# Variáveis de Ambiente

Crie um arquivo `.env` na raiz:

```env
DATABASE_URL=mysql+pymysql://user:password@localhost/db_name

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Migrações com Alembic

## Criar migration

```bash
alembic revision --autogenerate -m "create tables"
```

## Executar migrations

```bash
alembic upgrade head
```

---

# Executando o Projeto

```bash
uvicorn app.main:app --reload
```

Servidor:

```txt
http://127.0.0.1:8000
```

---

# Documentação Automática

Swagger:

```txt
http://127.0.0.1:8000/docs
```

Redoc:

```txt
http://127.0.0.1:8000/redoc
```

---

# Funcionalidades

- Autenticação JWT
- CRUD completo
- Migrations com Alembic
- Validação com Pydantic
- Arquitetura modular
- Integração com banco de dados
- Segurança com hashing de senhas

---

# Docker

## Build

```bash
docker build -t fastapi-project .
```

## Run

```bash
docker run -p 8000:8000 fastapi-project
```

---

# Autor

Desenvolvido por Vitor Ramos
