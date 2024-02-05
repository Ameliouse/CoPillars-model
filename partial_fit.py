import pandas as pd
import numpy as np
import sys
from time import time
from time import sleep

from typing import List
from pyBKT.models import Model

import bkt

if __name__ == '__main__':    

    if len(sys.argv) != 5:
        print("pb nb paramètres")
        sys.exit(1)

    # Récupérer les arguments de la ligne de commande
    user_id = sys.argv[1]
    skill_id = sys.argv[2]
    correct = sys.argv[3]
    path_load_model = sys.argv[4]

    # df_train = pd.read_csv(path)
    print("moddle")

    bkt.partial_fit_model(None, int(user_id), int(skill_id),int(correct), fileName_load_model=path_load_model)
    sleep(0.5)

    print("byebye")

    # print("byebye")