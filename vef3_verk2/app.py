import os
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('default.html')

@app.route('/kt-sida/<kt>')
def ktsida(kt):
    summa = 0
    for item in kt:
        summa = summa + int(item)
    return render_template('kt-sum.html', kt = kt, summa = summa)

frettir = [
    ['0','21 lát­inn eft­ir eld­gosið á Nýja-Sjálandi','Alls er 21 lát­inn eft­ir að eld­fjall á Hvítu­eyju á Nýja-Sjálandi gaus í des­em­ber.'],
    ['1','Lög­reglumaður ákærður fyr­ir morð',' Lög­reglumaður í Mary­land-ríki hef­ur verið ákærður fyr­ir morð en hann skaut mann til bana á mánu­dags­kvöldið. Maður­inn var í járn­um inni í lög­reglu­bíl þegar Michael Owen skaut hann sjö sinn­um.'],
    ['2','131 lát­inn og yfir 5.500 smitaðir',' Dauðsföll­um af völd­um kór­óna­veirunn­ar held­ur áfram að fjölga'],
]
@app.route('/frettir')
def frettir():
    return render_template('frettir.html', frettir=frettir)

@app.route('/frett/<int:id>')
def frett(id):
    return render_template('frett.html', frett=frettir[id], nr=id)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

if __name__ == '__main__':
    app.run(debug=True)