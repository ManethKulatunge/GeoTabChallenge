import mygeotab
import json
import pickle

def authenticate(username,password,database):
    api = mygeotab.API(username, password, database)
    credentials=api.authenticate()
    with open('Authentication.obj', 'wb') as fp:
        pickle.dump(api, fp)

    
