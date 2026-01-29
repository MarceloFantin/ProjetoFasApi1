#pip  install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart
#para executar no terminal usar o comando uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()