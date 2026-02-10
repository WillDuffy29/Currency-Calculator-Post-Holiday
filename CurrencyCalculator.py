# Currency Calculator Post-Holiday

print ("Wow! Quite some money you have left there... May I translate it back to USD for you?")

a = float(input("How many 🇨🇴 Colombian pesos 🇨🇴 do you have remaining?"))
print("You have:")
print (a), print ("🇨🇴 Colombian Pesos")
print("Whew! Okay then... Let's continue!")

b = float(input("How many 🇵🇪 Peruvian soles 🇵🇪 do you have remaining?"))
print("You have:")
print (b), print ("🇵🇪 Peruvian soles")
print("Okay, we're getting there!")

c = float(input("How many 🇧🇷 Brazilian reais 🇧🇷 do you have remaining?"))
print("You have:")
print (c), print ("🇧🇷 Brazilian reais")

# Calculating exchange rate for USD (EXCHANGE RATE AS OF 09/02/26)
# This is only a fixed exchange rate and may become outdated. Can manually update if needed.

a_rate = a / 3659.57
b_rate = b / 3.36
c_rate = c / 5.19

USD = a_rate + b_rate + c_rate

print ("Looking good! You have a total of:")
print (USD), print ("USD! 🇺🇸")