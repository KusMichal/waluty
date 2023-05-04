from flask import Flask,redirect,render_template,request 
import requests, csv
app = Flask(__name__)


responde = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = responde.json()
rates = data[0]['rates']

with open ('dane.csv',newline='') as dane:
    reader = csv.reader(dane,delimiter=';')
    for row in dane:
        rates
def calculator(currency, number):
    number = int(number)
    for rate in rates:
        values = [rate["currency"], rate["code"],rate["ask"]]
        if values[0] == currency:
            return round((number * rate["ask"]),2)



@app.route("/", methods=["GET", "POST"])
def currency():
    if request.method=='POST':
        currency=request.form.get('currency')
        number=float(request.form.get('number'))
        ask = calculator(currency, number)
        return render_template("calculator.html", ask=ask)
    elif request.method=='GET':
        return render_template("calculator.html")
