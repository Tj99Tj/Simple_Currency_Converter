print("Welcome to Thomas Johnston's Currency Converter!")
print("Currency Conversions Correct as of 03/10/2018")
print("When inputting your currency choices please use the 3 letter code in block capitals e.g. USD for dollar")
basecurrency = input("What currency do you have? \n 1) EUR \n 2) USD \n 3) GBP \n")
exchangecurrency = input("Which currency would you like to convert to?\n")

if basecurrency == "EUR" and exchangecurrency == "USD":
    print("How many euros would you like to convert? In numbers please")
    amount = float(input())
    print("You will receive $:", amount*1.15458)

if basecurrency == "EUR" and exchangecurrency == "GBP":
    print("How many euros would you like to convert? In numbers please!")
    amount = float(input())
    print("You will receive £:", amount*0.889916)

if basecurrency == "USD" and exchangecurrency == "EUR":
    print("How many dollars would you like to convert? In numbers please!")
    amount = float(input())
    print("You will receive €:", amount*0.866206)

if basecurrency == "USD" and exchangecurrency == "GBP":
    print("How many dollars would you like to convert? In numbers please!")
    amount = float(input())
    print("You will receive £:", amount*0.770773)

if basecurrency == "GBP" and exchangecurrency == "EUR":
    print("How many pounds would you like to convert? In numbers please!")
    amount = float(input())
    print("You will receive €:", amount*1.12375)

if basecurrency == "GBP" and exchangecurrency == "USD":
    print("How many pounds would you like to convert? In numbers please!")
    amount = float(input())
    print("You will receive $:", amount*1.129753)
