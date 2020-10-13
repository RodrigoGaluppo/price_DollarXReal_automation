from flask import Flask,jsonify,request
from Searcher import DolarSearcher

app = Flask(__name__)

#calling the searcher
searcher = DolarSearcher()
searcher.Start()

# building the request 
@app.route("/price/dolar",methods=['GET'])
def get_dolar_price(): 
    return jsonify({"price":searcher.dolarPrice})

if __name__ == '__main__':
    app.run()