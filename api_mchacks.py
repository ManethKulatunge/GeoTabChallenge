from flask import Flask,request,jsonify
from authentication import authenticate
from function1 import function1
from function2 import function2
from flask_cors import CORS, cross_origin
import logging
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/geotab/authenticate',methods=['GET','POST'])
def authenticate_client():
    req=request.json
    print("i am here")
    server=req['server']
    username=req['userName']
    password=req['password']
    database=req['database']
    authenticate(username,password,database)
    return jsonify({'result':'success'})

@app.route('/geotab/function1',methods=['GET','POST'])
@cross_origin()
def function1_launcher():
    logging.debug('Yo')
    req=request.json
    device_id=req['device_id']
    from_date=req['from_date']
    to_date=req['to_date']
    function1(device_id,from_date,to_date)
    return jsonify({'result':'success'})

@app.route('/geotab/function2',methods=['GET','POST'])
def function2_launcher():
    req=request.json
    route_num=req['num']
    function2(route_num)
    return jsonify({'result':'success'})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5009)



