from Bio import SeqIO
import tkinter as tk
from tkinter import filedialog

### Escrito em 02/02/2023, por Vitor Luciano

# Importar FASTA
def abrir():
    global fasta
    root = tk.Tk()
    root.withdraw()

    fasta = filedialog.askopenfilename(title = "Selecione seu arquivo Fasta")
    
# Diretório de destino
def destino():
    global local_destino
    root = tk.Tk()
    root.withdraw()

    local_destino = filedialog.askdirectory(title = "Onde salvar?")    

# Escolher arquivo fasta e onde salvar
abrir()
destino()

# Definir os genes e colocá-los numa lista
genes = list(SeqIO.parse(fasta, "fasta"))

# Variável de posição
n = 0

# Loop de processamento: Transcrição
for x in genes:

    # Transcrever sequência
    gene = x.seq
    seq_transcrita = gene.transcribe()
    
    # Inserir o gene transcrito na respectiva posição
    genes[n].seq = seq_transcrita

    # Salvar Fasta transcrito
    SeqIO.write(genes, local_destino+"/Transcrição.fna", "fasta")

    # Atualizar variável de posição
    n += 1

# Resetar variável de posição
n = 0

# Loop de processamento: Tradução
for x in genes:
    
    # Traduzir sequência
    gene = x.seq
    seq_transcrita = gene.transcribe()
    seq_traduzida = seq_transcrita.translate()

    # Inserir o gene traduzido na respectiva posição
    genes[n].seq = seq_traduzida

    # Salvar Fasta traduzido
    SeqIO.write(genes, local_destino+"/Tradução.fna", "fasta")

    # Atualizar variável de posição
    n += 1

print("Concluído.\nArquivos salvos em: "+local_destino)



