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