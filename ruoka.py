import random

ruoka = ["Pizza", "Hamburger", "Salmon", "Ceasar salad", "Tacos"]

def eparuoka ():
    satunnainen_numero = random.randint(0, len(ruoka) - 1)
    return ruoka[satunnainen_numero] 

print ("Do you want to know your least favorite food in 20 yrs. yes/no ")
vastaus = raw_input()

if vastaus == "yes":
    print ("OK you have commited to answer four questions to determine what the asnwer will be.")
    print(" ")
    print ("1.Whats is your cuurent favorite food:")
    lempiruoka = raw_input()
    print ("2.What is your least favorite food currently")
    juttu = raw_input()
    print ("3.What would you order from McDonald's")
    McDonald = raw_input()
    print ("What do you think your least favorite food will be in 20 years")
    moi = raw_input()
    print( eparuoka() )

else:
    print (": )")
    exit()
