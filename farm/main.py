from flask import Flask,flash, render_template, request, redirect, url_for, session,Response,flash,jsonify,json,send_file
import numpy as np
import pandas as pd
import cgi
from typing import List
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your secret key'

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':

        #saving the file to extract data
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(secure_filename(file.filename))
        session['file'] = filename
        return redirect(url_for('predict'))

    return render_template("index.html",trigger=0)
@app.route('/per',methods=['POST','GET'])
def per():
    form = cgi.FieldStorage()
    search = form.getvalue('cmb1')
    return search
search = per()
@app.route('/predict',methods=['POST','GET'])
def predict():
    if 'file' in session:
        filename = session.get('file')
        df = pd.read_csv(filename)  # get the csv data
        cols = list(df)  # csv columns
        a=0
        list_ = ['S No', 'pH', 'Temperature', 'Moisture', 'Time_log', 'Gadget Id', 'Location']  # super list remains unchanged
        if (search=='clay'):
            a=35
        else:
            a=40
        ### Here the value is selected on the given data set nature and for more info refer this https://www.botanicare.com/hydro-101/temperature-and-humidity/
        if (cols == list_):
            df['target'] = np.where((df['Moisture']  >= a),'no_irrigation', 'irrigate')
            df = df.dropna()
            print(df)
            list_.append('target')
            df.to_csv('result.csv',index=False)
            return render_template("index.html", data=df, cols=list_, len=df.shape[0],trigger=1)
        else:
            return render_template("index.html", trigger=-1) #error code

    else:
        return render_template("index.html",trigger=0)

@app.route('/download',methods=['POST','GET'])
def download():
    path = "result.csv"
    return send_file(path, as_attachment=True)




if __name__ == "__main__":
    app.run(debug=True)