#napisz program który wczyta podane liczby od użytkownika, i sumuje je do momentu otrzymania sumy przekraczającej 123, program zwraca suma oraz ilość składników
i=0
suma=0
while suma<=123:
    a=int(input("podaj liczbe"))
    i=i+1
    suma+=a
print("ilość skłądników: ", i)
print("suma: ", suma)

#napisz program ktory obliczy sume kolejnych 5 liczb naturalnych
suma=0
for i in range(0,5):
    suma+=1
    print("suma= ",suma)

while i<6:
    suma+=1

'''
print("wprowadz liczbe")
#for i in range(0,5): #[0-4] (0-5)
s=0
maks=-1000000
for i in range(5):
        a=float(input("podaj liczby: "))
        s=s+a
        if a>maks:
            maks=a
print("suma:", round(s,1))
print("maks:", round(maks,1))
#round zaokrągla standardowo 1-4 w dół 5-9 w góre
# round(to co zaokrąglić, do ilu miejsc po przecinku)
'''
"""
print()
#co dwa
for i in range(1,11,2): #[1,3,5,7,9]
    print(i)
#range jest przedziałem otwartm czyli liczba do już nie wchodzi
print()
#co dwa
for i in range(2,22,2): #[2,4,6,8,10,12,14,16,18,20]
    print(i, end="  ")
"""

#napisz program który zliczy osobno ile liczb ujemnych wprowadzono z klawiatury spośród podanych liczb. czytanie liczby 0 końćzy podawanie liczb
i=0
a=int(input("podaj liczbe"))
while a!=0:
    a = int(input("podaj kolejną liczbe"))
    if a<0:
        i=i+1
print("ilość liczb ujemnych:", i)


