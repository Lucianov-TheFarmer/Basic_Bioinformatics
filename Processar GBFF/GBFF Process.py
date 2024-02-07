from Bio import SeqIO
import tkinter as tk
from tkinter import filedialog
import re

# Importar GBFFs
def abrir():
    global gbff_file
    root = tk.Tk()
    root.withdraw()

    gbff_file = list(filedialog.askopenfilenames(title = "Selecione seu(s) GBFF: "))

# Diretório de destino
def destino():
    global local_destino
    root = tk.Tk()
    root.withdraw()

    local_destino = filedialog.askdirectory(title = "Onde salvar?")

abrir()    
destino()

output_nuc = open(local_destino + "\_Nucleotídeos.txt", "w")
output_anot = open(local_destino + "\_Anotação.txt", "w")

# Percorrer os diferentes GBFFs
for gbff in gbff_file:

    #print("\nPara o GBFF: ", gbff)
    output_nuc.write("------------------")
    output_nuc.write("\n\nPara o GBFF: " + gbff + "\n\n")
    output_anot.write("------------------")
    output_anot.write("\n\nPara o GBFF: " + gbff + "\n\n")

    # Fazer um dicionário com todos os genes do GBFF
    genes = {}

    # Inserir genes no dicionário
    for seq_record in SeqIO.parse(gbff, "genbank"):
        genes[seq_record.id] = seq_record
        
    # Escolher o(s) gene(s)
    gene_alvo = {}

    i = input("\nInsira o gene (quando terminar, aperte enter): ")
    while i != "":
        gene_alvo[i] = ([s for s in i.split()])
        i = input("Insira o gene: ")
    gene_alvo[i] = ([s for s in i.split()])
    del gene_alvo[""]

    # Loop com todos os genes escolhidos
    for n in gene_alvo:

        sequencia = genes[n].seq

        output_nuc.write("------------------\n\n")
        output_nuc.write("Para o gene: " + n)
        output_anot.write("------------------\n\n")
        output_anot.write("Anotação do gene: " + n + "\n")

        output_nuc.write("\n\nSequencia de nucleotideos: " + str(sequencia))
        output_nuc.write("\n\nSequencia de aminoácidos: " + str(sequencia.translate()) + "\n")        

        # Criar uma lista com os CDS, que possuem sequência
        gene_interno = []

        # Variável de posição: gene_interno
        z = 0 

        # Inserir genes com CDS
        for feature in genes[n].features:
            gene_interno.insert(z, str(feature).__contains__("CDS"))
            z += 1
        
        # Recuperar índice dos CDS dentro da lista de features do gene
        indices = []
        item_para_achar = True
        def calc_index(gene_interno, item_para_achar):
            for idx, value in enumerate(gene_interno):
                if value == True:
                    indices.append(idx)
            return indices
        calc_index(gene_interno, item_para_achar)

        # Recuperar informações de todos os CDS
        for z in indices:
            seq = re.search("translation, Value: (?:.*)'", str(genes[n].features[z])).group()
            produto = re.search("product, Value: (?:.*)'", str(genes[n].features[z])).group()

            output_anot.write("\nProduto: " + produto[18:-1])
            output_anot.write("\nSequencia: " + str(seq[22:-1]) + "\n")
        output_anot.write("\n")
        output_nuc.write("\n")
    output_anot.write("\n")
    output_nuc.write("\n")
                       
print("Concluído")



            







