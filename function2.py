import mygeotab
import json
import pandas as pd
from gmplot import gmplot
def function2(num):
    df=pd.read_csv('df.csv')
    df_trips=pd.read_csv('df_trips.csv')
    #print(df_trips.head())
    df_singletrip=df[df['dateTime_con'].between(df_trips.start_con[num],df_trips.stop_con[num], inclusive=True)]
    #print(df_trips.start_con[0:5])
    #print(df_trips.stop_con[num])
    print("coming here")
    #last_loc=df_trips.loc[num,'stopPoint']
    #print(last_loc)
    print("after there")
    coordinates=df_singletrip[['latitude','longitude']]
    coordinate_tuples = [tuple(x) for x in coordinates.values]
    #coordinate_tuples.append((last_loc['y'],last_loc['x']))
    gmap = gmplot.GoogleMapPlotter(coordinate_tuples[0][0],coordinate_tuples[0][1] , 13)
    golden_gate_park_lats, golden_gate_park_lons = zip(*coordinate_tuples)
    gmap.plot(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', edge_width=5)
    gmap.draw("geomap_routes.html")
