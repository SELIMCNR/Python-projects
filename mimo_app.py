is_day=False
lights_on= not is_day

print("Daytime?")
print(is_day)

print("Lights on ?")
print(lights_on)

#track sales data
stock=600 
jeans_old = 500
target = 500
target_hit = jeans_old = target 
print("Hit jeans sale target : ")
print(target_hit)

current_stock= stock - jeans_old 
in_stock = current_stock !=0
print("Jeans in stock: ")
print(in_stock)

#heart rate 
heart_rate = 77 

too_low= heart_rate <60 
too_high= heart_rate>100

print("Heart rate low:")
print(too_low)

print("Heart rate high: ")
print(too_high)

#frequency
frequency = "once a week"
intensity = "low"

highly_active = frequency == "daily"
print("Highly active user: ")
print(highly_active)

highly_intensity=intensity=="high"
print("High intensity sports: ")
print(highly_intensity)

#double lare qalqulatery
ride_type= "Black"
credits = 4 

ride_price =0
final_price=0

if ride_type =="DooberX":
    ride_price=20.5
elif ride_type=="Black":
    ride_price= 37.9
else:
    ride_price = 18.7 
print(f"Ride price{ride_price}")

if credits > 0 :
    final_price = ride_price - credits

print(f"Final price:{final_price} ")
#calculater
account = 100 
interest_rate = 0.004
years =3 
print(f"Initial amount: {account}")
counter = 1 
while counter <= years :
    accrued_interest = account * interest_rate 
    account += accrued_interest 
    print(f"year {counter}:{account}")
    counter +=1

#new product rating 
flavors = ["cinammon","pumpkin","apple pie"] 
print(f"New flawors: {flavors}")

ratings = [4,2.5,3]
print(f"Consumer rating: {ratings}")
print(ratings)

passed = [True,False,True]
print("Release: ")
print(passed)

#Stocks
apple_stocks=[298.18,304.14,289.23]
apple_stocks[0]=310
print("latest value")
print(apple_stocks[0])

apple_stocks[1]=310
print("highest value:")
print(apple_stocks[1])

print("lowest values: ")
print(apple_stocks[2])

#humidity
humidity_level = [87,83,89,88,87]
humidity_level.insert(0,90)
humidity_level.pop()
print(humidity_level)











