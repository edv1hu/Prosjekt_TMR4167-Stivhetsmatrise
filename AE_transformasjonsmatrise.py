from import_file import *

def global_rot( element, punkter, lengde):
    punkt_1 = punkter[element[0]]
    punkt_2 = punkter[element[1]]
    l = lengde

    x_1 = punkt_1[0]
    x_2 = punkt_2[0]
    y_1 = punkt_1[1]
    y_2 = punkt_2[1]

    dy = y_2 - y_1
    dx = x_2 - x_1
    # Vinkel i radianer
    vinkel = np.arcsin(dy / l)

    t = np.zeros((2, 2))
    T = np.zeros((6,6))

    t[0][0] =   dx / l
    t[0][1] = - dy / l
    t[1][0] =   dy / l
    t[1][1] =   dx / l

    T[2][2] = T[5][5] = 1
    for i in range(2):
        for j in range(2):
            T[i][j] = T[i + 3][j + 3] = t[i][j]


    return T