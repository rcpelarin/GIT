from cpf_cnpj import Documento

exemplo_cpf = "80802958834"
documento_cpf = Documento.cria_documento(exemplo_cpf)
print('CPF:', documento_cpf)

exemplo_cnpj = "35379838000112"
documento_cnpj = Documento.cria_documento(exemplo_cnpj)
print('CNPJ:', documento_cnpj)
