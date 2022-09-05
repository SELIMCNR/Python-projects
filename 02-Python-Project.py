from itertools import count
from unicodedata import name


Name, Surname, No, isStudent = ("Selim", "Çınar", 630, True)

if (Name == Name.lower()):
    print("Harflerin hepsi küçüktür.")
elif (Name == Name.upper()):
    print("Harflerin hepsi büyüktür.")
elif (1 == Name.count("e")):
    if Name == "Selim":
        Name = Name.replace("", "-", 20)
        print(f"{Name} 'de 1 e harfi vardır")

elif (Name == Name.startswith("Se")):
    print(f"{Name} değişkeni 'Se' ile başlıyor")
elif (Name == Name.endswith("im")):
    print(f"{name} değişkeni im ile bitiyor ")

for i in range(0, 4):

    if i == 0:
        Name = Name.center(50, "*")
        print(f"Öğrenci adı : {Name}")
    elif i == 1:
        Surname = Surname.center(50, "*")
        print(f"Öğrenci Soyadı : {Surname}")
    elif i == 2:
        print(f"Öğrenci numarası : {No}")
    elif i == 3:
        print(f"Öğrenci bilgisi doğrumu : {isStudent}")
