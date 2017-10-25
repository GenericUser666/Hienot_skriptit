


import os


print("Good day!")
print(" ")
print("Would you like some tea?")

vastaus = raw_input()

if vastaus == "yes":
  print (" ")
  print ("OK")
  print (" ")
else:
  print (" ")
  print (":(")
  print (" ")
  print ("Would you like to continue?")
  print (" ")
  juttu = raw_input()
  if juttu == "yes":
    print("OK")
    os.system ("reboot")
  else:
    os.system ("reboot")

print("Would you like some biscuits? ")
kiva = raw_input()

while kiva  != "no thank you" and  kiva != "yes please":
  print (" ")
  print ("Excuse me?")
  kiva = raw_input()
  print (" ")
print ("OK!")
exit()

 







