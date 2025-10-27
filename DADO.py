#scrivi un programma che simula il lancio di uno o più dadi. Chiedi all'utente quanti dadi 
# vuole lanciare e stampa il risultato per ciascuno

import random
def lancia_dadi():
    dadi=int(input("quanti dadi vuoi lanciare?: "))

    for i in range (0,dadi):
        risultato_lancio = random.randint(1,6)
        print("Al lancio del dado " + str(i+1) + ", è uscito " + str(risultato_lancio))

lancia_dadi()