# IF STATEMENT. Questo costrutto server a controllare e prendere una scelta.
# Operatori di confronto
# == (uguale a)
# != (diverso da)
# > (maggiore)
# < (minore)
# >= (maggiore uguale)
# <= (minore uguale)

# Tutte le volte che uso un operatore di confronto sto generando un valore booleano

#I valori boolean mi servono proprio negli if statement

#SINTASSI:
# if condizione:
#       corpo dell'if che viene eseguito se condizione è true
# else:
#       corpo dell'if che viene eseguito se condizione è false

#Esempio 1
piove = False

if piove:
    print("Porto l'ombrello")
else:
    print("Non porto l'ombrello")

#Esempio 2
miaEta = 20

if miaEta >= 18:
    print(f"Io ho {miaEta} e quindi sono maggiorenne")
elif miaEta < 0:
    print(f"Inserire un'età valida, {miaEta} non è un'età valida")
else:
    print(f"Io ho {miaEta} e quindi sono minorenne")

#Esempio 3
etaLo = 18
etaSa = 17

if etaLo > etaSa:
    print(f"Lorenzo ha {etaLo} anni ed è più grande di Sanna che ha {etaSa} anni")
elif etaLo == etaSa:
    print("Sanna e Lorenzo sono coetanei")
else:
    print(f"Sanna ha {etaSa} ed è più grande di Lorenzo che ha {etaLo}")

#Esempio 4 
parola1 = "ciao"
parola2 = "ciao"
parola3 = "Ciao"

if parola1 == parola2:
    print("Le due parole sono uguali")
elif parola1 != parola2:
    print("Le due parole sono diverse")
else:
    print("Non mi hai fornito due parole")

if parola1 == parola3:
    print("Le due parole sono uguali")
elif parola1 != parola3:
    print("Le due parole sono diverse")
else:
    print("Non mi hai fornito due parole")

#Esempio 5 - Confronto tra stringhe case insensitive

stringa1 = "Caffè"
stringa2 = "caffè"

if stringa1.lower() == stringa2.lower():
    print(f"Le due stringhe sono uguali: {stringa1}")
else:
    print(f"Le due stringhe sono diverse: {stringa1} e {stringa2}")

#Esempio 6 - Altri confonti tra stringhe
# Possiamo confontare porzioni di stringhe

frase = "Ciao Dario, come stai?"

print(frase.startswith("Cia")) #True
print(frase.endswith("?")) #True
print("Dario" in frase) #True

if "Dario" in frase:
    print("La stringa Dario si trova nella frase")
else:
    print("La stringa Dario non si trova nella frase")

if frase.startswith("Cia"):
    print("La frase comincia con Cia")
else:
    print("La frase non cominica con Cia")

#Esempio 7 - Voto e valutazione
#Patente di guida. Per iscrivermi all'esame devo aver compiuto 18 anni.

etaStudente = int(input("Quanti anni hai?")) #Attenzione a età. Tutto quello preso da un input è considerato una stringa
nomeStudente = input("Come ti chiami?")

if etaStudente >= 18 and etaStudente < 80:
    print(f"Benvenuto/a {nomeStudente}, puoi iscriverti all'esame di scuola guida")
elif etaStudente < 18 and etaStudente >= 15:
    print(f"Benvenuto/a {nomeStudente}, con la tua età puoi solo accedere all'esame per la patente AM")
else:
    print(f"Benvenuto/a {nomeStudente}, con la tua età non puoi ancora iscriverti a nessuna scuola guida")