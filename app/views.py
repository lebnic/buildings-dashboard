import pandas as pd
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    url = 'http://donnees.ville.montreal.qc.ca/dataset/772087ee-e11f-42a8-ab6b-a175d6c6e249/resource/9d77d85a-f54c-408a-b6ff-3d847c05b2e0/download/sause01direction01directiondonneesouvertesbatimentsvacantsbatimentsvacantsvm2015.csv'
    buildings = pd.read_csv(url, sep = ',',encoding = "latin1")
    return render_template('index.html',
                          buildings=buildings)