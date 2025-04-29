import requests

with open("input.txt", "r") as f:
    data = f.read().split("\n")

for cod in data:
    cod_original = cod
    cod = cod.split("_")[0]
    url = "https://www.uniprot.org/uniprot/" + cod + ".fasta"
    r = requests.get(url)

    seq_atual = ""

    for _ in r.text.split("\n")[1:]:
        seq_atual += _

    posicoes = []

    for i in range(len(seq_atual) - 3):
        if seq_atual[i] == "N":
            if seq_atual[i+1] != "P":
                if seq_atual[i+2] == "S" or seq_atual[i+2] == "T":
                    if seq_atual[i+3] != "P":
                        posicoes.append(i+1)

    if posicoes != []:
        print(cod_original)
        print(*posicoes)

    