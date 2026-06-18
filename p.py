#napisz program który wczyta podane liczby od użytkownika, i sumuje je do momentu otrzymania sumy przekraczającej 123, program zwraca suma oraz ilość składników
i=0
suma=0
while suma<=123:
    a=int(input("podaj liczbe"))
    i=i+1
    suma+=a
print("ilość skłądników: ", i)
print("suma: ", suma)
