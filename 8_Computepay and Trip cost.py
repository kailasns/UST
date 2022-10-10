#Write a pay computation program with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).


def computepay(hours,rate):
    pay =('Your pay this month: ' + str((hours + hours/2) * rate)) 
    print(pay)


#program for trip cost 
a = []
def hotel_cost(night):
    cost = 140
    totalcost = 140*night
    print("Amount to be paid:",totalcost)  
def plane_ride_cost(city):
    dict = {"Charlotte": 183,
   "Tampa": 220,
   "Pittsburgh": 222,
   "Los Angeles": 475}
    print("plane ride cost for" ,city, "is:" ,dict[city])    
def rental_car_cost(days):
    carcost = 40
    amount = carcost*days
    a.append(amount)
    if days >= 7:
     amount = amount - 50
     print("Amount to be paid with discount of 50 dollars:",amount)
    elif days >= 3:
        amount = amount - 20
        print("Amount to be paid with discount of 20 dollars:",amount)
    else:
        print("Amount to be paid:",amount)
def trip_cost(city,days,spending_money):   
    cost2 = 140
    totalcost2 = 140*days
    a.append(totalcost2)
    dict = {"Charlotte": 183,
   "Tampa": 220,
   "Pittsburgh": 222,
   "Los Angeles": 475}
    a.append(dict[city])
    carcost2 = 40
    amount2 = carcost2*days
    if days >= 7:
     amount2 = amount2 - 50
    elif days >= 3:
        amount2 = amount2 - 20
    else:
        print(":)")
    a.append(amount2)
    a.append(spending_money)
    print("spending money INR:",spending_money," added")
    print("Sum of all amounts :",sum(a))
    
