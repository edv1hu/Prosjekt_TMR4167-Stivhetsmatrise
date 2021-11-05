
def index_profildata(element, profildata_liste):
    type_profil = element[3]
    for i in range(len(profildata_liste)):
        if type_profil == profildata_liste[i][0]:
            return i
