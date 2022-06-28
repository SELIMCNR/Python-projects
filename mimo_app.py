
"""

sayi=2565849
sayiondalık=25.6546
complex=4+5j
metin="selim"

LISTE1=["LSIT1","LIST2","LIST3","LIST4"]

DEMET=("TUPLE1","TUPLE2","TUPLE3","TUPLE4","TUPLE5")

SOZLUK={"DİCTİONARY": "DİCT","DİCTİONARY":"DİCT2","DİCTİONARY":"DİCT3"}

sayi=25
METİN="8"
print(METİN[::1])
print(type(sayi))
METİN=int(METİN)
sayi=str(sayi)
print(type(sayi))
print(METİN*2)
print(5**3)
print(4//3)
print(5%4)
#== != > < >= <= is is not in not in 
# 4*=3 4+=3 or veya and ve 

vizePuani=80
finalPunai=70
sonuc=(0.4*vizePuani)+(finalPunai*0.6)
print(sonuc>=60)
plaka="06"
print(type(plaka))
#sehir="Ankara"
sehir="İstanbul"
print(sehir)
sehir="Ankara"
sehir="İstanbul"
print(sehir!="istanbul")

ad,soyad="Mehmet","Çınar"
devamsızlıksüresi=45
mesaj=f"Sn{ad}{soyad} öğrencinizin toplam devamsızlığı {devamsızlıksüresi} gündür."
print(mesaj)

hitapşekli="Sayın"
abonenumarası=4848798
tüketimdönemi=2020
tüketimtutarı=4500
mesaj=f"{hitapşekli} {abonenumarası} nolu abonemiz {tüketimdönemi} dönemi faturanız {tüketimtutarı} Tl dir.Python Belediyesi"
print(mesaj)
print("Kahramanmaraş'ın dondurması meşhurdur.")
print("Kahramanmaraş madalya \"lı tek şehirdir")
print("1.satır\n 2.satır\n 3.satır")
print("Pazartesi \t salı \t çarşamba") 
print("Merhaba !",end=" ")
print("Python")

print("Merhaba!",end=",")
print("Python")

print("pazartesi","salı","çarşamba","perşembe","cuma",sep="-")
print("pazartesi","salı","çarşamba","perşembe","cuma",sep="-fenerbahçe-")

a,b,c=5,6,9
print("girdiğiniz",a,b,"ve",c,"değerlerinin toplamı: ",a+b+c,"dir")
print("çıktı işlemi {} {} {}".format(1,2,3))
a,b,c=5,6,9
print("girdiğiniz {},{} ve {} değerlerinin toplamı= {} dir".format(a,b,c,a+b+c))
print("{1}{0}{2}".format(10,"Python",20))

print("Memleket isterim,\n Gök mavi,dal yeşil,tarla sarı olsun,")
print("Memleket isterim,","Gök mavi,dal yeşil,tarla sarı olsun,")

print("Memleket isterim,")
print("Gök mavi,dal yeşil","tarla sarı olsun")

print("Memleket","isterim","Gök mavi","dal","yeşil",sep="fenerbahçe")

print("   *")
print("  * * ")
print(" *   *")
print("*      *")
print("***     ***")
print("  *     *")
print("  *     *")
print("  *******")
not1 = 55 
not2 = 100 
print("1.Sınav Notu:{} \n2.sınav Notu:{}".format(not1,not2))

isim = input("isminizi giriniz: ")
print("merhaba! ",isim)

sayi=int(input("sayi gir"))
if(sayi>0):
         print("Sayi pozitif")
elif(sayi<0):
    print("sayi negatif")
else:
    print("sayı 0")
"""
"""
sınav1=int(input("sınav1"))
sınav2=int(input("sınav2"))
ortalama=sınav1+sınav2/2
if(ortalama>50):
    print("geçti")
elif(ortalama<50):
    print("kaldı")
"""
"""
sayi=int(input("sayi1:"))
sayi2=int(input("sayi2:"))
if(sayi>sayi2):
     print("sayi1 büyüktür")
elif(sayi2>sayi):
     print("sayi2 büyüktür")
else:
     print("eşittir")
"""
"""
harfler=["a","e","i","o","i","u"]
print(harfler.count("i"))
print(harfler.count("p"))

liste1,liste2,liste3,liste4=["a"],["b"],["c"],["d"]
print(liste1)
print(liste2)

liste1,liste2=["a"],["b"]
liste3=liste1+liste2
print(liste3)
"""
"""
liste=[34,1,56,334,23,2,3,19]
liste=liste.reverse()
liste=liste.sort()
print(liste)
"""
"""
listem=["Merhaba","Türkiye","Nasılsın","Tebrikler"]
print(listem[-1])
print(listem[-3])
print(listem[-4])

liste=[1,2,3,4,5,6,7]
print(liste[1:4])
print(liste[0:4])
print(liste[3:])
print(liste[0:])

isimler=["ali","veli","ayşe"]
soyisimler=["türk","izci","erel"]
ad_soy1=isimler[0]+" "+soyisimler[0]
ad_soy2=isimler[1]+" "+soyisimler[1]
ad_soy3=isimler[2]+" "+soyisimler[2]
print(ad_soy1)
print(ad_soy2)
print(ad_soy3)

liste=["bir","iki","dört"]
liste.insert(2,"üç")
liste.insert(4,"beş")

liste=["birinci veri","ikinci veri","üçüncü veri", "dördüncü veri","beşinci veri"]
print(liste[0])
print(liste[4])
"""
                     
"""
a=int(input("ağacın yükseklliği"))
b=a
for i in range(1,a+1):
    print(b*" ",(2*i-1)*"*")
    b-=1
"""
"""
liste=[5,9,7,1,2,3,6,4]
buyuk=0
kucuk=999
for i in range(len(liste)):
    if liste [i]> buyuk:
        buyuk=liste[i]
    if liste[i]<kucuk:
        kucuk=liste[i]
print(f"girilensayıların en buyugu = {buyuk} en kucugu {kucuk}")        
"""
"""
import turtle
yıldız = turtle.Turtle()
for i in range(5):
 yıldız.forward(100)
 yıldız.right(144)
turtle.done()
"""
import time
for i in range(1,21):
    time.sleep(0.5)
    print(i)











