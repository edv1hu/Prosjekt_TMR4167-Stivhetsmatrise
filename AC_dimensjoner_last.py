from import_file import *
from AC_index_profil import *


def dimensjoner_fordeltlast(profildata, laster, elementer):
    '''
   Regner rikig størrelse på de fordelte lastene basert på at de er proporsjonale med bjelkenes diameter (Oppgitt i oppgaven)
   :param profildata: Liste over profildata for alle elementene sortert etter elementnummer
   :param laster: liste over alle lastene
   :return: liste over lastene med riktig størrelse på lastene
   '''
    # itererer gjennom hver last i lastlisten
    for last in laster:
        # Sjekker om lasten er en fordelt last
        if last[0] == 2:
            # Finner index til elementet lasten virker på
            elem_nr     = int(last[1])
            elem        = elementer[elem_nr]

            # Finner index til profilet som tilhører elementet
            profil_nr   = index_profildata(elem,profildata)
            profil      = profildata[profil_nr]

            # Kraftstørrelsene er dimensjonert for diameter på 1m
            # F_1 er kraften i lokal ende 1, F_2 i lokal ende 2
            F_1 = last[2]
            F_2 = last[3]

            # I profildata er dimensjonene lagret som ytre diameter og må dobles
            D = profil[1] * 2

            last[2] = F_1 * D
            last[3] = F_2 * D

    return laster

