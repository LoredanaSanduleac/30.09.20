"""
Într-o gospodărie sunt 4 găini. Introduceţi în calculator prin variabilele a, b, c, d
numărul de ouă pe care-l dă fiecare găină într-o zi.
"""
a=int(input("introduceti nr de oua pe care le produce 1 gaina"))
b=int(input("introduceti nr de oua pe care le produce a 2 gaina"))
c=int(input("introduceti nr de oua pe care le produce a 3 gaina"))
d=int(input("introduceti nr de oua pe care le produce a 4 gaina"))
zi=a+b+c+d
saptamana=zi*7
print("pe saptamana gainile fac", saptamana, "oua")