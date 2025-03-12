''' DICIONARIO '''

'''
- CHAVE: VALOR
- A CHAVE DEVE SER ÚNICA NO DICIONÁRIO 
- MUTABILIDADE 
- 
'''

dados_pessoais = {'nome_completo': 'Kleber Matos', 'cpf': '154.897.657-93', 'e-mail': 'klebinprefeito@gmail.com', 'spa': 12341348129, 'mts': '12n34j3149u1u3902!@#$!%'}

print(dados_pessoais)

print('-'*100)

# Capturando valor associado a chave
print(dados_pessoais['nome_completo'])

# get() -> Captura o valor ou imprime uma mensagem caso a chave não esteja no dicionario
print(dados_pessoais.get('nome_completo', 'Essa chave não pertence ao dicionário'))

print('-'*100)

# Atribuindo um novo valor para a chave 'nome_Completo'
dados_pessoais['nome_completo'] = 'Xaropinho do Ratinho'

# Impressão do novo valor
print(f'O nome completo passa a ser: {dados_pessoais['nome_completo']}')

# Deletando os dados 
del dados_pessoais['spa']
print(f'o valor excluido foi: {dados_pessoais.pop('mts')}')

print('-'*100)
print('DICIONARIO APOS A REMOCAO')
print(dados_pessoais)

print('-'*100)

atualizacao = {'nome_completo': 'Kleber Matos', 'idade': 258, 'profissao': 'Engenheiro'}
# Atualiza o dicionario com novas informações.
# Caso a atualização contenha uma chave que ja esteja no dicionario, seu valor é modificado
dados_pessoais.update(atualizacao)
print(dados_pessoais)

print('-'*100)
print(f' As chaves no dicionário são: {dados_pessoais.keys()}')
print(f' Os valores no dicionário são: {dados_pessoais.values()}')

print('-'*100)
print('ITERAÇÃO NO DICIONARIO')

for chaves,valores in dados_pessoais.items():
    print(f'A chave {chaves} está associado ao valor {valores}')
    