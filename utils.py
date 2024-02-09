import pandas as pd
import random
import numpy as np
import sys

from time import time
from typing import List
from pyBKT.models import Model

MECA = {0 : "hexa", 1 : "carr",
        3 : "sun"}
LIMIT = 0.9

def generate_data(fileName_model : str, nb_players : int, skill_id : int) -> None:
    """generate random success for a skill and nb_player players

    Args:
        fileName (str): csv file name
        nb_players (int): number of players
        skill_id (int): skill id
    """
    l_id = []
    l_skill = []
    l_correct = []
    for i in range(0, nb_players):
        for _ in range(0, random.randint(1,6)):
            correct = random.randint(0,1)
            l_id.append(i)
            l_skill.append(skill_id)
            l_correct.append(correct)
        
    data = {"user_id" : l_id, "skill_name" : l_skill, "correct" : l_correct}        
    df = pd.DataFrame(data)
    df.to_csv(fileName_model, index = False)
    return

def add_data_to_model(user_id : int, skill_id : int, correct : int, nb : int, fileName_model : str = "data/all_data.csv") -> None:
    
    """add success or fail for user_id and skill_id

    Args:
        fileName (str): csv file name
        user_id (int): player id
        skill_id (int): skill id
    """
    data = {"user_id" : [user_id], "skill_name" : [skill_id], "correct" : [correct]}        
    df = pd.DataFrame(data)
    for i in range(0, nb):
        df.to_csv(fileName_model, mode='a', index=False, header=False, lineterminator='\n')
    return

def set_p_skill(fileName_prob : str, user_id : int, skill_name : str, p : float) -> None :
    """set the probability p in the csv file

    Args:
        fileName_prob (str): csv file name to update
        skill_name (str): skill name
        user_id (int): player id
        p (float): probability of success
    """
    df = pd.read_csv(fileName_prob)
    df.loc[user_id, skill_name] = p
    df.to_csv(fileName_prob, index=False)
    return


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("pb nb paramètres")
        sys.exit(1)

    # Récupérer les arguments de la ligne de commande
    user_id = sys.argv[1]
    skill_id = sys.argv[2]
    correct = sys.argv[3]
    nb = sys.argv[4]

    
    add_data_to_model(int(user_id), int(skill_id),int(correct), int(nb))
    # generate_data("test.csv", 15, 1)
    
    # model = Model(num_fits = 5, seed = 200)
    
    # df_train = pd.read_csv("test_1_15.csv")

    # start = time()
    # model.fit(data = df_train)
    # end = time()
    # print("temps fit : "+str(end-start))
    
    # df0 = pd.read_csv("test_predict_0.csv")
    # df0.to_csv("test_1_15.csv", mode='a', index=False, header=False)
    # set_p_skill("p_bkt.csv",0,"carre2",0.1)
    
    # start = time()
    # predictions = model.predict(data = df0)
    # end = time()
    # print("temps predict : "+str(end-start))
    # print(predictions)
    
    # start = time()
    # model.partial_fit(data = df0)
    # end = time()
    # print("temps partial : "+str(end-start))
