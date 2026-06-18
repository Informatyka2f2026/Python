#napisz program który zliczy osobno ile liczb ujemnych wprowadzono z klawiatury spośród podanych liczb. czytanie liczby 0 końćzy podawanie liczb
i=0
a=int(input("podaj liczbe"))
while a!=0:
    a = int(input("podaj kolejną liczbe"))
    if a<0:
        i+=1
print("ilość liczb ujemnych:", i)
