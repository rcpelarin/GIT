import re #Regular Expressions - RegEx
endereco = 'Rua Icatu, 390 - Apto 903, Bloco 4, Pq. Industrial - São José dos Campos, SP, 12237-010'

#5 dígitos numéricos + (um hífem (opicional)) + 3 dígitos numéricos

padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')
busca = padrao.search(endereco) # Match
if busca:
    cep = busca.group()
    print(cep)