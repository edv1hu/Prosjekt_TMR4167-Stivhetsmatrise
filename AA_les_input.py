from import_file import *

def lesinput():
    # Åpner inputfilen
    file_in_data = open("test_2_input.txt", "r")

    # Leser totalt antall punkter og lagrer antallet som int
    n_punkter = int(file_in_data.readline())

    # Leser alle punktene og lagrer i en liste der hvert punkt består av x-koordinat, y-koordinat og fastinnspenning
    punkter = np.loadtxt(file_in_data, dtype=float, max_rows=n_punkter)


    # Leser antall elementer
    n_elem = int(file_in_data.readline())

    # Leser inn element-data; lokalt punkt 1, lokalt punkt 2, Elastisitetsmodul, Profiltype
    # Elementnummer tilsvarer radnummer i "elem"-variabel
    elementer = np.loadtxt(file_in_data, dtype=int, max_rows=n_elem)

    # Leser antall laster som virker på rammen
    n_last = int(file_in_data.readline())

    # Leser lastdata
    laster = np.loadtxt(file_in_data, dtype=float, max_rows=n_last)

    # Leser antall profiltyper totalt, både IPE og ror
    n_profiler = int(file_in_data.readline())

    # Leser profildata
    profiler = np.loadtxt(file_in_data, dtype=float, max_rows=n_profiler)



    # Lukker input-filen
    file_in_data.close()

    return n_punkter, punkter, n_elem, elementer, n_last, laster,n_profiler, profiler
