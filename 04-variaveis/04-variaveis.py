# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 4: Variáveis

# Definição das primeiras variáveis
a = 3
b = 7
print(a+b)

# Mudança de tipo de uma variável
a = "Agora uma string"
print(a)

# Definindo uma variável com base no valor atual de outra
b = a
print(b)

# Definição de múltiplas variáveis com valores iguais
x = y = z = 10
print(x)
print(y)
print(z)

# Definição de múltiplas variáveis com valores diferentes
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

# Captação de input do usuário
nome = input("Olá, qual o seu nome?\n")
print("Olá, %s" % nome)