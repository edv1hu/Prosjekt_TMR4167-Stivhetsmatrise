import numpy as np

from import_file import *
from AE_transformasjonsmatrise import *
from AE_lokal_k import *
from AC_index_profil import *


def system_stivhetsmatrise( n_elem, elementer, elementlengder, profildata, n_punkt,punkter, I,A):
    K = np.zeros((n_punkt *3, n_punkt *3))

    for i in range(n_elem):
        elem  = elementer[i]
        l     = elementlengder[i]
        index = index_profildata(elem, profildata)  #index for profildata
        #A     = areal(elem, profildata[index])


        if profildata[index][0] == elem[3]:
            k = lokal_k(elem,A[i], I[i], l)
            T = global_rot(elem,punkter,l)
            T_inv = np.linalg.inv(T)
            k_global = np.linalg.multi_dot([T,k,T_inv])

            K = legg_til_K(elem,k_global, K)

    return K



def legg_til_K (element, global_k , K):
    #lokal ende :
    lokal_ende_1 = element[0]
    lokal_ende_2 = element[1]

    #global ende _
    global_ende_1 = 3* ( lokal_ende_1 )
    global_ende_2 = 3* ( lokal_ende_2 )
    rad = 0
    col = 0
    for i in range(6):
        for j in range(6):
            if i >=0 and i<3 : rad = global_ende_1 +i
            else    : rad = global_ende_2 +i-3
            if j >= 0 and j <3 : col = global_ende_1 +j
            else    : col = global_ende_2 +j-3
            input       = global_k[i][j]
            K[rad][col] += input

    return K

