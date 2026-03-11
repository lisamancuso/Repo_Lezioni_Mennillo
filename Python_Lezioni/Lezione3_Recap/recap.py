nome = "Lisa"
cognome = "Mancuso"
eta = 20
corso = "Tecnico Informatico"
altezza = 1.64
presenza = True

# con queste variabili crea una "presentazione" di te stesso utilizzando il metodo print con una f-string all'interno

print(f"Mi presento: \nMi chiamo {nome} {cognome} e ho {eta} anni.")
print(f"Studio nel corso di {corso}.")
print(f"Altezza {altezza} m")

if presenza:
    print("Oggi sono presente")
else:
    print("Oggi sono assente")

print("====== IL MIO AMICO ======")
#Adesso presenta un tuo compagno/amico di classe. Fai attenzione ad assegnare delle variabili con un altro nome

nomeAmico = "Gabriele"
cognomeAmico = "Conte"
etaAmico = 17
corsoAmico = "Tecnico Informatico"
altezzaAmico = 1.68
presenzaAmico = False

print(f"Presento il mio amico: \nSi chiama {nomeAmico} {cognomeAmico} e ha {etaAmico} anni.")
print(f"Studia nel corso di {corsoAmico}.")
print(f"Altezza {altezzaAmico} m")

if presenzaAmico:
    print("Oggi è presente")
else:
    print("Oggi è assente")

if etaAmico < 60 :
    print(f"{nomeAmico} è ancora giovane")
else:
    print(f"{nomeAmico} non è più così giovane")