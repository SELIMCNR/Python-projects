"# -*- coding: utf-8 -*- "
#Yorum satırı oluşturan ifade tek satırlık
"""
Çoklu satırlı yorum 
"""
'''
Çoklu satırlı yorum
'''
print("Konu: Yorum satırlarını kullanma")
print(5+3) #bu yorum satırı toplama işlemi yapar
"""
##########################################
#***************************************##
#           Python Öğreniyorum          ##
#             Python 3                  ##
#***************************************##
##########################################
"""
sayi=5 #sayi değişkenine 5 sayısı atandı
print("Degişkenin içindeki sayı: ",sayi) #Değişken içinde sayi yazdırıldı
sayi1=10 #sayi1 değişkenine 10 sayısı atandı
print("Değişken içindeki sayı: ",sayi1) #Değişken içinde sayi yazdırıldı
metin="Selim" #Metin değişkenine Selim atandı
print("Değişken içindeki metin: ",metin) #Değişken içinde metin yazdırıldı 
sayi2=10.15 
print("Değişken içindeki sayı: ",sayi2)

a=b=c=1 #3değişkene 1 değer atandı
print("1.sayı= ",a)
print("2.sayı= ",b)
print("3.sayı= ",c)

adi,soyadi,yasi ="Selim","Çınar",45 #Değişik biçimde atama oluşturuldu
print("Adı=",adi)
print("Soyadı=",soyadi)
print("Yaşı=",yasi)

adi="Yusuf";soyadi="Çınar"; yasi = 24 #Noktalı virgüllü değişken atama
print("Adı=",adi)
print("Soyadı=",soyadi)
print("Yaşı=",yasi)

adi="Selim"
soyadi="Çınar"
dogumyili=2000
universiteMezunuMu=True       #camelCase değiken adlandırma
universiteyeBasladigiYil=2000
mezuniyetNotu=3.67
print("Adı: ",adi)
print("Soyadı:",soyadi)
print("Dogum tarih: ",dogumyili)
print("Unı mezun: ",universiteMezunuMu)
print("Unı basladıgı yıl: ",universiteyeBasladigiYil)
print("Mezunıyet notu: ",mezuniyetNotu)

sayi1 = 5 
sayi2 = "3" 
print(sayi1*sayi2) #Stringle sayı çarpıldında sayı kadar string yazılır
##################################################################
# Pythonda Veri tipleri  #########################################
#Sayısal int,float and complex

piSayisi = 3.14 #float veri
print("pi sayısı",piSayisi) 
rCm=2 #ınt veri
alan = 3.14*2**2
print("Alan=",alan)  #float tip sonuç
print("Yarıcapı 2cm olan dairenin alanı ",alan,"cm 2 dir")
karmasikSayi=4+5j
print("Bir karmaşık sayı = ", karmasikSayi+3j)

#################################################################
#KARAKTER DİZİSİ (string) Veri Tipi 
metin1 = "Merhaba"
metin2 = "Mars"
print(metin)                    #karakter direk yazıldı
print(metin1 *2)                #karakter dizisi 2 defa yazdık
print(metin1 + metin2)          #karakterler birleşti

##String Dilimleme İşlemleri
metin="Merhaba Mars"
print(metin[0]) #ilk karakteri yazdırır
print(metin[4:7])  #ifadenin 5,6 ve 7.karakterlerini yazar.
print(metin[8::])  #dokuzuncu karakterden sona kadar yazar
print(metin[-2])   #Karakter dizisinin sondan ikinci karakterini yazar
print(metin[:7])   #indisi 0'dan 7'e kadar yazar (7 dahil değil)
print(metin[0:8:2]) #0,2,4 ve 6 indis numaralı karakterleri dilimler

 #type() Metodu Kullanımı tipi ne int,float
sayi1 = 5 
sayi2 = 10.556
metin1 ="1"
sayi3 = 4+5j
askerlikYaptiMi=True
print("1. değişkenin veri tipi: ",type(sayi1))
print("2. değişkenin veri tipi: ",type(sayi2))
print("3. değişkenin veri tipi: ",type(metin1))
print("4. değişkenin veri tipi: ",type(sayi3))
print("5. değişkenin veri tipi: ",type(askerlikYaptiMi))
listem=["Çınar",24,"Mühendis",True]
print("6. değişkenin veri tipi: ",type(listem))
demet1=("Çınar",24,"Mühendis",True)
print("7.değişkenin veri tipi : ",type(demet1))
sozluk={"adi": "Çınar","Yasi": 22,"Meslekunvani":"Mühendis","Askerlikdurumu":True}
print("8.değişkenin veri tipi : ",type(sozluk))

