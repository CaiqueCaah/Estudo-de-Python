# MANIPULANDO UMA STRING EM PYTHON
frase = 'Curso em Video Python'
print(frase[9:14])
print(frase[9:])
print(frase[:14])
print('______________________________________________________')
print('Qual é o tamanho da frase ', len(frase))
print('Quantos >O< tem na frase ? ', frase.count('o'))
print('Em qual posição tem a palavra >vi< na frase ? ', frase.find('Vi'))
print('________________________________________________________')
print('Trocando a palavra Python por Java \n', frase.replace('Python', 'Java'))
print('Aumentando todas as letras = ', frase.upper())
print('Diminuindo todas as letras = ', frase.lower())
print('Colocando a primeira letra em maiscula e o resto minusculo = ', frase.capitalize())
print('Colocando a primeira letra de cada palavra em maisculo = ', frase.title())
frase2 = '   Teste Teste   '
print('Removendo os espaços desnecessarios da frase = ', frase2.strip())
print('Removendo apanas os espaços do final = ', frase2.rstrip())
print('Removendo apanas os espaços do começo = ', frase2.lstrip())
print('________________________________________________________')
lista = [frase2.split()]
print('Dividindo a frase ', lista)
print('Juntar a frase ', '-'.join(frase2))
