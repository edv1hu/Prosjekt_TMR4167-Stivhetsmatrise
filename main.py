import numpy as np

from structure_visualization    import *
from AA_les_input               import *
from AA_klas                    import *
from AB_lengder                 import *
from AC_dimensjoner_last        import *
from AB_areal_og_I              import *
from AD_fim                     import *
from AE_lokal_k                 import *
from AE_transformasjonsmatrise  import *
from AE_lastvektor              import *
from AE_store_stivhetsmatrisen  import *
from AF_randbetingelser         import *
from AG_endemomenter            import *
from AP_print                   import *

# -----Rammeanalyse-----
def main():
    # -----Initialiserer figurer-----
    fig_init, ax_init, fig_def, ax_def = setup_plots()
    # -----Til visualiseringen, velg første indeks brukt i nummerering av noder og element-----
    first_index = 0


    # -----Leser input-data-----
    n_punkter, punkter, n_elementer, elementer, n_laster, laster_udimensjonert, n_profiler, profiler = lesinput()

    elem_list = ant_elementer(n_elementer)
    add_elements(n_elementer, elementer, elem_list, profiler)



    # -----Plott initalramme-----
    plot_structure(ax_init, punkter, elementer, 1, first_index)

    # Dimensjonerer de fordelte lastene til diameteren på rørprofilene de virker på
    laster = dimensjoner_fordeltlast(profiler, laster_udimensjonert, elementer)

    #test fil: Areal og aam
    #I = np.array([3.692e-5, 1.943e-5,3.692e-5,3.692e-5,3.692e-5,1.943e-5,  2.06e-6])
    #A = np.array([0.005383, 0.002848,0.005383,0.005383,0.005383,0.002848,0.00135])
    #testfil 2
    #A = np.array([1,1,1,1,1,1,1])
    #I = np.array([1, np.sqrt(2), 10,5,np.sqrt(2),5,10])
    #I = np.array([1,1,1,1,1,1,1])
    A = np.array([1,1,1])
    I = np.array([1,1,1])

    # -----Regner andre arealmoment ------



    # -----Regner ut lengder til elementene------
    elementlengder = lengder(punkter, elementer, n_elementer)


    # -----Fastinnspenningsmomentene------
    # Regner ut fastinnspenningsmomentene for elementene
    fim, fiq, fastinnsp_mat = fastinnspennings_mq( n_elementer, laster, elementlengder)

    # -----Lastvektor-----
    lastvektor = lastvektor_pktlaster(n_punkter,punkter,laster, fim, fiq, n_elementer, elementer, elementlengder)

    # -----Systemets stivhetsmatrise-----
    K_system = system_stivhetsmatrise(n_elementer, elementer, elementlengder, profiler, n_punkter,punkter, I,A)

    # -----Justerer stivhetsmatrisen og lastvektoren til randbetingelsene -----
    K, L_vek = randbetingelser(punkter,n_punkter,K_system,lastvektor)


    # -----Sjekk av deformasjoner -----
    deform_test = np.linalg.solve(K, L_vek)

    # -----Deler deformasjonsvektoren i rotasjoner, x- og y-forskyvning -----
    rot = deform_test[2::3]
    x_def = deform_test[0::3]
    y_def = deform_test[1::3]


    # -----Regner ut knutepunktkreftene -----
    #elementkrefter(K, L_vek,n_elementer, elementer,  elementlengder,punkter, deform_test, profiler, I, fim, fastinnsp_mat)

    print_deformations(rot, x_def, y_def, n_punkter)
    # ------Finner endemoment for hvert element-----
    #endemoment = endeM(n_punkter, punkter, n_elementer, elementer, elementlengder, rot, fim)


    # -----Plott deformert ramme-----
    skalering = 1e-3;  # Du kan endre denne konstanten for å skalere de synlige deformasjonene til rammen
    plot_structure_def(ax_def, punkter, elementer, 1, first_index, skalering * rot)
    plt.show()

main()