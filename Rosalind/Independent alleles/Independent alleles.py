from scipy.stats import binom

with open("input.txt", "r") as f:
    dados = f.read()

k = int(dados.split(" ")[0])
n = int(dados.split(" ")[1])

# The probability of an individual having the AaBb genotype
p = 0.25

# The total number of individuals in generation k
total_individuals = 2**k

# Calculate the probability of having at least n individuals with the AaBb genotype
prob = sum(binom.pmf(range(n, total_individuals+1), total_individuals, p))

print(round(prob, 3))