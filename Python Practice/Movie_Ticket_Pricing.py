customer_age=int(input("Please enter the age of customer:"))
#Child (0-12): ₹100
#Teen (13-17): ₹150
#Adult (18-59): ₹200
#Senior (60+): ₹120
if customer_age >= 0 and customer_age<=12:
    print(f"Customer is Child and his ticket price is ₹100")
elif customer_age >= 13 and customer_age <= 17:
    print(f"Customer is Teen and his ticket price is ₹150")
elif customer_age >= 18 and customer_age <= 59:
    print(f"Customer is Adult and his ticket price is ₹200")
elif customer_age >=60 :
    print(f"Customer is Senior and his ticket price is ₹120")
else :
    print(f"Please enter valid age of customer")