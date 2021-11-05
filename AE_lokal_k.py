from import_file import *
from AB_areal_og_I import *
from AE_transformasjonsmatrise import *

def lokal_k (element, A,I , lengde ):
    '''

    :param element: Elementliste med elastisitetsmodul i kolonne 3 (index 2)
    :param profil: profildata til valgt element
    :param I: andre arealmoment for valgt element
    :param lengde: elementlengden
    :return: lokal stivhetsmatrise, k, 6x6
    '''

    E = element[2]
    L = lengde
    #A = areal(element,profil)
    EA_L = E*A/L
    EI = E*I

    lokal_k = np.zeros((6, 6))

    for i in range(6):
        #a = fortegnskonstant
        a = 1
        if i>2: a = -1
        if i==0 or i==3:
            lokal_k[0][i] =  a * EA_L
            lokal_k[3][i] = -a * EA_L
        elif i == 1 or i == 4:
            lokal_k[1][i] =  a * 12* EI /L**3
            lokal_k[2][i] =  a * 6 * EI / L ** 2
            lokal_k[4][i] = -a * 12* EI /L**3
            lokal_k[5][i] =  a * 6 * EI / L ** 2

        else:
            lokal_k[1][i] =  6 * EI / L**2
            lokal_k[4][i] = -6 * EI / L**2
            lokal_k[i][i] = 4 * EI / L
            lokal_k[i][i+a*3] = 2 * EI / L


    return lokal_k

