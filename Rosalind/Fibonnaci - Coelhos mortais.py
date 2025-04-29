n = int(input("Quantos meses se passarão? "))
m = int(input("Quantos meses os coelhos são capazes de sobreviver? "))

coelhos = [1, 1]                                                               
mes_atual = 2                                                                     
while mes_atual < n:                                                              
    if mes_atual < m:                                                             
        coelhos.append(coelhos[-2] + coelhos[-1])                              
    elif mes_atual == m:                                        
        coelhos.append(coelhos[-2] + coelhos[-1] - 1)                          
    else:                                                                      
        coelhos.append(coelhos[-2] + coelhos[-1] - coelhos[-(m + 1)])                                                           
    mes_atual += 1                                                                
print(coelhos[-1])            

