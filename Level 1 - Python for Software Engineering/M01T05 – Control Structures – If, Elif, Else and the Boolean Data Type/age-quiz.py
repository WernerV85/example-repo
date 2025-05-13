age_user = int(input("What is your age? :"))

if age > 100:
    print("Sorry, your're dead!")
elif age <= 100 and age >= 65:
    print("Enjoy your retirement!")
elif age < 65 and age <= 40:
    print("You're over the hull!")
elif age == 21:
    print("Congrats on your 21st")
elif age < 13:
    print("You qualify for the Kiddie discount!")
else :
    print("Age is just a number!")