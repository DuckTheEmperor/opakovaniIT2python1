#Vypsani jmena a prijmeni
x = "Wiktor"
y = "Kotas"
print (x + y)

#Zadani veku uzivatele a vypsani dekuji
try:
    age = int(input("Zadejte svůj věk: ")) 
    print("Děkuji")
    print (age)
except ValueError:
    print("Zadej jen celočíselnou hodnotu.")
#Pouzil jsem tady try except protoze jsem si nepamatoval jak se to dela
#Try except overuje jestli zadane cislo je cele cislo nebo ne a kdyz se mu to nepodari dostane value error ktery vypise text

#Delky prvnich dvou promenn
print (len(x))
print (len(y))

#Vytvoreni promene a cyklus
z = 6
while z < 21:
    print (z)
    z += 3
else:
    print ("Koncova hodnota:",z)

#Vypsani nahodneho cisla
import random
print(random.randint(1,10))