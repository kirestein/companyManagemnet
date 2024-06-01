from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Union
from firebase_admin import credentials, db
from firebase_admin import initialize_app
from variaveis import *


# Use a chave privada que você obteve do Firebase aqui
cred = credentials.Certificate('.env\companymanagement-poc-firebase-adminsdk-k7wtt-1c3ad95f6e.json')
initialize_app(cred, {
    'databaseURL': DATABASE_URL
})

# ref = db.reference("/")
app = FastAPI


# if DATABASE_URL:
#     print(f"URL do banco de dados: {DATABASE_URL}")
# else:
#     print("Variável de ambiente DATABASE_URL não encontrada.")
