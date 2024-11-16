from flask import *

foods = [{'id':1,'name':'pizza','price':60.0},
    {'id':2,'name':'sushi','price':38.0},
    {'id':3,'name':'flafel','price':28.0}]

app = Flask(__name__)

@app.get('/')
def get_all_foods():
    return foods
    
if __name__== '__main__':
    app.run(port=8070,host='0.0.0.0')