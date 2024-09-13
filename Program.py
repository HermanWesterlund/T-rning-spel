import random
from reader import feed
import time
print("Är ni redo att starta spelet?")
blank = str(input(""))
print ("Datorns första slag")
time.sleep(1)
datorSlag1 = random.randint(1,6)
datorSlag2 = + random.randint(1,6)
allaLever = True
print (f'Datorn slog {datorSlag1}')
time.sleep(2)
print ("Datorns andra slag")
time.sleep(1)
print (f'Datorn slog {datorSlag2}')
datorLiv = datorSlag2 + datorSlag1
time.sleep(2)
print ("Datorns totala liv: " +str(datorLiv))
time.sleep(1)
print("Din tur. Redo att slå?")
blank = str(input(""))
print("\nDitt första slag")
spelarSlag1 = random.randint(1,6)
blank = str(input(""))
print(spelarSlag1)
print("\nDitt andra slag")
spelarSlag2 = random.randint(1,6)
blank = str(input(""))
print(spelarSlag2)
spelarSlag3 = 0
if spelarSlag1 == 1 and spelarSlag2 == 6:
    print("...")
    time.sleep(1)
    print("..?")
    time.sleep(1)
    print("Den hemliga kombinationen!")
    time.sleep(1)
    print("Du får ett extra slag med en dubbel tärning!")
    time.sleep(1)
    spelarSlag3 = random.randint(1,12)
    time.sleep(1)
    print(f'Du slog {spelarSlag3}')
spelarLiv = spelarSlag1 + spelarSlag2 + spelarSlag3
time.sleep(1)
print("Ditt totala liv: " + str(spelarLiv))
blank = str(input(""))
while allaLever:
    print ("Datorns tur")
    datorSlag1 = random.randint(1,6)
    time.sleep(1)
    print("Datorn slog " + str(datorSlag1))
    time.sleep(1)
    if datorSlag1 > 3:
        print("Datorn gör " + str(datorSlag1) + " skada på dig")
        spelarLiv = spelarLiv - datorSlag1
        time.sleep(1)
        print("Du har " + str(spelarLiv) + " liv kvar\n")
    else:
        print (f'Datorn gör {datorSlag1} skada på sig själv')
        datorLiv = datorLiv - datorSlag1
        time.sleep(1)
        print (f'Datorn har {datorLiv} liv kvar\n')
    if datorLiv <= 0:
        time.sleep(1)
        print("Datorn dog lol")
        allaLever = False
        break
    if spelarLiv <= 0:
        time.sleep(1)
        print("Du dog lol")
        allaLever = False
        break
    time.sleep(1)
    print("Ditt slag")
    spelarSlag1 = random.randint(1,6)
    blank = str(input(""))
    print(f'Du slog {spelarSlag1}')
    blank = str(input(""))
    if spelarSlag1 > 3:
        print(f'Du gör {spelarSlag1} skada på datorn')
        datorLiv = datorLiv - spelarSlag1
        blank = str(input(""))
        print(f'Datorn har {datorLiv} liv kvar\n')
    else:
        print(f'Du gör {spelarSlag1} skada på dig själv')
        spelarLiv = spelarLiv - spelarSlag1
        blank = str(input(""))
        print(f'Du har {spelarLiv} liv kvar\n')
    if datorLiv <= 0:
        time.sleep(1)
        print("Datorn dog lol")
        allaLever = False
        break
    if spelarLiv <= 0:
        time.sleep(1)
        print("Du dog lol")
        allaLever = False
        break
    time.sleep(1)
time.sleep(1)
vinnare = ""
if spelarLiv > datorLiv:
    vinnare = "spelare"
else:
    vinnare = "datorn"
print(f'{vinnare} vinner')