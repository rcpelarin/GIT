import requests
from acesso_cep import BuscaEndereco

cep = 12237010
objeto_cep = BuscaEndereco(cep)

# r = requests.get("https://viacep.com.br/ws/12237010/json/")
# print(r.text)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, "-", cidade, "-", uf)
