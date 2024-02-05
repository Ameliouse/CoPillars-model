import sys
import time
import pandas as pd

from pyBKT.models import Model


def update_player(user_id : int, skill_id : int, correct : int, fileName_model : str = "data/all_data.csv") :
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
    model = Model(num_fits = 5, seed = 200)
    df_train = pd.read_csv(fileName_model)
    print("fit the model...")   
    model.fit(data = df_train)
    # print("temps fit model : "+str(end-start))
    # model.save('model.pkl')
    
    v = {"user_id" : [user_id], "skill_name" : [skill_id], "correct" : [correct]}
    dt_v = pd.DataFrame(data=v)

    #predict p success
    dt_pred = model.predict(data=dt_v)
    return dt_pred

if __name__ == '__main__':
    print(update_player(0, 1, 0))
    # time.sleep(5)