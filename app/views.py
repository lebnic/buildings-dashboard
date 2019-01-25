import pandas as pd
from flask import render_template
from app import app
import numpy as np

@app.route('/')
@app.route('/index')
def index():
    url = 'http://donnees.ville.montreal.qc.ca/dataset/772087ee-e11f-42a8-ab6b-a175d6c6e249/resource/886bdfe0-3946-413c-8dff-9c82ee9631c1/download/batimentsvacants2016.csv'
    buildings = pd.read_csv(url, sep = ',',encoding = "latin1")
    buildings['VALEUR_TOTAL'] = buildings['VALEUR_TER']+buildings['VALEUR_TER']
    buildings = buildings.replace(np.nan,' ', regex=True)
    return render_template('index.html',
                          buildings=buildings)