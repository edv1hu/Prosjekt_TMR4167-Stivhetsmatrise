from import_file import *
from AC_index_profil import *
from AB_areal_og_I import *

class Element:
    #index på de lokale endene
    ende_1 = int
    ende_2 = int

    #punktdata
    punkt_1 = []
    punkt_2 = []

    E = int
    I = float
    A = float


    profil_type = int
    profil = []

    laster = []





def ant_elementer (n_elem):
    elem_list = []
    for i in range(n_elem):
        elem_list.append("element_" + str(i))
    return elem_list

def add_elements (n_elem, elementer, elem_list, profiler, punkter):

    #Liste med andre arealmoment sortert i elementrekkefølge
    I = andre_arealmoment(n_elem, elementer, profiler)

    for i in range(n_elem):
        elem = elementer[i]
        e = elem_list[i]

        #Lager et objekt for elementet og legger inn data i Element-klassens variabler
        e = Element()
        e.ende_1     = elem[0]
        e.ende_2     = elem[1]


        e.E          = elem[2]
        e.I          = I[i]
        e.profil_type = elem[3]

        # Finner indexen til riktig proofil og legger til listen med profildata for profilet
        #til profil-variablen til elementet
        index = index_profildata(elem, profiler)
        p_data = profiler[index]


        e.profil = p_data

        # Lagrer punktdata( x, y, fastinnsp.) til element-klassen
        e.punkt_1 = punkter[e.ende_1]
        e.punkt_2 = punkter[e.ende_2]

        #Regner profilets areal
        A = areal(elem, p_data)

        e.A = A




