from flask import Flask,jsonify,request
from flask_cors import CORS
from Searcher import DolarSearcher
import os

app = Flask(__name__)

cors = CORS(app,resource={r"/*":{"origns":"*"}})

#calling the searcher
searcher = DolarSearcher()
searcher.Start()

@app.route("/price/dolar",methods=['GET'])
def get_dolar_price(): 
    return jsonify({"price":searcher.dolarPrice})

def main():
    PORT = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=PORT)

"""
# building the request 
@app.route("/price/dolar",methods=['GET'])
def get_dolar_price(): 
    return jsonify({"price":searcher.dolarPrice})
"""

if __name__ == '__main__':
    main()