teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
galera.append(teste[:])
#SE NÃO COLOCAR O [:] AO ALTERAR A LISTA TESTE VAI ALTERAR EM GALERA TBM
print(galera)

teste[0] = 'Maria'
teste[1] = 22

galera.append(teste[:])
print(galera)

galera2 = [['Joao', 19], ['Ana', 33], ['Joaquim', 33], ['Maria', 45]]
print(galera2[3][0])
print(galera2[3][1])

for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade')
