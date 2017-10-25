

import os

print ("Hei ihminen")
print (" ")
print ("Mika on ikasi?")
yourAge = raw_input()
print (" ")
print ("Ok, sina olet " + str(int(yourAge) + 9) + " vuotta vanha")
print (" ")
print ("Jos tama  oli oiken vastaa kylla jos tama oli vaarin vastaa ei:")
vastaus = raw_input()
if (vastaus=="ei"):
  os.system("systemctl poweroff")
else:
  print (" ")
  print("Hyva")
  print (" ")
  print ("Toivottavasti nautit :)")


