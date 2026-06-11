"""
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
"""
"""
#wersja 2
#napisz program ktory sprawdzi czy liczba dzieli sie przez 2 i czy liczba wyniku dzielnia przez 5 daje reszte 1
print("---------------------------------")
print("program sprawdza czy liczba x dzieli sie przez 2 oraz czy liczba wyniku z dzielnia przez 5 dzaje 1")
print("---------------------------------")
x=int(input("podaj liczbe"))
if x%2==0:
    print("---------------------------------")
    print("tak, liczba jest podzielna przez 2")
    print("---------------------------------")
elif x%5==:
    print("tak, wynik z dzielnia liczby x przez 5 daje 1")
    print("---------------------------------")
else:
    print("liczba nie spenia warunkow")
    print("---------------------------------")
"""
"""
#wersja 3
#napisz program ktory sprawdzi czy liczba dzieli sie przez 2 i czy liczba wyniku dzielnia przez 5 daje reszte 1
print("---------------------------------")
print("program sprawdza czy liczba x dzieli sie przez 2 oraz czy liczba wyniku z dzielnia przez 5 dzaje 1")
print("---------------------------------")
x=int(input("podaj liczbe"))
if x%2==0 and x%5==1:
    print("---------------------------------")
    print("tak, liczba jest podzielna przez 2")
    print("---------------------------------")
    print("tak, wynik z dzielnia liczby x przez 5 daje 1")
    print("---------------------------------")
else:
    print("liczba nie spenia obu warunkow")
    print("---------------------------------")
"""
"""
#wersja 4
#napisz program ktory sprawdzi czy liczba dzieli sie przez 2 i czy liczba wyniku dzielnia przez 5 daje reszte 1
print("---------------------------------")
print("program sprawdza czy liczba x dzieli sie przez 2 oraz czy liczba wyniku z dzielnia przez 5 dzaje 1")
print("---------------------------------")
x=int(input("podaj liczbe"))
if x%2==0 or x%5==1:
    print("---------------------------------")
    print("tak, liczba spelnia przynajmniej jeden z warunkow")
    print("---------------------------------")
else:
    print("liczba nie spenia ani jednego warunkow")
    print("---------------------------------")
"""
"""
#wersja 5
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
"""

#modulo nie dziala przy liczbach rzeczywistch trzeba uzyc liczby naturalne


#petla while
x=0
while x<10:
    print(x)
    x+=1
#instrukcja powtarzajca wywietlenie danej liczby

print()

#ptla for
for i in range(10): #[0,9] [0,10)
    print(i)

print()

for i in range(1,10): #[1,9] [1,10)
    print(i)

for i in range(1,11): #[1,10] [1,11)
    print(i)

print()
#co dwa
for i in range(1,11,2): #[1,10] [1,11)
    print(i)


#napisz program ktory obliczy sume kolejnych 5 liczb naturalnych
suma=0
for i in range(0,5):
    suma+=1
    print("suma= ",suma)

