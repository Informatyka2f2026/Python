#napisz program który bedzie gra w zgadywanie ustalonej liczby z przedziału od 0 do 100 program powinien działać do monmentu podanie przez użytko właściwej liczby po każdej próbie odgadnięcia liczby program powinen wypisać jeden z komunikatów za mała za duża brawo udało ci sie za x razem gdzie x oznacza liczbę pób które wykonał użytkownik
C=57

a=int(input("podaj liczbe"))
while a!=57:
    if a>C:
        print("za duża")
    if a<C:
        print("za mała")
    a = int(input("próbuj dalej"))
if a==57:
    print("Brawo!!")
