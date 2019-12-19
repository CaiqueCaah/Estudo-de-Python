#TUPLAS SÃO IMUTAVEIS

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1])

for comida in lanche:
    print(f'eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])
print('comi pra caramba !')