####Veri Tiplerini Dönüştürmerk int(metin1) vs#########

metin1 = "5"
metin2 = "3"
print(metin1 + metin2)
print(int(metin1)+int(metin2))

piDegeri = 3.14 
print("Veri Tipi: ",type(piDegeri))
yaricap = 5 
daireninAlani =((piDegeri*2)*yaricap)
print("Dairenin Alanı (float)=",daireninAlani)
piDegeriInt =(int(piDegeri))  #float veri inte dönüştü
print("Int veri tipine dönüştürülen piDegeri: ",piDegeriInt)
daireninAlani=((piDegeriInt*2)*yaricap)
print("Dairenin Alanı (int)=",daireninAlani)

askerlikYaptiMi=True 
print("Askerlik yaptı mı?",askerlikYaptiMi)
askerlikYaptiMiInt=int(askerlikYaptiMi) #integer tipine dönüştürüldü
print("Askerlik yaptı mı?",askerlikYaptiMiInt)
askerlikYaptiMiStr = str(askerlikYaptiMi) #string tipine dönüştürüldü
print("Askerlik yaptı mı?",askerlikYaptiMiStr)


########Operatörler ##########


###toplama operatörü####
print(5+3)
print(5+3+3)
sayi=10
print(sayi +5)
sayi2=10.34
print(sayi + sayi2+5.5) #farklı veri tiplerindeki sayıları ve değişkenlerş kullanabiliriz

print("Merhaba" + "Mars")
metin1 = "Merhaba " + "Mars " + "Nasılsın ?"
print(metin1)

##Çıkarma operatörü#####
print(5-3)
sayi1=5
sayi2=3
print(sayi1-sayi2)
print(3-4-5)


##Çarpma Operatörü 
print(5*3)
print(5*3*2)
sayi1=5
sayi2=3
print(sayi1+sayi2)

print(20*"Münire")

##Bölme Operatörü
print(5/3)
print(18/3/2)

##Kuvvet Alma Operatörü
uslusayı = 6**4 #uslu sayı alma
print(5**3)
print(4**3)
print(49**(1/2))

