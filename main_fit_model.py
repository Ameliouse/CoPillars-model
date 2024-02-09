import bkt
from pyBKT.models import Model
import pandas as pd

if __name__ == '__main__':
    # bkt.fit_model()
    
   
    # bkt.partial_fit_model(None,0,0,0)
    model = Model(num_fits = 5, seed = 40)
    model.load('model.pkl')
    print(model.params())
    model.partial_fit(data_path = 'data/all_data.csv', forgets = True, skills = '1')
    print(model.params())
    model.save('model.pkl')

    # df_train = pd.read_csv("data/all_data_0.csv")
    # dt_pred = model.predict(data=df_train)

    # model = bkt.partial_fit_model(model,10,0,1)

    
    # print(bkt.update_player(None,0,1,1))


    # bkt.partial_fit_model(None,0,0,1)
    # bkt.partial_fit_model(None,0,0,1)
    # bkt.partial_fit_model(None,0,0,1)

    # print(bkt.update_player(model,0,0,1))