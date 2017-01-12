# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 14: Data e Tempo

# Importar a classe date, do módulo datetime, usada para trabalhar com datas
from datetime import date

# Cria nova data, informando o ano, mês e dia
data1 = date(2016, 12, 9)
print(data1)

# Retorna o dia atual, baseado no sistema
print(date.today())

hoje = date.today()

data2 = date(hoje.year, hoje.month, 1)
print(data2)

# Calcular a diferença entre datas
carnaval_2017 = date(2017, 2, 24)
tempo_para_o_carnaval = abs(carnaval_2017 - hoje)
print(tempo_para_o_carnaval.days)

# Métodos para trabalho com datas
print(hoje.weekday())

data2 = data2.replace(day=3)
print(data2)

print(data2.strftime("%d/%m/%Y"))

# Importar a classe time, do módulo datetime, usada para trabalhar com tempo
from datetime import time

tempo1 = time(12, 25, 31, 1333)
print(tempo1)

# Formatação de tempo
print(tempo1.strftime("%H horas, %M minutos e %S segundos"))