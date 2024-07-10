# Importando uma biblioteca sem alias
import matplotlib  # Importa a biblioteca matplotlib

print(matplotlib.__version__)  # Imprime a versão da biblioteca matplotlib
print(matplotlib.__class__)  # Imprime a classe da biblioteca matplotlib

# Importando uma biblioteca com alias
import matplotlib.pyplot as plt  # Importa o módulo pyplot da biblioteca matplotlib com alias plt

estudantes = ["João", "Maria", "José"]
notas = [8.5, 9, 6.5]

plt.bar(x=estudantes, height=notas)  # Cria um gráfico de barras com os estudantes e suas notas

plt.show()  # Mostra o gráfico na tela