#Tam bolum operatörü 
print(121.00//3)

#Mod alma operatörü 
print(5%3) # sayının 3 ' e bölümden kalan
print(9%2)

#####İlişkisel Operatörler
print(5==3)
sayi1=5
sayi2=3
print(sayi1==sayi2)
print(sayi1==5)

print("Selim"=="Selim")
#Küçük büyük harf duyarlılığı (case sensetive) dikkat et.
metin1="Selim"
metin2="SELİM"
print(metin1==metin2)
print(metin1=="SELİM")

#Eşit değildir Operatörü 
print(5!=3)
sayi1=5
sayi2=3
print(sayi1!=sayi2)
print(sayi1!=5)
#Cıktılar == operatörünün tersi 

print("Selim"!="selim")
metin1="Selim"
metin2="SELİM"
print(metin1!= metin2)
print(metin1!= "SELİM")

#Büyüktür Operatörü 
sayi1 = 7.04
sayi2 = 7.07
print(sayi1>sayi2)
sayi1=8.06
print(sayi1>sayi2)

#Küçüktür Operatörü 
sayi1=70.4 
sayi2=70.5
print(sayi1<sayi2)

sayi2=6
print(sayi1<sayi2)
sayi2=6.06
print(sayi1<sayi2)
print("z">"a")
print("a"<"z")

#büyükeşittir(>=) ve küçükeşittir(<=) operatörleri
sayi1 =6.06
sayi2=6.06
print(sayi1>=sayi2)
print(sayi1<=sayi2)
#Sayılar birbirine eşit olduğu için iki operatör de True değeri döndürür.
sayi2=6.07
print(sayi1>=sayi2)
print(sayi1<=sayi2)
sayi2=6.05
print(sayi1>= sayi2)
print(sayi1<=sayi2)
#sayi2 değişkeni 6.05 olduğu ve sayi1 sayi2 den büyük olacağı için sadece >= operatörü True değeri döndürür.
 
##is ve isnot          içeriyormu?
sayi1 = 5 
print(sayi1 is 5 )
print(sayi1 is not 5) # is operatörünün tersini verir

## in ve not in operatörleri 
#in operatörü 
print("Bil" in "Bilişim")
#2.karakter dizisi içinde 1.karakter dizisi var mı ? 
print("Bil" not in "Bilişim")
#in operatörünün tersi sonuç verir.



#Atama Operatörleri

##Artırarak Atama Operatörü 
sayi1=5 
sayi1+=3
print(sayi1)
metin1="Merhaba"
metin1+="Mars"
print(metin1)


##Eksilterek azaltma operatörü
sayi1=5
sayi1-=5
print(sayi1)

#Çarparak Atama Operatörü
sayi1=5
sayi1*=5
print(sayi1)
#Aynı şekilde karakter dizilerinde de kullanabilirsiniz
metin1="Merhaba"
metin1*=3 #metin1= metin1*3 koduyla aynı işlevi görür
print(metin1)

#Bölerek Atama Operatörü 

sayi1=5
sayi1/=3
print(sayi1)

#kuvvet alarak atama operatörü
sayi1 = 5 
sayi1 **=3
print(sayi1)

#Tam sayı bölerek atama operatörü 
sayi1=15 
sayi1//=3
print(sayi1)

#Mod Alarak Atama Operatörü 
sayi1=5 
sayi1%=3
print(sayi1)


#Mantıksal Operatörler 

#Or Operatörü Veya Operatörü 
sayi1=5
print(sayi1<6 or sayi1>10)
adi="Selim"
print(adi=="Selim" or adi=="Çınar") #adi selim veya çınar ise true değeri döndürür
Meslekunvani="Mühendis"
print(Meslekunvani=="Öğretmen" or Meslekunvani=="Doktor")
#Meslek Ünvanı Öğretmen veya Doktor veya Mühendis'ten biri ise True değerini döndürür.
# İkiden fazla koşul için de kullanılabilir


#and opearatörü ve 
ogrenciDersPuani = 50 
print(ogrenciDersPuani>50 and ogrenciDersPuani<60)
adi="Selim"
yasi=22
print(adi=="Selim" and yasi>=20)
#Adı Emre ve yaşı en az 20 ise True değerini döndürür.
meslekUnvani='Mühendis'
askerlikDurumu='Yaptı'
isTecrubeYil=2
print (meslekUnvani=='Mühendis' and askerlikDurumu=='Yaptı')
print (meslekUnvani=='Mühendis' and askerlikDurumu=='Yaptı' and isTecrubeYil>=3)

###Not operatörü
ogrenciDersPuani=50
print(not(ogrenciDersPuani<45))
print (ogrenciDersPuani>45) #Yukarıdaki ifade ile aynı işlevi görür

#Operatörlerde öncelik sırası 

print((3+5)*2) #16 
print(3+5*2)   #13
print(3**2*2)  #18
print(6*7/7)   #6
print(6*3/2+8/2*3) #21.0
sehir='Ankara'
sehir='İstanbul'
print (sehir!='istanbul') #operatöre dikkat
#Büyük harf küçük harf duyarlılığına dikkat
print (sehir=='İstanbul')

###Bölüm Sonu Örnekler 
#1
sayi1=8*5/2
print(sayi1>20)
#2 
vizePuani=80
finalPuani=70
sonuc=(0.4*vizePuani)+(finalPuani*0.6)
print(sonuc)
#3
#yanlış değişken tanımlama 1sinavpuani=100
sinavPuani=90
_sinav_puani1=90
SınavPuanı=70

#4
plaka="06"
print(type(plaka))

#5 
#sehir="Ankara"
sehir = "İstanbul"
print("Şehir: ",sehir)
#6
sehir="Ankara"
sehir = "İstanbul"
print(sehir!="İstanbul")
print(sehir=="İstanbul")
#7
adsoyad="Selim Çınar"
devamsızlıksüresi=24
mesaj=f"Sn {adsoyad} öğrencinizin toplam devamsızlığı {devamsızlıksüresi} gündür.Python Listesi"
print(mesaj)
#8
hitapşekli="Sn"
abonenumarası=5484868468
tüketimdönemi=2020
tüketimtutarı=3500
mesaj=f"{hitapşekli} {abonenumarası} nolu abonemiz {tüketimdönemi} dönemi faturanız {tüketimtutarı} Tl'dir.Python Belediyesi"
print(mesaj)

###################################################################
###                     Pythonda Temel Fonksiyonlar            ####
##Temel Fonksiyonlar
#Print fonksiyonu
print("değer") #Print fonksiyonun Çift tırnakla veya
print('değer')#tek tırnakla ve 
print("""değer""")#Üç tırnakla yazımı mevcuttur
print(1907)# print içersinde değere argüman denir 1907 argümandır
print("Türkiyen 'nin en kalabalık ili İstanbul 'dur ") #karakter dizilerinde çift tırnak, tek tırnak ya da üç çift tırnak kullanılabilir.
print(2+2) #argümanlar arasında toplama işlemi yapılabilir.

