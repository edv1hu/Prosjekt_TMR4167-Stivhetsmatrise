from import_file import *
from prettytable import PrettyTable
def print_deformations(rot, x_def, y_def, n_punkter):
    deformasjoner = PrettyTable()

    deformasjoner.field_names = ["Knutepunkt", "X-forskyvning", "Y-forskyvning", "Rotasjon"]
    for i in range(n_punkter):
        deformasjoner.add_row([i , round(x_def[i][0],5) ,round(y_def[i][0], 5), round(rot[i][0],5)])
        deformasjoner.align = 'r'
    print(deformasjoner)