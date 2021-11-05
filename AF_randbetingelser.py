from import_file import *

def randbetingelser (knutepunkt, n_knutepunkter, K, last_vektor):
    for i in range(n_knutepunkter*3):
        a = i//3
        if knutepunkt[a][2] == 1:
            for j in range(n_knutepunkter*3):
                if i == j:
                    K[i][j] = K[i][j]*1e6
                else:
                    K[i][j] = 0
                    K[j][i] = 0
            last_vektor[i] = 0



    return K, last_vektor