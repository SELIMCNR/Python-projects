#kullanıcıdan 3 sayi al en büyüğünü bul 
a=int(input("SAYİ 1 : "))
b=int(input("SAYİ 2 : "))
c=int(input("SAYİ 3 : "))

if (a >b and a>c):
    print(f"En buyuk sayi {a}")
elif(b>a and b>c):
    print(f"En buyuk sayi {b}")
elif(c>a and c>b):
    print(f"En buyuk sayi {c}")
else : 
    print("işlem hatasi")    
