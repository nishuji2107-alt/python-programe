basic_salary=1500
bonus_rate=200
commision_rate=0.02
sold=int(input("Enter the number of inputs solid: "))
price=float(input("Enter the total prices: "))
bonus=(bonus_rate * sold)
commission=(commision_rate * sold * price)
print("Bonus=%6.2f" % bonus)
print("Commision=%6.2f" % commission)
print("Gross salary=%6.2f" % (basic_salary + bonus + commission) )



