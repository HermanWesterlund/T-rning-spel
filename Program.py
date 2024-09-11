import random
print ("Datorns första slag")
datorSlag1 = random.randint(1,6)
datorSlag2 = + random.randint(1,6)
allaLever = True
blank = str (input(""))
print (datorSlag1)
print ("Datorns andra slag")
blank = str(input(""))
print (datorSlag2)
datorLiv = datorSlag2 + datorSlag1
print ("Datorns totala liv: " +str(datorLiv))
blank = str(input(""))
print("Ditt första slag")
spelarSlag1 = random.randint(1,6)
blank = str(input(""))
print(spelarSlag1)
print("Ditt andra slag")
spelarSlag2 = random.randint(1,6)
blank = str(input(""))
print(spelarSlag2)
spelarLiv = spelarSlag1 + spelarSlag2
blank = str(input(""))
print("Ditt totala liv: " + str(spelarLiv))
blank = str(input(""))
while allaLever:
    print ("Datorns slag")
    datorSlag1 = random.randint(1,6)
    blank = str(input(""))
    print("Datorn slog " + str(datorSlag1))
    blank = str(input(""))
    if datorSlag1 > 3:
        print("Datorn gör " + str(datorSlag1) + " skada på dig")
        spelarLiv = spelarLiv - datorSlag1
        blank = str(input(""))
        print("Du har " + str(spelarLiv) + " liv kvar")
    else:
        print (f'Datorn gör {datorSlag1} skada på sig själv')
        datorLiv = datorLiv - datorSlag1
        blank = str(input(""))
        print (f'Datorn har {datorLiv} liv kvar')
    if datorLiv <= 0:
        blank = str(input(""))
        print("Datorn dog lol")
        allaLever = False
        break
    if spelarLiv <= 0:
        blank = str(input(""))
        print("Du dog lol")
        allaLever = False
        break
    blank = str(input(""))
    print("Ditt slag")
    spelarSlag1 = random.randint(1,6)
    blank = str(input(""))
    print(f'Du slog {spelarSlag1}')
    blank = str(input(""))
    if spelarSlag1 > 3:
        print(f'Du gör {spelarSlag1} skada på datorn')
        datorLiv = datorLiv - spelarSlag1
        blank = str(input(""))
        print(f'Datorn har {datorLiv} liv kvar')
    else:
        print(f'Du gör {spelarSlag1} skada på dig själv')
        spelarLiv = spelarLiv - spelarSlag1
        blank = str(input(""))
        print(f'Du har {spelarLiv} liv kvar')
    if datorLiv <= 0:
        blank = str(input(""))
        print("Datorn dog lol")
        allaLever = False
        break
    if spelarLiv <= 0:
        blank = str(input(""))
        print("Du dog lol")
        allaLever = False
        break
    blank = str(input(""))
blank = str(input(""))
vinnare = ""
if spelarLiv > datorLiv:
    vinnare = "spelare"
else:
    vinnare = "datorn"
print(f'{vinnare} vinner')