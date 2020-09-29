"""
Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile trebuie să găsească
cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion. 
"""
n=int(input("introduceti un nr"))
print(n-2, n-1, n, n+1, n+2, sep=" ")