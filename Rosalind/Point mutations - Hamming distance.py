string1 = input("Primeira string: ")
string2 = input("Segunda string: ")

n = 0 

for a, b in enumerate(string1):
    
    if b != string2[a]:
        n += 1

print(n)
