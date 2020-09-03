import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")
mydata = pd.read_csv("nba_2018_teamstats.csv", sep=",")

print(mydata.head())

