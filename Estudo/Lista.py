#LISTAS SÃO MUTAVEIS

num = [2, 5, 9, 1]
lista = list()


#add
num.append(7)

#ordena
num.sort()

#quantidade de elementos
quantidade = len(num)

#adiciona na posicao
num.insert(2, 0)

#remove com parametro ou sem
num.pop()

#remove
num.remove(2)

for c, v in enumerate(num):
    print(f'Na posicao {c} encontrei o valor {v} !')
print('Cheguei ao final da lista.')
