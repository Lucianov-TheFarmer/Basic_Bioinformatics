import tkinter as tk
from tkinter import filedialog
from Bio.Seq import Seq
from Bio.SeqUtils import GC 
from Bio import SeqIO
import matplotlib.pyplot  as plt
from pathlib import Path

# Importar genoma
def abrir():
    global genoma
    root = tk.Tk()
    root.withdraw()

    genoma = filedialog.askopenfilenames(title = "Selecione seu(s) genoma(s)") 
    
# Função do gráfico 
def grafico():
    plt.bar(nome_genoma, cont_GC_gen)
    plt.xlabel("Genoma(s)")
    plt.xticks(rotation=15)
    plt.ylabel("Conteúdo GC (%)")
    plt.title("Conteúdo GC")
    plt.show()
    

# Escolher genomas
abrir()

# Variável de posição: Genoma
n_genoma = 0

# Armazenar conteúdos GC dos genomas
global cont_GC_gen
cont_GC_gen = []

# Armazenar nome dos genomas
global nome_genoma
nome_genoma = []

# Colocar genomas numa lista e realizar os cálculos de GC
while n_genoma < len(genoma):

    # Armazenar conteúdo GC das sequências
    global cont_GC
    cont_GC = []

    # Escolher um genoma
    genoma_atual = list(SeqIO.parse(genoma[n_genoma], "fasta"))

    # Recuperar nome do arquivo
    nome_genoma.insert(n_genoma, Path(genoma[n_genoma]).stem)

    # Variável de posição: Sequência dentro do genoma
    n_seq = 0
    
    while n_seq < len(genoma_atual):

        # Isolar sequencia dentro do genoma
        sequencia = genoma_atual[n_seq].seq

        # Inserir conteúdo GC da sequencia na lista
        cont_GC.insert(n_seq, GC(sequencia))

        # Atualizar variável de posição: Sequência dentro do genoma
        n_seq += 1

    # Prints
    print(nome_genoma[n_genoma])        
    print("Para o genoma: " + genoma[n_genoma] + "\nO conteúdo GC é: " + str(round(sum(cont_GC)/len(cont_GC), 4)) + " %") 
    print("--------------------------------")

    # Inserir média do conteúdo GC do genoma numa lista
    cont_GC_gen.insert(n_genoma, round(sum(cont_GC)/len(cont_GC), 4))

    # Atualizar variável de posição: Genoma
    n_genoma += 1

# Plotar gráfico
grafico()

