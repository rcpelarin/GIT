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

lista = []

@app.post('/cadastro')
def cadastro(carro: Carro):
    try:
        lista.append(carro)
        return {'Status': 'Carro cadastrado'}
    except:
        return {'Status': 'Erro'}

@app.post('/consulta')
def consulta(opcao: int == 0):
    opcao = int(input('Digite 0 para ver todos, 1 para filtrar os não vendidos e 2 para filtrar os vendidos: '))
    if opcao == 0:
        return (lista)
    elif opcao == 1:
        return list(filter(lambda x: x.vendido == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.vendido == True, lista))
    else:
        return ('Opção Inválida')
    
