import re
import pandas as pd
from BCBio.GFF import GFFExaminer
from BCBio import GFF
import tkinter as tk
from tkinter import filedialog
import os


### Última modificação em 01/02/2023;
### O objetivo desse script é agrupar os nomes dos genes com seus determinados IDs para posterior mapeamento com dados de RNAseq;
### Script inoperante, reconhece apenas o primeiro gene de seqIDs semelhantes;
### Optei por corrigir os seqIDs no excel, provavelmente será possível fazer tudo por lá.

### Atualização 01/02/2023;
### Observei o parâmetro .features presente no rec do GFF.parse, meu problema estava lá;
### Após as devidas alterações, o script está operante;
### A linha 28 permite filtrar o que se espera pegar no arquivo .gff;
### As linhas 40 e 41 permitem escolher, através de Regex, qual parte da string retornar.

### Atualização 03/02/2023;
### Otimização das entradas e saídas de dados

# Variável de posição
n = 0

# Função salvar 
def salvar():
    planilha.to_excel(local_destino + "\output.xlsx")

# Importar GFF
def abrir():
    global gff
    root = tk.Tk()
    root.withdraw()

    gff = filedialog.askopenfilename(title = "Selecione seu arquivo GFF")
    
# Diretório de destino
def destino():
    global local_destino
    root = tk.Tk()
    root.withdraw()

    local_destino = filedialog.askdirectory(title = "Onde salvar?")

# Escolher arquivo GFF e onde salvar
abrir()
destino()

# Importações
local_planilha = os.path.dirname(__file__) + "\input.xlsx"
planilha = pd.read_excel(local_planilha, sheet_name="Sheet1", usecols = ["id", "value"])
examiner = GFFExaminer()

# Selecionar todos os genes
limite = dict(gff_type = ["gene"])
in_handle = open(gff)

print("Executando...")

# Printar todos os genes
for rec in GFF.parse(in_handle, limit_info = limite):

    tam_rec = len(rec.features) 
    ref = 0
    while ref < tam_rec:
        entradas = str(rec.features[ref])
        ref +=  1
        ID = re.search("(?<=id: )(?:.{1,})", entradas).group()
        try:
            Note = re.search("(?<=Note, Value: )(?:.{1,})", entradas).group()
        except:
            Note = "NA"

        # Escrever na planilha 
        planilha.at[n, "id"] = ID
        planilha.at[n, "value"] = Note[2:-2]
        n += 1

salvar()

in_handle.close()