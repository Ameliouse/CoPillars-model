import pandas as pd
from typing import List
import random
import numpy as np
from pyBKT.models import Model


def generate_data(fileName : str, nb_player : int, skill_name : int) -> None:
    l_id = []
    l_skill = []
    l_win = []
    for i in range(0, nb_player):
        for n in range(0, random.randint(1,6)):
            win = random.randint(0,1)
            l_id.append(i)
            l_skill.append(skill_name)
            l_win.append(win)
        
    data = {"user_id" : l_id, "skill_name" : l_skill, "correct" : l_win}        
    df = pd.DataFrame(data)
    df.to_csv(fileName, index = False)
    return


# def create_csv_forBKT(fileName : str, nb_level : int, name_skill : List[str]) -> None:
#     df = pd.DataFrame(index = [i for i in range (0, nb_level)], columns = name_skill)
#     df.to_csv(fileName, index=False)
#     return 

    
def set_p_skill(fileName : str, skill_name : str, level : int, p : float) -> None :

    df = pd.read_csv(fileName)
    df.loc[level, skill_name] = p
    df.to_csv(fileName, index=False)
    return

if __name__ == '__main__':
    # generate_data("test.csv", 15, 1)
    df0 = pd.read_csv("test.csv")
    
    seq_length = round(len(df0) / len(df0["user_id"].unique()))
    df_train = (df0.groupby('user_id').apply(lambda x: x.iloc[:-1] if len(x)>1 else x).reset_index(drop=True)) #remove all but last element
    
    model = Model(num_fits = 5, seed = 200)
    print(model)
    model.fit(data = df_train)
    params = model.params
    print(params)
    predictions = model.predict(data = df0)
    print(predictions)