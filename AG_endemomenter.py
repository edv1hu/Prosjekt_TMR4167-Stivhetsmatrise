import numpy as np
from AE_lokal_k import *
from AE_transformasjonsmatrise import *
from import_file import *
from AC_index_profil import *
def elementkrefter (K, lastvektor,n_elementer, elementer, elementlengder, punkter, deformasjoner, profiler,I, fim, fastinsp_mat):

    K_inv = np.linalg.inv(K)
    r     = np.dot(K_inv, lastvektor)
    print(r)
    for i in range(n_elementer):
        elem = elementer[i]
        T = global_rot(elem, punkter, elementlengder[i])
        T_inv = np.linalg.inv(T)
        index = index_profildata(elem, profiler)
        A = areal(elem, profiler[index])
        k_lokal = lokal_k(elem,A[i], I[i][0], elementlengder[i])

        ende1 = elem[0]
        ende2 = elem[1]

        lokale_def = np.zeros((6,1))
        for j in range(3):
            lokale_def[j]     = deformasjoner[ende1*3 + j]
            lokale_def[3 + j] = deformasjoner[ende2*3 + j]

        v = np.linalg.solve(T,lokale_def)

        lokal_fim = fastinsp_mat[i]

        print(lokal_fim)

        krefter = np.dot(k_lokal, v)
        print(krefter)
