"""
Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
aceste cifre luate o singură dată.
"""
n=int(input("introduceti 1 nr"))
m=int(input("introduceti 2 nr"))
l=int(input("introduceti 3 nr"))
print(str(n)+str(m)+str(l), str(m)+str(n)+str(l), str(l)+str(n)+str(m), str(m)+str(l)+str(n), str(n)+str(l)+str(m), sep=" ")