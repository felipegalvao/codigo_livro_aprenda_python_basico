# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 15: Exceções

print("Vamos dividir dois números inseridos por você\n")
num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")

# resultado = int(num1) / int(num2)
# print("O resultado é " + str(resultado))

# try:
#   resultado = int(num1) / int(num2)
#   print("O resultado é " + str(resultado))
# except ZeroDivisionError:
#   print("O segundo número não pode ser zero")
# except ValueError:
#   print("Você deve inserir dois números")

# try:
#   resultado = int(num1) / int(num2)
#   print("O resultado é " + str(resultado))
# except:
#   print("Uma das entradas é inválida. Favor inserir dois números, sendo o segundo diferente que zero")

# Blocos else e finally em exceções
try:
  resultado = int(num1) / int(num2)
  print("O resultado é " + str(resultado))
except ZeroDivisionError:
  print("O segundo número não pode ser zero")
except ValueError:
  print("Você deve inserir dois números")
else:
  print("Divisão feita!")
finally:
  print("Programa concluído")

# Chamando exceções dentro do seu código com "raise"
nome = input("Qual o seu nome? ")
try:
  if nome == "Felipe":
    raise NameError("Não gostei do seu nome")
  print("Olá, %s" % nome)
except NameError:
  print("O programa não gostou do seu nome")