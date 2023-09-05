import json

from flask import Flask
import numpy as np
import pandas as pd
from numpy.random import randn

app = Flask(__name__)

@app.route('/')
def main():
    array = np.arange(1,21)
    array = array.reshape(5,4)
    series_1 = pd.DataFrame(array, ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
    # series_1 = pd.Series(randint(1,100),['A','B','C','D'],['W','X','Y','Z'])
    return series_1.to_html(classes='data')

if __name__ == '__main__':
    app.run(debug=True)