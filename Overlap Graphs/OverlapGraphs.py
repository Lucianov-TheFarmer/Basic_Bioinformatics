from Bio import SeqIO

# Importar FASTA
fasta = "input.fasta"
strings = list(SeqIO.parse(fasta, "fasta"))

# Definir K
k = 3

sequencias = {}

for string in strings:
 
    seq_inicial = string.seq[0:k]
    seq_final = string.seq[-k:]

    sequencias[string.id] = {"seq_inicial":seq_inicial, "seq_final":seq_final}

for key, value in sequencias.items():
    for key2, value2 in sequencias.items():
        if value["seq_final"] == value2["seq_inicial"] and key != key2:
            print(key, key2)