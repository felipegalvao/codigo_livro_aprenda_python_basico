# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 9: Sets

# Criando nossos primeiros sets
lista1 = ["Luiz", "Alfredo", "Felipe", "Alfredo", "Joana", "Carolina", "Carolina"]
set1 = set(lista1)
print(set1)
set2 = {"cachorro", "gato", "papagaio", "cachorro", "papagaio", "macaco", "galinha"}
print(set2)

# Criando um set a partir de uma string
set3 = set("papagaio")
print(set3)

# Criando uma lista sem duplicatas através dos sets
lista2 = ["Luiz", "Alfredo", "Felipe", "Alfredo", "Joana", "Carolina", "Carolina"]
lista_sem_duplicatas = list(set(lista2))
print(lista_sem_duplicatas)

# Removendo um item do set
print(set2)
set2.remove("cachorro")
print(set2)

# Funções úteis para se trabalhar com sets
print(len(set2))
print("gato" in set2)
print("elefante" in set2)

set4 = {"Luiz", "Alfredo", "Joana", "Felipe", "Mauro"}
set5 = {"Joana", "Carolina", "Afonso", "Carlos", "Mauro"}
print(set4.difference(set5))
print(set4.intersection(set5))

set_backup = set4
print(set_backup)
set4.clear()
print(set_backup)
set()

set4 = {"Luiz", "Alfredo", "Joana", "Felipe", "Mauro"}
set_backup = set4.copy()                               
print(set_backup)
set4.clear()
print(set_backup)