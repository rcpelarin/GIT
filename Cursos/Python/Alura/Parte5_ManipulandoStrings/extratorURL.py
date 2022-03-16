url = 'https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'.strip()
url = ' '.strip()

# Validação da URL
if url == '':
    raise ValueError('A URL está vazia')

# Separa base e os parâmetros
separador = url.find('?')
url_base = url[:separador]
url_param = url[separador+1:]
# print(url_param)

# Busca o valor de um parâmetro
busca = 'moedaDestino'
indice_parametro = url_param.find(busca)
indice_valor = indice_parametro + len(busca) + 1
indice_e_comercial = url_param.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_param[indice_valor:]
else:
    valor = url_param[indice_valor:indice_e_comercial]
print(valor)

