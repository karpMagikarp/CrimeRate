from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os
from datetime import date
import math
import pickle
import sklearn
# from requests_html import HTMLSession
# from sample import func
lst=[]
model = pickle.load (open ('Model/model.pkl', 'rb')) 
app = Flask(__name__)
app.secret_key = os.urandom(24)

#getting headlines
# ses = HTMLSession()
# r = ses.get('https://www.indiatoday.in/crime')
# res=func(r)




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/home')
def dashboard():
    return render_template('home.html')


@app.route('/about')
def us():
    return render_template('about_us.html')

@app.route('/map')
def map():
    return render_template('test.html')

@app.route('/predict')
def predict():
    return render_template("predict.html")

@app.route('/result', methods =['POST'])
def result():
    city_names = { '0': 'Mumbai', '1': 'Pune', '2': 'Thane', '3': 'Nagpur'}
    
    crimes_names = { '0': 'Rape', '1': 'Criminal damage and arson', '2': 'Murder','3':'Assualt','4':'Theft'}
    
    population = { '0': 150.50, '1': 60.00, '2': 25.00, '3': 15.50, '4': 163.10}
    
    city_code = request.form["city"] 
    crime_code = request.form['crime'] 
    year = request.form['year'] 
    pop = population[city_code] 
    

    year_diff = int(year) - 2011;
    pop = pop + 0.1*year_diff*pop

    
    crime_rate = model.predict([[year, city_code, pop, crime_code]])[0] 
    
    city_name = city_names[city_code] 
    
    crime_type =  crimes_names[crime_code] 
    print(city_name,crime_type,year)
    if crime_rate <= 0.1:
        crime_status = "Very Low Crime Area" 
    elif crime_rate <= 0.5:
        crime_status = "Low Crime Area"
    elif crime_rate <= 1.0:
        crime_status = "High Crime Area"
    else:
        crime_status = "Very High Crime Area" 
    print(crime_rate,pop)
    cases = math.ceil((crime_rate) * pop)
    print(cases)
    
    return render_template('result.html', city_name=city_name, crime_type=crime_type, year=year, crime_status=crime_status, crime_rate=crime_rate, cases=cases, population=pop)

if __name__ == "__main__":
    app.run(debug=True)
