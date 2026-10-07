# FastAPI Auth API

API REST desenvolvida com **FastAPI** para praticar uma arquitetura de backend organizada, autenticação JWT e persistência de dados.

## Sobre o projeto

O projeto implementa uma API com autenticação e operações de CRUD, utilizando banco de dados relacional, migrations e validação de dados.

A proposta foi aplicar conceitos comuns em aplicações backend modernas, mantendo responsabilidades separadas e uma base preparada para evolução.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- MySQL
- JWT
- bcrypt
- Uvicorn
- Docker

## Funcionalidades

- Autenticação com JWT
- Hashing de senhas
- CRUD
- Validação de dados com Pydantic
- Persistência com SQLAlchemy
- Migrations com Alembic
- Documentação automática via Swagger e ReDoc

## Como executar

### 1. Clone o projeto
```bash
git clone https://github.com/Vitorram/Api_FastAPI_completo.git
cd Api_FastAPI_completo
```

### 2. Crie e ative o ambiente virtual

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo .env:
```
DATABASE_URL=mysql+pymysql://user:password@localhost/db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Execute as migrations
```bash
alembic upgrade head
```

### 6. Inicie a API
```bash
uvicorn app.main:app --reload
```

## Documentação

Com a aplicação em execução:
- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Arquitetura


```text
Cliente
   ↓
FastAPI / Rotas
   ↓
Schemas / Validação
   ↓
Serviços e regras de negócio
   ↓
SQLAlchemy
   ↓
MySQL
```

## Próximos passos

- Adicionar testes automatizados
- Melhorar tratamento global de erros
- Adicionar paginação e filtros
- Criar pipeline de CI
- Publicar uma instância de demonstração

## Autor

**Vitor Ramos**