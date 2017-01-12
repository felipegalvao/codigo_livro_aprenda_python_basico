# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 16: Arquivos

file = open("nomes.txt", "r")
print(file.read())

print("\n")

file = open("nomes.txt", "r")
print(file.read(10))

print("\n")

file = open("nomes.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())

print("\n")

file = open("nomes.txt", "r")
print(file.readlines())

print("\n")

file = open("novo_arquivo.txt", "w")
file.write("Testando, testando!\n")
file.write("Mais uma linha para testar")
file.close()

file = open("novo_arquivo.txt", "w")
file.write("Novo texto, mesmo arquivo")
file.close()

file = open("novo_arquivo.txt", "a")
file.write("\nTexto adicionado ao arquivo com o modo a")
file.close()

file = open("novo_arquivo.txt", "r+")
file.write("Testando r+")
file.seek(15)
file.write("Novo teste do r+")
file.seek(0)
print(file.read())
file.close()