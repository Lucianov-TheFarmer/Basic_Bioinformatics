with open("input.txt", "r") as arquivo:
    dados = arquivo.readlines()

AAAA = int(dados[0].split(" ")[0])*2
AAAa = int(dados[0].split(" ")[1])*2
AAaa = int(dados[0].split(" ")[2])*2
AaAa = int(dados[0].split(" ")[3])*0.75*2
Aaaa = int(dados[0].split(" ")[4])*0.5*2
aaaa = int(dados[0].split(" ")[5])*0*2

print("AA-AA", AAAA)
print("AA-Aa", AAAa)
print("AA-aa", AAaa)
print("Aa-Aa", AaAa)
print("Aa-aa", Aaaa)
print("aa-aa", aaaa)

print("Filhos com fenótipo dominante: ", AAAA+AAAa+AAaa+AaAa+Aaaa)