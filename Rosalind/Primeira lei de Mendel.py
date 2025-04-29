k = int(input("Número de indivíduos da população K: "))
m = int(input("Número de indivíduos da população M: "))
n = int(input("Número de indivíduos da população N: "))

ind_totais = k + m + n

prob_NN = abs((n/ind_totais)*((n-1)/(ind_totais-1)))
prob_MN = abs((n/ind_totais)*(m/(ind_totais-1))*0.5)
prob_NM = abs((m/ind_totais)*(n/(ind_totais-1))*0.5)
prob_MM = abs((m/ind_totais)*((m-1)/(ind_totais-1))*0.25)

print("A probabilidade de pegar dois indivíduos aleatórios e o descendente possuir um alelo dominante é de: ", 
1-(prob_MM + prob_MN + prob_NM + prob_NN))