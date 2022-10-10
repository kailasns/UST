


num = int(input("Enter days: "))
year = num // 365
month = (num-year*365)//30
days = (num-year*365-month*30)
print("Year",year, "month",month,"days",days)
