from flask import Flask, render_template, redirect, request
import numpy as np
import pandas as pd
from pycaret.regression import *

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

sih_model = load_model('model')

@app.route('/', methods = ['POST'])

def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        
        def relia(pv1, pi1, t1, a1, w1):    
            sd_v,sd_i,sd_t,sd_w,sd_age,a_v,a_i,a_t,a_w,a_age = 14.450315,1.184078,14.724061,11.850687,3,425.041214,10.004947,55.033790,99.990990,5        
            
            reliabilty = 5
            if pv1 > a_v + 1.2*sd_v:
                reliabilty -=1
            if pi1 > a_i + 1.2*sd_i:
                reliabilty -=1
            if t1 > a_t + 1.2*sd_t:
                reliabilty -=1
            if w1 > a_w + 1.2*sd_w:
                reliabilty -=1
            if a1 > a_age + sd_age:
                reliabilty -=1

            if reliabilty == 5:
                return 'Highly Reliable'
            if reliabilty == 3 or reliabilty == 4:
                return 'Moderately Reliable'
            if reliabilty == 1 or reliabilty == 2:
                return 'Less Reliable'
            if reliabilty == 0:
                return 'Not Reliable'
        
        pv1 = to_predict_list['voltage']
        pi1 = to_predict_list['current']
        po1 = to_predict_list['poles']
        f1 = to_predict_list['frequency']
        pf1 = to_predict_list['cosq']
        t1 = to_predict_list['temperature']
        l1 = to_predict_list['load']
        w1 = to_predict_list['angvel']
        a1 = to_predict_list['age']
        
        if len(pv1)==0:
           pv1 = 425.041214
        if len(pi1)==0:
            pi1 = 10.004947
        if len(po1)==0:
            po1 = 3
        if len(f1)==0:
            f1 = 50
        if len(pf1)==0:
            pf1 = 0.650188
        if len(t1)==0:
            t1 = 55
        if len(l1)==0:
            l1 = 85
        if len(w1)==0:
            w1 = 100
        if len(a1)==0:
            a1 = 5
            
        pv1 = float(pv1)
        pi1 = float(pi1)
        po1 = float(po1)
        f1 = float(f1)
        pf1 = float(pf1)
        t1 = float(t1)
        l1 = float(l1)
        w1 = float(w1)
        a1 = float(a1)
        
        pv,pi,po,f,pf,t,l,w,a= [pv1],[pi1],[po1],[f1],[pf1],[t1],[l1],[w1],[a1]
        df = pd.DataFrame(list(zip(pv,pi,po,f,pf,t,l,w,a)),columns = ['3 Phase Voltage in Volts','3 Phase Current in Amps','Poles','Frequency in Hz','Power Factor','Temperature in Celcius','% Load','Angular Velocity in rad/sec','Motor Age in Yrs'])
       
        pred_new = predict_model(sih_model,data=df)
        print(pred_new.head())
        r = relia(pred_new['3 Phase Voltage in Volts'][0],pred_new['3 Phase Current in Amps'][0],pred_new['Temperature in Celcius'][0],pred_new['Motor Age in Yrs'][0],pred_new['Angular Velocity in rad/sec'][0])
        e = pred_new['Label'][0]
        c = 0
        ctr = round(50 - (3500/e),0)
        if ctr < 0 : ctr = 0
        c = abs(ctr)
        
        return ("Effeciency: "+str(e)+"%\nReliability: "+str(r)+"\nLife Cyle: "+str(int(c))+" Years")
        
    return render_template("index.html", result = result)

if __name__ == '__main__':
	#app.debug = True
	app.run(debug = True)
