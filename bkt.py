import pandas as pd
import os
import sys
from time import time
from time import sleep

from typing import List
from pyBKT.models import Model

import utils as ut

def fit_model(fileName_model : str = "data/all_data.csv") -> Model:
    """at the start of the game fit the model 

    Args:
        fileName_model (str, optional): _description_. Defaults to "data/all_data.csv".

    Returns:
        Model: the model
    """
    model = Model(num_fits = 5, seed = 200)
    df_train = pd.read_csv(fileName_model)
    print("fit the model...")   
    start = time()
    model.fit(data = df_train)
    end = time()
    print("temps fit model : "+str(end-start))
    model.save('model.pkl')
    return model

def partial_fit_model(model : Model, user_id : int, skill_id : int, correct : int, fileName_load_model : str = "model.pkl") -> None :
    """partial fit the model

    Args:
        model (Model): the model
        user_id (int): player id
        skill_id (int): skill id
        correct (int): 0 if fail else 1
        
    Returns:
        None
    """
    
    if model == None:
        model = Model(num_fits = 5, seed = 200)
        model.load(fileName_load_model)
    
    v = {"user_id" : [user_id], "skill_name" : [skill_id], "correct" : [correct]}
    dt_v = pd.DataFrame(data=v)

    #partial fit model
    
    model.partial_fit(data=dt_v)
    # model.save(fileName_load_model)
    return model
    
def update_player(model : Model, user_id : int, skill_id : int, correct : int, fileName_prob : str = None, fileName_model : str = "data/all_data.csv", fileName_load_model : str = "model.pkl") -> int :
    """update the probability of the skill for the player after a success or a fail
        and update the model

    Args:
        model (Model): the model
        user_id (int): player id
        skill_id (int): skill id
        correct (int): 0 if fail else 1
        fileName_prob (str, optional): _description_. Defaults to "data/all_p.csv".
        fileName_model (str, optional): _description_. Defaults to "data/all_data.csv".
        
    Returns:
        int: 0 if under the limit else 1
    """
    #load the model if var model empty

    if model == None:
        model = Model(num_fits = 5, seed = 200)
        model.load(fileName_load_model)
        
    if fileName_prob != None :
        fileName_prob = fileName_prob + "data/all_data_"+str(user_id)+".csv"
    else:
        fileName_prob = "data/all_data_"+str(user_id)+".csv"
        
    v = {"user_id" : [user_id], "skill_name" : [skill_id], "correct" : [correct]}
    dt_v = pd.DataFrame(data=v)
    
    # Vérifier si le fichier existe
    if os.path.isfile(fileName_prob):
        # Si le fichier existe, append les données
        dt_v.to_csv(fileName_prob, mode='a', header=False, index=False, lineterminator='\n')
    else:
        # Si le fichier n'existe pas, créez-le et écrivez les données
        dt_v.to_csv(fileName_prob)
        
    #add to the model file v
    # dt_v.to_csv(fileName_model, mode='a', index=False, header=False, lineterminator='\n')

    #predict p success
    dt_pred = model.predict(data_path=fileName_prob)

    p_success = dt_pred.iloc[-1, dt_pred.columns.get_loc("state_predictions")]
    #set p success
    # ut.set_p_skill(fileName_prob, user_id, ut.MECA[skill_id], p_success)
    # dt_pred[dt_pred['skill_name'] == '0']
    return p_success
    
# def no_skills(user_id : int, fileName_prob : str = "all_p.csv") -> List[int]:
#     df = pd.read_csv(fileName_prob)
#     df.loc[user_id]
#     if p < ut.LIMIT:
#         return False
#     else:
#         return True
    
# if __name__ == '__main__':
#     model = fit_model()
#     print(update_player(model, 0, 1, 1))

if __name__ == '__main__':    
    # model = fit_model()
    # model = Model(num_fits = 5, seed = 200)
    # model.load('model.pkl')
    if len(sys.argv) != 6:
        print("pb nb paramètres")
        sys.exit(1)

    # Récupérer les arguments de la ligne de commande
    user_id = sys.argv[1]
    skill_id = sys.argv[2]
    correct = sys.argv[3]
    path = sys.argv[4]

    # df_train = pd.read_csv(path)

    print(update_player(None, int(user_id), int(skill_id),int(correct), fileName_prob = path, fileName_model=path+"data/all_data.csv", fileName_load_model=path+"model.pkl"))