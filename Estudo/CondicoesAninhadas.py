nome = str(input('Qual é o seu nome ? \n'))
if nome == 'Gustavo':
    print('Que nome bonito.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {} !'.format(nome))
# or é o || do python
