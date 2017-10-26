from os import walk
from time import sleep as sl

manifesto = "Ur files are encrypted to recover them do the following : "

files = []
for (dirpath, dirnames, filenames) in walk("."):
    files.extend(filenames)
    break

for i in files:
    try:
        sl(0.5)
        print "Encrypting file : " + i

        pass
    except KeyboardInterrupt:
        print "no escape"
i = 0

print manifesto

while i != 10:
    try:
        print "send 5 BTC to XhgU55ygGfghft555crcrcYJTcgh"
    except KeyboardInterrupt:
        print "no escape"

    sl(1)
    i += 1
    pass
