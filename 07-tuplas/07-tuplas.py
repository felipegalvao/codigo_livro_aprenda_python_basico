# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 7: Tuplas

# Definindo nossa primeira tupla
tupla1 = ("Gato", "Cachorro", "Papagaio", "Tartaruga")
print(tupla1)

# Acessando um elemento da tupla; mesmo formato das listas, com colchetes
print(tupla1[2])

# Slicing de uma tupla; pegando um intervalo; mesmo formato das listas
print(tupla1[1:3])

# Criando uma tupla vazia
tupla_vazia = ()
print(tupla_vazia)

# Não é possível fazer a alteração de um elemento da tupla; Python retorna um erro
# tupla1[1] = "Elefante"

# Para apagar uma tupla, usa-se del()
# del(tupla1)
# print(tupla1)

# Algumas funções úteis para se trabalhar com tuplas
tupla2 = (8.3, 9.4, 3.3, 7.5, 7.6)
print(max(tupla2))
print(min(tupla2))
print(len(tupla2))

# Transformando uma tupla em lista e vice-versa
lista1 = list(tupla1)
print(lista1)
lista2 = ["José", "Afonso", "Carlos", "Luiz"]
tupla3 = tuple(lista2)
print(tupla3)