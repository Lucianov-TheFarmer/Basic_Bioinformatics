with open("input.txt", "r") as f:
    protein = f.read().strip()

different_RNA_strings = 1

number_of_codons = {"F": 2, "L": 6, "S": 6, "Y": 2, "C": 2, "W": 1, "P": 4, "H": 2, "Q": 2, "R": 6, "I": 3, "M": 1, "T": 4, "N": 2, "K": 2, "V": 4, "A": 4, "D": 2, "E": 2, "G": 4, "stop": 3}

for aa in protein:
    for codon in number_of_codons:
        if aa == codon:
            different_RNA_strings *= number_of_codons[codon] 

different_RNA_strings *= number_of_codons["stop"]
print(different_RNA_strings % 1000000)
