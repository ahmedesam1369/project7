
from unicodedata import name
import numpy as np
import joblib
import traceback
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/name",methods=['GET' , 'POST'])
def get_current_user():
    x=jsonify({"name":"soad"})
    lr = joblib.load("model.pkl")      
    if request.method == "GET":
        return x
    elif request.method == "POST":
        return "postttt"
# GET requests will be blocked
@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']
    print("The language value is: {}".format(language))

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


@app.route("/", methods=['GET'])
def hello():
    return "hey"

@app.route('/Mypredict', methods=['POST'])
def Mypredict():
    ir=joblib.load("model.pkl")
    if ir :
        try:
            json=request.get_json()
            temp=list(json[0].values())
            vals=np.array(temp).reshape((1,-1))
            prediction=ir.predict(vals)
            return jsonify({'prediction': str(prediction[0])})
        except:
            return jsonify({'prediction': str(prediction[0])})
    else:
        return ('No model here to use')       

@app.route('/predict', methods=['POST'])
def predict():
	lr = joblib.load("model.pkl")
	if lr:
		try:
			json = request.get_json() 
			temp=list(json[0].values())
			prediction = lr.predict(temp)
			print("here:",prediction)     
			return jsonify({'prediction': str(prediction[0])})

		except:        
			return jsonify({'trace': traceback.format_exc()})
	else:
		return ('No model here to use')

if __name__ == '__main__':
    app.run(debug=True)    