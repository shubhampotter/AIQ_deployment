from flask import Flask, render_template, url_for, request

import pandas as pd
import pickle

# load the model
model=pickle.load(open("random_forest_regression_model.pkl","rb"))

app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv('real_2017.csv')
    my_prediction=model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html', prediction=my_prediction)




if __name__=='__main__':
    app.run(debug=True)