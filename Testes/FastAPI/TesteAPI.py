from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Carro(BaseModel):
    veiculo: str
    marca: str
    ano: int
    descricao: Optional[str]
    vendido: bool
    created: date
    updated: date

lista = [
    Carro(
        veiculo='Ka', 
        marca='Ford',
        ano=2009,
        descricao='120.000 Km rodados',
        vendido=False,
        created='2021-10-30T13:54:23.138Z',
        updated='2021-10-30T14:30:26.138Z'
    )
]

@app.post('/carro')
def cadastro(carro: Carro):
    lista.append(carro)
    return ('Carro cadastrado')

@app.post('/consulta')
def consulta(opcao: int == 0):
    if opcao == 0:
        return (lista)
    elif opcao == 1:
        return list(filter(lambda x: x.vendido == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.vendido == True, lista))
    
