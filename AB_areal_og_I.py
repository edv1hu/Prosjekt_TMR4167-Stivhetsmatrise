from import_file import *
from AC_index_profil import *


# Areal:

def ror_areal (profildata):
   R = profildata[1]
   t = profildata[2]
   A = ((np.pi * R**2) - (np.pi * (R - t)**2))
   return A

def ipe_areal (profildata):
   a_flens = profildata[1] * profildata[2]
   a_steg  = profildata[3] * profildata[4]
   A       = 2 * a_flens + a_steg
   return A

def areal(element, profildata):  # todo sjekk om regner rett
    '''

    :param element: Element
    :param profildata: Geometri og data til valgt element
    :return: tverrsnittsareal
    '''

    type_profil = element[3]

    # Sjekker om profilet er IPE
    if str(type_profil)[:1] == '1':
        A = ipe_areal(profildata)

    # Sjekker om profilet er rør
    elif str(type_profil)[:1] == '2':
        A = ror_areal(profildata)
    return A



# Arealtreghetsmoment:

def aam_I_profil (profildata):
    '''

    :param profildata: [profiltype, bredde flens, tykkelse flens, høyde steg, tykkelse steg]
    :return: areal treghetsmoment for et I_profil
    '''
    h_steg  = profildata[3]
    t_steg  = profildata[4]
    b_flens = profildata[1]
    t_flens = profildata[2]

    arm     = h_steg/2  + t_flens/2
    I_steg  = t_steg    * h_steg**3 /12
    I_flens = b_flens   * t_flens**3/12

    I_total = I_steg + 2*(I_flens + b_flens*t_flens * arm**2)

    return I_total

def aam_ror_profil(profildata):
    '''

    :param profildata: [profiltype, Ytre radius, tykkelse rør, 0, 0]
    :return: areal treghetsmoment for et rørprofil
    '''
    R = profildata[1]   # Ytre radius
    r = R - profildata[2]

    I_total = (np.pi / 4) * (R**4 - r**4) # Bruker formel for tykkveggede tverrsnitt

    return I_total

def andre_arealmoment (n_elem, elementer, profildata):
    '''

        :param elem: Liste over elementer
        :param n_elem: Antall elementer
        :param profildata: Liste over mål på profiler
        :return: Todimensjonal liste med andre arealmoment og arealsenter
        '''
    I = np.zeros((n_elem, 2))


    for i in range(0, n_elem):

        if n_elem == 1:
            profiltype = elementer[3]
        else:
            profiltype = elementer[i][3]

        profil_nr = index_profildata(elementer[i], profildata)
        profil    = profildata[profil_nr]

        # Sjekker om profilet er IPE
        if str(profiltype)[:1] == '1':

            # Regner høyden opp til arealsenteret
            # halve høyden på steget  + tykkelsen på flensen (antar lik tykkelse på begge flensene)
            z_c = profil[3] / 2 + profil[2]

            I_total = aam_I_profil(profil)

            I[i][0] = I_total
            I[i][1] = z_c

        # Sjekker om profilet er rør
        elif str(profiltype)[:1] == '2':

            # Høyden til arealsenteret er lik ytre radius
            z_c = profil[1]

            I_total = aam_ror_profil(profil)

            I[i][0] = I_total
            I[i][1] = z_c

    return I