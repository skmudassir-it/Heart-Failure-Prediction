from flask import Flask, redirect, render_template, request, url_for
import joblib
app = Flask(__name__)
solve = joblib.load('model')

@app.route('/', methods=['POST','GET'])
def home():
    sol = ''
    if request.method == 'POST':
        Age = float(request.form.get('age'))
        Sex = int(request.form.get('sex'))
        ChestPain = int(request.form.get('cpt'))
        BP = float(request.form.get('bp'))
        Chol = float(request.form.get('chol'))
        Sugar = int(request.form.get('sugar'))
        ECG = int(request.form.get('ecg'))
        MHR = float(request.form.get('mhr'))
        Angina = int(request.form.get('ae'))
        Oldpeak = float(request.form.get('st'))
        Slope = int(request.form.get('slope'))
        m = [[Age,Sex,ChestPain,BP,Chol,Sugar,ECG,MHR,Angina,Oldpeak,Slope]]
        sol = solve.predict(m)
    return render_template('index.html',result = sol)



if __name__ == '__main__':
    app.run(debug = True)
