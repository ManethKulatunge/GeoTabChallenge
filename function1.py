from gmplot import gmplot
import pickle
import mygeotab
import pandas as pd
def function1(device_id,from_date,to_date):
    with open('Authentication.obj', 'rb') as fp:
        api = pickle.load(fp)
    from_date=from_date+"T00:00:00.000Z"
    to_date=to_date+"T00:00:00.000Z"
    
    path_traversed = pd.DataFrame(api.get("LogRecord",search = {"fromDate": from_date,"toDate":to_date,"deviceSearch": {"id": device_id}}))
    path_traversed=path_traversed.sort_values(by=['dateTime'])
    
    df=path_traversed.drop_duplicates(subset=['latitude', 'longitude'])
    
    
    df_trips=pd.DataFrame(api.get("Trip", search = {"fromDate": from_date,"toDate":to_date,"deviceSearch": {"id":device_id}}))
    df_trips=df_trips.sort_values(by=['start','stop'])

    df['dateTime_con']=[i.value for i in df['dateTime']]
    df_trips['start_con']=[i.value for i in df_trips['start']]
    df_trips['stop_con']=[i.value for i in df_trips['stop']]
    df.to_csv('df.csv')
    df_trips.to_csv('df_trips.csv')
