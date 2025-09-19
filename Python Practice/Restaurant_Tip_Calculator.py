bill_amount=float(input("Dear Customer.Thanks for your visit!Please enter the bill amount : "))
service_quality=input("Dear Customer Request you to enter Service Quality:").lower()
#Excellent: 20% tip
#Good: 15% tip
#Fair: 10% tip
#Poor: 5% tip

if service_quality == "excellent" :
    tip_amount=0.2*bill_amount
    print(f"Tip amount is ₹{tip_amount:.2f}")
elif service_quality == "good":
    tip_amount=0.15*bill_amount
    print(f"Tip amount is ₹{tip_amount:.2f}")
elif service_quality == "fair":
    tip_amount=0.1*bill_amount
    print(f"Tip amount is ₹{tip_amount:.2f}")
elif service_quality == "poor":
    tip_amount=0.05*bill_amount
    print(f"Tip amount is ₹{tip_amount:.2f}")
else :
    print(f"Dear Customer, Sorry but please enter valid Service Quality")