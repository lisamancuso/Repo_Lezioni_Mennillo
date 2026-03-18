nome = input("Come ti chiami? ")
eta = int(input("Quanti hanni hai? "))

if eta <= 0 or eta > 120:
    print(f"{eta} anni non è un'età valida")
else:
    print(f"Ciao {nome}, tra 5 anni avrai {eta + 5} anni")