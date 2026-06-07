units=int(input("Enter number of units consumed : "))
if(units>500):
    amount=units * 9.25
    surcharge=80
elif(units>=300):
    amount=units * 7.75
    surcharge=70
elif(units>=200):
    amount=units * 5.25
    surcharge=50
elif(units>=100):
    amount=units *3.75
    surcharge=30
else:
    amount=units * 2.25
    surcharge=20
billtotal=amount + surcharge
print("Electricity bill=%.2f"  %billtotal)
