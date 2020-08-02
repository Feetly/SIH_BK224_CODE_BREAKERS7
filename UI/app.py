from flask import Flask, render_template, redirect, request

import numpy as np
# from sklearn.externals import joblib

# import sklearn.external.joblib as extjoblib
import joblib
import pickle
import xgboost as xgb

#__name__ == __main__
app = Flask(__name__)

# booster.save_model('model.pkl')

@app.route('/')
def hello():
	return render_template("index.html")

# model = joblib.load("model.pkl")
bst = xgb.Booster()
model = bst.load_model('model.pkl')

# def ValuePredictor(to_predict_list): 
#     to_predict = np.array(to_predict_list).reshape(1, 9)
#     model = joblib.load("model.pkl") 
#     print(model)
#     result = model.predict(to_predict)
#     print(result[0])
#     return result[0] 


# with open(f'model/model.pkl', 'rb') as f:
#     model = pickle.load(f)


@app.route('/', methods = ['POST'])
def result():
	if request.method == 'POST':
		to_predict_list = request.form.to_dict()
		list1 = []
		list1.append(float(to_predict_list['voltage']))
		list1.append(float(to_predict_list['current']))
		list1.append(float(to_predict_list['poles']))
		list1.append(float(to_predict_list['frequency']))
		list1.append(float(to_predict_list['cosq']))
		list1.append(float(to_predict_list['temperature']))
		list1.append(float(to_predict_list['load']))
		list1.append(float(to_predict_list['angvel']))
		list1.append(float(to_predict_list['age']))
		# to_predict_list = list(to_predict_list.values())
		# to_predict_list = list(map(float, to_predict_list)) 
		# result = ValuePredictor(to_predict_list)
		# return 'hello'
		print (list1)
		to_predict = np.array(list1).reshape(1, 9)
		print (to_predict)
		# model = joblib.load("model.json") 
		# model = pickle.load(open("model.json", "rb"))
		# print(model)
		result = model.predict(to_predict)
		# print(result[0])
		return result[0] 

	return render_template("index.html", result = result)

if __name__ == '__main__':
	#app.debug = True
	app.run(debug = True)
