from flask import Flask,request,jsonify
from http import HTTPStatus as status
from authentication import authenticate



app = Flask(__name__)


@app.route('/geotab/authenticate',methods=['GET','POST'])
def authenticate_client():
    req=request.json
    server=req['server']
    username=req['userName']
    password=req['password']
    database=req['database']
    authenticate(username,password,database)
    return jsonify({'result':'success'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug= True, port=5000)
