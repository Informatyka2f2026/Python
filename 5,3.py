#napisz program który bedzie gra w zgadywanie ustalonej liczby z przedziału od 0 do 100 program powinien działać do monmentu podanie przez użytko właściwej liczby po każdej próbie odgadnięcia liczby program powinen wypisać jeden z komunikatów za mała za duża brawo udało ci sie za x razem gdzie x oznacza liczbę pób które wykonał użytkownik
import random
C=random.randint(0,100)
i=1
a=int(input("podaj liczbe"))
while a!=C:
    i+=1
    if a>C:
        print("za duża")
    if a<C:
        print("za mała")
    a = int(input("próbuj dalej"))
if a==C:
    print("Brawo!!")
    print("udało ci sie za: ", i, 
