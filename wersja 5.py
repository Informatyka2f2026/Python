#napisz program ktory sprawdzi czy liczba dzieli sie przez 2 i czy liczba wyniku dzielnia przez 5 daje reszte 1
print("---------------------------------")
print("program sprawdza czy liczba x dzieli sie przez 2 oraz czy liczba wyniku z dzielnia przez 5 dzaje 1")
print("---------------------------------")
x=float(input("podaj liczbe"))
if x%2==0 or x%5==1:
    print("---------------------------------")
    print("tak, liczba spelnia przynajmniej jeden z warunkow")
    print("---------------------------------")
else:
    print("liczba nie spenia ani jednego warunkow")
    print("---------------------------------")
