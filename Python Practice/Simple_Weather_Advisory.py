temperature=int(input("Please enter the current temperature in Celsius:"))
#Below 0: "It's freezing! Wear warm layers."
#0-10: "It's very cold. Wear a heavy jacket."
#11-20: "It's cool. A light jacket would be good."
#21-30: "It's pleasant. Enjoy the weather!"
#Above 30: "It's hot. Stay hydrated!"
if temperature < 0 :
    print(f"Temperature is {temperature}°C.It's freezing! Wear warm layers.")
elif temperature >= 0 and temperature <= 10:
    print(f"Temperature is {temperature}°C.It's very cold. Wear a heavy jacket.")
elif temperature >= 11 and temperature <= 20:
    print(f"Temperature is {temperature}°C.It's cool. A light jacket would be good.")
elif temperature >= 21 and temperature <= 30:
    print(f"Temperature is {temperature}°C.It's pleasant. Enjoy the weather!")
elif temperature > 30 :
    print(f"Temperature is {temperature}°C.It's hot. Stay hydrated!")
else :
    print(f"Invalid temperature entered.Please enter valid temperature")