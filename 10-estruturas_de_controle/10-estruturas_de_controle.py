# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 10: Estruturas de Controle

# Primeira estrutura de controle: If
nome = input("Digite aqui seu nome: ")

if nome == "Felipe":
  print("Olá, %s" % nome)

if nome == "Felipe":
  print("Olá, %s" % nome)
else:
  print("Olá, visitante")

if nome == "Felipe":
  print("Olá, Felipe")
elif nome == "Maria":
  print("Oi, Maria")
elif nome == "Carlos":
  print("E aí, Carlos?")
else:
  print("Olá, visitante")

# Iterando com for sobre listas
lista = ["Alfredo", "Mario", "José", "Carolina", "Joana", "Luiza"]
for nome in lista:
  print(nome)

# Iterando com for sobre dicionários
aluno = {"nome": "Maria", "idade": 20, "nota": 9.2}

print("Exemplo 1a - iterando sobre chaves")
for chave in aluno:
  print(chave)

print("\nExemplo 1b - iterando sobre chaves")
for chave in aluno.keys():
  print(chave)

print("\nExemplo 2 - iterando sobre valores")
for valor in aluno.values():
  print(valor)

print("\nExemplo 3 - iterando sobre ambos")
for chave, valor in aluno.items():
  print(chave + " - " + str(valor))

# Utilizando range para criar um intervalo de números
print("Range com 1 parâmetro")
for i in range(5):
  print(i)

print("Range com 2 parâmetros")    
for i in range(3,10):
  print(i)

# Break e continue em loops
print("Exemplo break")
for i in range(1,11):
    if i % 5 == 0:
        break
    print(i)
    
print("Exemplo continue")
for i in range(1,11):
  if i % 5 == 0:
      continue
  print(i)

# Exemplo do loop while
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1

# Exemplo com condição while true e break
while True:
  nome = input("Digite seu nome ou sair para terminar o programa: ")
  if nome == "sair":
    break
  else:
    print("Olá, %s" % nome)