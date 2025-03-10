''' LISTAS '''

'''
- ARMAZENAR VÁRIOS DADOS DENTRO DESSA LISTA
- MUTAVEIS
- ORDENADA COM BASE NA INSERÇÃO
'''

minha_lista_de_filmes = ['a procura da felicidade', 'Interestellar', 'Escritores da liberdade', 'Harry Potter', 'Vingadores', 'Filme a ser removido', 'O Rapto do menino dourado', 'Senhor dos Anéis', 'Ratatouille', 'Tarzan', 'Rei Leão', 'Star Wars']

print(minha_lista_de_filmes)
print('-'*100)

# append() -> Adiciona elementos na ultima posição
minha_lista_de_filmes.append('As tranças do rei careca')
print(minha_lista_de_filmes)

print('-'*100)

# insert() -> Adiciona o elemento no index desejado
minha_lista_de_filmes.insert(0, 'O Jogo da imitação')
print(minha_lista_de_filmes)

print('-'*100)

minha_lista_de_filmes.append('O Jogo da imitação')
print(minha_lista_de_filmes)

print('-'*100)

# pop() -> Remove o ultimo elemento da lista
# pop(indice) -> Remove o elemento pelo indice indicado
minha_lista_de_filmes.pop(6)
print(minha_lista_de_filmes)

print('-'*100)

# minha_lista_de_filmes.remove('O Jogo da imitação')
print(minha_lista_de_filmes)

print('-'*100)

# index() -> Encontra a posição doe elemento
print(minha_lista_de_filmes.index('Senhor dos Anéis'))

print('-'*100)

print(minha_lista_de_filmes[6])

print('-'*100)

# len(obj) -> Retorna o tamanho da lista
print(len(minha_lista_de_filmes))

print('-' *100)

# count() -> Conta a quantidade de vezes que o elemento aparece na lista
print(f'O jogo da imitação aparece {minha_lista_de_filmes.count('O Jogo da imitação')} vezes')

print('-' *100)

print(minha_lista_de_filmes[  : 3])
print(minha_lista_de_filmes[2 : 10])
print(minha_lista_de_filmes[ 5 : ])

print('-' *100)

minha_lista_de_filmes.append('123143124')
minha_lista_de_filmes.append('123')
minha_lista_de_filmes.append('1')

# sort() -> Ordena a lista
minha_lista_de_filmes.sort()

print(minha_lista_de_filmes)