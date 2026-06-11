#napisz program ktory sprawdzi czy liczba dzieli sie przez 2 i czy liczba wyniku dzielnia przez 5 daje reszte 1
print("---------------------------------")
print("program sprawdza czy liczba x dzieli sie przez 2 oraz czy liczba wyniku z dzielnia przez 5 dzaje 1")
print("---------------------------------")
x=int(input("podaj liczbe"))
if x%2==0:
    print("---------------------------------")
    print("tak, liczba jest podzielna przez 2")
    print("---------------------------------")
else:
    print("---------------------------------")
    print("nie, liczba nie jest podzielna przez 2")
    print("---------------------------------")
if x%5==1:
    print("tak, wynik z dzielnia liczby x przez 5 daje 1")
    print("---------------------------------")
else:
    print("nie wynik z dzielnia liczby x przez 5 nie daje 1")
    print("---------------------------------")
