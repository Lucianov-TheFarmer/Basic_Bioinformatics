from Bio import SeqIO
import tkinter as tk
from tkinter import filedialog

# Importar FASTA
def abrir():
    global fasta
    root = tk.Tk()
    root.withdraw()

    fasta = filedialog.askopenfilename(title = "Selecione seu arquivo Fasta")
abrir()

strings = list(SeqIO.parse(fasta, "fasta"))

countsA = []
countsT = []
countsC = []
countsG = []

for string in strings:
    m = 0
    string_len = len(string.seq)
    while string_len != 0:
        countsA.insert(m, 0)
        countsT.insert(m, 0)
        countsC.insert(m, 0)
        countsG.insert(m, 0)
        m += 1
        string_len -= 1
    break

for string in strings:

    n = 0
    
    while n < len(string.seq):
    
        if string[n] == "A":
            countsA[n] += 1

        elif string[n] == "T":
            countsT[n] += 1

        elif string[n] == "C":
            countsC[n] += 1

        elif string[n] == "G":
            countsG[n] += 1

        n += 1

consensus = str("")
dicionario = {}
x = len(countsA)
y = 0

while x != 0:

    dicionario["A"] = countsA[y]
    dicionario["C"] = countsC[y]
    dicionario["G"] = countsG[y]
    dicionario["T"] = countsT[y]

    var = max(dicionario.values())
    nucleotideo = list(dicionario.keys())[list(dicionario.values()).index(var)]
    consensus = consensus + str(nucleotideo)

    x -= 1; y += 1

print(consensus)

print("A:",str(countsA)[1:-1].replace(",", ""))
print("C:",str(countsC)[1:-1].replace(",", ""))
print("G:",str(countsG)[1:-1].replace(",", ""))
print("T:",str(countsT)[1:-1].replace(",", ""))

f = open(fasta[:-6]+"_output.txt", "w")
texto = [consensus, "\nA: " , str(countsA)[1:-1].replace(",", "") , "\nC: " , str(countsC)[1:-1].replace(",", "") , "\nG: " , str(countsG)[1:-1].replace(",", "") , "\nT: " , str(countsT)[1:-1].replace(",", "")]
f.writelines(texto)

