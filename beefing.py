import random

namez = ["Reko", "Joe", "Angeltio", "Julius", "Alpo", "Henrique", "Mark", "Arthur", "Paul", "Anis", "Hugo"]
names = ["Aysin", "Iris", "Elina","Lea", "My", "Julie", "Helena", "Maria"]

def random_nimi ():
  dumb = random.randint(0,len(namez))
  return namez[dumb]

def random_names ():
    dumbz = random.randint(0,len(names))
    return names[dumbz]

print ("Do you want to know who someone is dating with? yes/no")
vastaus = raw_input()
print (" ")
if vastaus == "yes":
  print ("OK!")
else:
  print (":(")
  exit()


print ("his/hers gender: ")
sukupuoli = raw_input()
print (" ")
print ("hers/his name: ")
nimi = raw_input()
print (" ")

if sukupuoli == "female":
    print ("She is dating" (random_nimi())

if sukupuoli == "male":
    print ("He is dating" (random_names())


print (" ")
print ("This is a joke!!")
exit()
