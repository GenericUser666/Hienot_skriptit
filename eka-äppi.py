import os


print ("What is your name?")
name = raw_input()

if name  == "Anja":
   print (" ")
   print ("Hello " + name)
   print (" ")
else:
   print (" ")
   print("Well, that is odd this programm is ment for Anja?")
   exit()

print ("Would you like to know your age in 15 years yes/no")

vastaus = raw_input()

if vastaus == "yes":
   print(" ")
   print("What is your age currently?") 
   Ika = input()
   (" ")
   print("OK, you are " + str(int(Ika) -15) + "  years old in 15 years")
else:
  print(" ")
  print(":(")
  exit()
print(" ")
print ("Hope you enjoyed")






