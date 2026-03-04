# Questo è un commento
# Cos'è una variabile? E' un contenitore che memorizza un valore. Questo valore può cambiare (arbitrariamente) durante l'esecuzione del codice.

#Assegno una variabile
nome = "Lisa"   #String
eta = 20        #Intero
corso = "Tecnico informatico 2025/26"   #String
altezza = 1.64  #Float

#Indipendentemente dal tipo che scelgo non viene dichiarato da nessuna parte. Questo comportamento è tipico dei linguaggi debolmente tipizzati

# ESERCZIO 2: Istanzia 2 variabili (nome a tua scelta) di tipo intero. Con queste 2 variabili elabora le 4 operazioni matematiche. Stampa con print i risultati
x = 5
y = 8
somma = x + y
sottr = y - x
per = x * y
div = y / x
print("La somma è", somma)
print("La sottrazione è", sottr)
print("Il prodotto è", per)
print("Il quoziente è", round(div, 2))

# Numeri con la virgola o float
pi = 3.14159
temperatura = 21.5

# controllare che tipo sono
print(type(pi))
print(type(temperatura))

calcolo = 0.1 + 0.2
print(calcolo)
print(round(calcolo, 2)) # arrotondare numeri, numero è per decidere quante cifre dopo la virgola mostrare

#Stringhe: sequenze immutabili di caratteri
nomeUser = "Anna99"
emailUser = "anna@mail.com"
etaUser = 31
corso = "Tecnico Informatico"

#Concatenazione tra stringhe
print(nomeUser + " " + emailUser, "anni", etaUser)# + per stringhe e , per numeri

#f-string è il modo moderno di formattare le stringhe
print(f"{nomeUser} - email: {emailUser} - età {etaUser}")

#ESERCIZIO: presenta te stesso: mioNome, mioCognome, miaEta, mioCorso con il metodo string
mioNome = "Lisa"
mioCognome = "Mancuso"
miaEta = 20
mioCorso = "Tecnico informatico 2025/26"

print(f"Il mio nome è {mioNome} {mioCognome}, ho {miaEta} anni e frequento il corso di {mioCorso}")