n = int(input("Quantos meses se passarão? ")) 
k = int(input("Quantos pares são gerados por cada cruzamento? "))

a = 0 # 2 antes
b = 1 # 1 antes
c = 1 # atual

n -= 1 # Ignorar primeiro mês

while n > 0:

    print("Mês: ", n, "\n2 antes: ", a) # Printar mês e 2 antes
    
    b = c  # 1 antes, se torna o atual

    print("1 antes: ", b) # printar um antes

    c = int(a*k) + int(b) # atualizar atual e multiplicar 2 antes pela quantidade de crias; Verificar diagrama para maiores explicações
    
    print("atual: ", c,"\n") # printar atual
    
    a = b  # 2 antes se torna 1 antes
    
    n -= 1

    