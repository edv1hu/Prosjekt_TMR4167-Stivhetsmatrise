from import_file import *
from AE_transformasjonsmatrise import *

def lastvektor_pktlaster(n_punkter, punkter, laster, fim, fiq, n_elem, elementer, elementlengder):

    lastvektor = np.zeros((3*n_punkter,1))



    for i in range(n_elem):
        lokal_lvek = np.zeros((6, 1))
        ende_1 = int(elementer[i][0])
        ende_2 = int(elementer[i][1])
        l      = elementlengder[i]

        lokal_lvek [1]  += fiq[i][0]
        lokal_lvek [2]  -= fim[i][0]
        lokal_lvek [4]  += fiq[i][1]
        lokal_lvek [5]  -= fim[i][1]

        T = global_rot(elementer[i],punkter,l)
        global_lvek = np.dot(T, lokal_lvek)

        lastvektor[ende_1 * 3 + 2] += global_lvek[2]
        lastvektor[ende_2 * 3 + 2] += global_lvek[5]
        lastvektor[ende_1 * 3 + 1] += global_lvek[1]
        lastvektor[ende_2 * 3 + 1] += global_lvek[4]



    # Legger til alle kreftene som virker i punktene, disse er allerede globalt rotert
    # Itererer gjennom lastene for å finne punktlaster
    for last in laster:
        if last[0] == 1:
            punkt = int(last[1])
            fx = last[2]
            fy = last[3]

            i = int(punkt * 3)

            lastvektor[i] += fx
            lastvektor[i + 1] += fy

    return lastvektor