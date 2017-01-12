# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 8: Dicionários

# Criando nosso primeiro dicionário
aluno = {"nome": "José", "idade": 20, "nota": 9.2}
print(aluno)

# Criando um dicionário vazio
dict_vazio = {}
print(dict_vazio)

# Acessando elementos do dicionário pela chave
print(aluno["nome"])
print(aluno["idade"])

# Acessando uma chave que não existe, o Python retorna um erro
# print(aluno["Peso"])

# Modificando o valor de uma chave em um dicionário
aluno["nota"] = 8.2
# Para criar uma nova chave, basta definir uma chave não existente ainda no Dicionário
aluno["peso"] = 74
print(aluno)

# Removendo uma ou todas as chaves de um dicionário
del aluno["idade"]
print(aluno)
aluno.clear()
print(aluno)

# Funções úteis para se trabalhar com dicionários
aluno = {"nome": "José", "idade": 20, "nota": 9.2}
print(len(aluno))

print("idade" in aluno)
print("peso" in aluno)

print(aluno.get("nome"))
print(aluno.get("peso"))
print(aluno.get("peso", "Não existe"))

print(aluno.items())
print(aluno.keys())  
print(aluno.values())

aluno_original = {"nome": "José", "idade": 20, "nota": 9.2}
aluno_update = {"peso": 75, "nota": 8.7}
aluno_original.update(aluno_update)
print(aluno_original)