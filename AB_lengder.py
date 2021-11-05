from structure_visualization import *


def lengder(knutepunkt, element, n_elem):
    elementlengder = np.zeros((n_elem))

    # Beregner elementlengder med Pythagoras' læresetning
    for i in range(0, n_elem):
        # OBS! Grunnet indekseringsyntaks i Python-arrays vil ikke denne funksjonen fungere naar vi bare har ett element.
        dx = knutepunkt[element[i, 0], 0] - knutepunkt[element[i, 1], 0]
        dy = knutepunkt[element[i, 0], 1] - knutepunkt[element[i, 1], 1]
        elementlengder[i] = np.sqrt(dx * dx + dy * dy)
    return elementlengder

