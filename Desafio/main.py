import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, mainloop



# Função para ler o arquivo CSV usando Pandas
def ler_dados():
    return pd.read_csv('C:/User/aluno/Desafio/Desafio/dados.csv')

# Função para calcular estatísticas usando NumPy
def calcular_estatisticas(dados):
    vendas = dados['vendas'].values
    return {
        'Média': np.mean(vendas),
        'Mediana': np.median(vendas),
        'Desvio Padrão': np.std(vendas),
        'Máximo': np.max(vendas),
        'Mínimo': np.min(vendas)
    }

# Função para mostrar as estatísticas em um label
def mostrar_estatisticas():
    estatisticas = calcular_estatisticas(dados)
    texto = "\n".join([f"{key}: {value}" for key, value in estatisticas.items()])
    label_estatisticas.config(text=texto)

# Função para gerar um gráfico de barras
def grafico_barras():
    dados.plot(kind='bar', x='vendedor', y='vendas')
    plt.title('Gráfico de Barras')
    plt.show()

# Função para gerar um gráfico de linhas
def grafico_linhas():
    dados.plot(kind='line', x='vendedor', y='vendas')
    plt.title('Gráfico de Linhas')
    plt.show()

# Função para gerar um gráfico de pizza
def grafico_pizza():
    vendas = dados['vendas']
    vendedores = dados['vendedor']
    plt.pie(vendas, labels=vendedores, autopct='%1.1f%%')
    plt.title('Gráfico de Pizza')
    plt.show()

# Função para gerar um gráfico de dispersão
def grafico_dispersao():
    plt.scatter(dados['vendedor'], dados['vendas'])
    plt.title('Gráfico de Dispersão')
    plt.xlabel('Vendedor')
    plt.ylabel('Vendas')
    plt.show()

# Função para gerar um histograma
def histograma():
    plt.hist(dados['vendas'], bins=5)
    plt.title('Histograma')
    plt.xlabel('Vendas')
    plt.ylabel('Frequência')
    plt.show()

# Leitura dos dados
dados = ler_dados()

# Criação da interface gráfica com Tkinter
janela = Tk()
janela.title("Análise de Vendas")

# Criação dos botões
Button(janela, text="Gráfico de Barras", command=grafico_barras).pack()
Button(janela, text="Gráfico de Linhas", command=grafico_linhas).pack()
Button(janela, text="Gráfico de Pizza", command=grafico_pizza).pack()
Button(janela, text="Gráfico de Dispersão", command=grafico_dispersao).pack()
Button(janela, text="Histograma", command=histograma).pack()

# Label para mostrar as estatísticas
label_estatisticas = Label(janela, text="")
label_estatisticas.pack()

# Botão para mostrar as estatísticas
Button(janela, text="Mostrar Estatísticas", command=mostrar_estatisticas).pack()

# Iniciar o loop da interface gráfica
mainloop()
