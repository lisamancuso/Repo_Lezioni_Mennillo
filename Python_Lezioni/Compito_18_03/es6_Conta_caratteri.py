parola = input("Scrivere una parola a piacere: ")

if len(parola) < 5:
    print(f"La parola {parola} è corta")
elif len(parola) >= 5 and len(parola) < 8:
    print(f"La parola {parola} è media")
elif len(parola) >= 8:
    print(f"La parola {parola} è lunga")