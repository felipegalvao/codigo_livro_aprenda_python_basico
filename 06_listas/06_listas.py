# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 6: Listas

# Definindo as primeiras listas
alunos = ["José", "João", "Luiz"]
notas = [8.5, 9.2, 6.7]
print(alunos)
print(notas)
lista_vazia = []
print(lista_vazia)

# Lista com itens de diferentes tipos
lista_misturada = [12, 15.56, "Sorveteria", ["Baunilha", "Chocolate"]]
print(lista_misturada)

# Acessando elementos das listas
print(alunos[0])
print(notas[2])

print(alunos[-1])
print(alunos[-3])

# Modificando elementos de uma lista
print(notas)
notas[2] = 7.7
print(notas)

# Adicionando itens a uma lista
print(alunos)
alunos.append('Alfredo')
print(alunos)

print(alunos)
alunos.insert(1, "Daniela")
print(alunos)

print(alunos)
novos_alunos = ['Carlos', 'Maria', 'Ana']
alunos.extend(novos_alunos)
print(alunos)

alunos1 = ['José', 'Daniel', 'João']
alunos2 = ['Maria', 'Ana', 'Carolina']
print(alunos1 + alunos2)

print(notas*2)

# Removendo itens da lista
print(alunos)
alunos.remove('João')
print(alunos)

print(alunos)
aluno_removido = alunos.pop()
print(aluno_removido)
print(alunos)
aluno_removido = alunos.pop(2)
print(aluno_removido)
print(alunos)

alunos = ['José', 'Denis', 'Daniela', 'Carla', 'Carlos', 'Augusto', 'Denis']
print(alunos)
alunos.remove('Denis')
print(alunos)

# Slicing de listas - pegar partes da lista baseado em intervalos definidos
print(alunos)
print(alunos[0:2])
print(alunos[2:4])
print(alunos[2:5])

print(alunos[:3])
print(alunos[3:])

print(alunos[1:-1])
print(alunos[2:-2])

# Funções úteis para trabalhar com strings
print(len(alunos))

print(max(notas))
print(min(notas))

alunos_backup = alunos
print(alunos_backup)
alunos.clear()
print(alunos_backup)

alunos = ['José', 'Daniela', 'Carla', 'Carlos', 'Augusto', 'Denis']
alunos_backup = alunos.copy()
print(alunos_backup)                                  
alunos.clear()                                        
print(alunos_backup)

alunos = ['José', 'Daniela', 'Carla', 'Carlos', 'Augusto', 'Denis']

alunos.extend(['Daniela', 'Carla', 'Daniela'])
print(alunos.count('Daniela'))

alunos.sort()
print(alunos)

alunos.reverse()
print(alunos)

print("José" in alunos)
print("Felipe" in alunos)

alunos_string = "; ".join(alunos)
print(alunos_string)
alunos_lista = alunos_string.split("; ")
print(alunos_lista)