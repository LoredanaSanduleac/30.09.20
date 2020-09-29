"""
Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la
începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să
realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi
iepuri sunt în crescătorie? 
"""
ninceput=int(input("introduceti nr de iepuri la inceputul lunii: "))
nnascut=int(input("introduceti nr de iepuri care sau nascut: "))
nmurit=int(input("introduceti nr de iepuri care au murit: "))
nfinal=ninceput+nnascut-nmurit
print("la sfarsitul lunii erau",nfinal,"iepuri")