age_user = int(input("What is your age? :"))

if age_user > 100:
    print("Sorry, your're dead!")
elif age_user >= 65 and age_user <= 100:
    print("Enjoy your retirement!")
elif age_user >= 40 and age_user < 65:
    print("You're over the hill!")
elif age_user == 21:
    print("Congrats on your 21st")
elif age_user < 13:
    print("You qualify for the Kiddie discount!")
else :
    print("Age is just a number!")