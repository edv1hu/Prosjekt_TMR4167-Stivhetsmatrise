from import_file import *

def fastinnspennings_mq (n_elementer , laster, elementlengder):
    fim = np.zeros((n_elementer, 2))
    fiq = np.zeros((n_elementer, 2))

    fastinnsp_matrise = np.zeros((n_elementer, 6))

    for last in laster:
        elem_nr = int(last[1])

        #For å vinkle alle kreftene riktig OBS! SJEKK!!!!
        rotasjon = np.cos(np.deg2rad(last[5]))

        F_1 = last[2] * rotasjon
        F_2 = last[3] * rotasjon
        l = elementlengder[elem_nr]


        if last[0] == 2:
            m1_F1 = - 1 / 20 * F_1 * l ** 2
            m2_F1 = 1 / 30 * F_1 * l ** 2
            m1_F2 = - 1 / 30 * F_2 * l ** 2
            m2_F2 = 1 / 20 * F_2 * l ** 2

            m_1 = m1_F1 + m1_F2
            m_2 = m2_F1 + m2_F2

            q_1 = -(7 / 20 * F_1 + 3 / 20 * F_2) * l
            q_2 = -(3 / 20 * F_1 + 7 / 20 * F_2) * l

            fim[elem_nr][0] = m_1
            fim[elem_nr][1] = m_2

            fiq[elem_nr][0] = q_1
            fiq[elem_nr][1] = q_2

            fastinnsp_matrise[elem_nr][1] = q_1
            fastinnsp_matrise[elem_nr][2] = m_1
            fastinnsp_matrise[elem_nr][4] = q_2
            fastinnsp_matrise[elem_nr][5] = m_2




    return fim,fiq, fastinnsp_matrise

