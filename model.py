import pandas as pd 
import numpy as np

def get_data():
    data = pd.read_csv('data/2018-personality-data.csv')
    ratings = pd.read_csv('data/2018_ratings.csv')
    
    return 'Main data \n{}\nRatings Data\n{}'.format(data, ratings)

print(get_data())