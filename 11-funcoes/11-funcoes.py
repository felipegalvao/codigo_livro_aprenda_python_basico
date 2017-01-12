# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 11: Funções

# Definição de função sem parâmetros e sem valor de retorno
def print_ola_tres_vezes():
  print("Ola Python")
  print("Ola Python")
  print("Ola Python")
    
print_ola_tres_vezes()

# Definição de uma função com parâmetro e valor de retorno
def numero_ao_cubo(numero):
  valor_a_retornar = numero * numero * numero
  return(valor_a_retornar)
    
numero = numero_ao_cubo(4)
print(numero)

# A chamada da função acima sem argumento retorna um erro
# numero = numero_ao_cubo()

# Definição de função com parâmetro com valor padrão
def print_ola(nome="estranho"):
  print("Olá, " + nome)
    
print_ola("Priscilla")
print_ola()

# Chamada de função com parâmetros nomeados
def print_infos(nome, idade):
  print("Olá, meu nome é %s e tenho %d anos" % (nome, idade))

print_infos(idade=30, nome="Felipe")

# Definição da função com número variável de argumentos: *args e **kwargs
def print_tudo_2_vezes(*args):
  for parametro in args:
    print(parametro + "! " + parametro + "!")

print_tudo_2_vezes("Olá", "Python", "Felipe")

def print_info(**kwargs):
  for parametro, valor in kwargs.items():
    print(parametro + " - " + str(valor))

print_info(nome="Felipe", idade=30, nacionalidade="Brasil")

def print_info_2(nome, idade, **kwargs):
  print("Nome: " + nome)
  print("Idade: " + str(idade))

  print("\nInformações adicionais:")
  for parametro, valor in kwargs.items():
    print(parametro + " - " + str(valor))

print_info_2(nome="Felipe", idade=30, nacionalidade="Brasil", telefone="999998888")