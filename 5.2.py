C=57
i=1
a=int(input("podaj liczbe"))
while a!=57:
    i+=1
    if a>C:
        print("za duża")
    if a<C:
        print("za mała")
    a = int(input("próbuj dalej"))
if a==57:
    print("Brawo!!")
    print("udało ci sie za: ", i, "próbą")
