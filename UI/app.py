from flask import Flask, render_template, redirect, request

# from sklearn.externals import joblib

# import sklearn.external.joblib as extjoblib
import joblib

#__name__ == __main__
app = Flask(__name__)



@app.route('/')
def hello():
	return render_template("index.html")

# model = joblib.load("model.pkl")

def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 9)
    model = joblib.load("model.pkl") 
    result = loaded_model.predict(to_predict)
    return result[0] 


@app.route('/', methods = ['POST'])
def result():
	if request.method == 'POST':
		to_predict_list = request.form.to_dict()
		to_predict_list = list(to_predict_list.values()) 
		to_predict_list = list(map(int, to_predict_list)) 
		result = ValuePredictor(to_predict_list)

	return render_template("index.html", result = result)

if __name__ == '__main__':
	#app.debug = True
	app.run(debug = True)