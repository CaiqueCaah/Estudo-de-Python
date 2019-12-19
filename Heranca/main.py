from Heranca.pessoa import Pessoa
from Heranca.cliente import Cliente
from Heranca.funcionario import Funcionario

pessoa = Pessoa('Joãozinho', 22)
cliente = Cliente('Maria', 30)
funcionario = Funcionario('Pedro', 15)

print(cliente.nome, cliente.idade)
cliente.falar()
print(funcionario.nome, funcionario.idade)
funcionario.falar()
print(pessoa.nome, pessoa.idade)
pessoa.falar()
