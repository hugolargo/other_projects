import random

zahlen_lotto=[]
zahlen_lotto.extend(range(1,50))

zahlen_euro=[]
zahlen_euro.extend(range(1, 51))

spielen=True
while spielen==True:
    spielart=input("🤑 [E]urojackpot oder [L]otto? 🤑 ")
    spielart=spielart.upper()
    #LOTTO 6aus49
    if spielart=="L":
        input("\nWähle 6 Zahlen\n : HIT ENTER")

        gewinnzahlen=random.sample(zahlen_lotto, 6)
        gewinnzahlen.sort()
        print(gewinnzahlen)

        superzahl=random.randint(0,9)
        print("\nSuperzahl: " + str(superzahl))
    #EUROJACKPOT
    elif spielart=="E":
        input("\nWähle 5 Zahlen\n : HIT ENTER")

        gewinnzahlen=random.sample(zahlen_euro, 5)
        gewinnzahlen.sort()
        print(gewinnzahlen)

        eurozahlen=random.sample(range(1,12), 2)
        eurozahlen.sort()
        print("\nEurozahlen: " + str(eurozahlen))
    else:
        print("Wrong input")
    #NOCH MAL
    restart=input("NOCH MAL SPIELEN: 'ENTER' or [q]uit")
    if restart=="q":
        spielen=False
    else: spielen=True
    






