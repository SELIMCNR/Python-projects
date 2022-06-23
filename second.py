#python methods 
web="https://www.fenerbahce.org/"
course = " Selim ÇınaR "
result= web.lstrip()
result= web.rstrip()
result= web.strip()
result= course.lower()
result= course.upper()
result=course.title() 
result=web.count("e")
result=web.startswith("https")
result=web.endswith("org/")
result=web.find("www")
result=web.rfind("www")
result=web.index("fener")
result=course.isalpha()
result=course.isdigit()
result=course.center(50,"*")
result=course.ljust(50,"*")
result=course.rjust(50,"*")
result=web.replace("org", "net")
result=course.split(" ")
print(result[1])

web=input("Web adresi giriniz")
name= input("Ad: ")
surname= input("Soyad: ")
result1=web.count(".")


if (name):
    result=name.upper()
    print(result)
    if(surname):
       result=surname.lower()
       print(result)
       if(result1==2):
           result1=web.center(30,"*")
           print(result1)  


    




