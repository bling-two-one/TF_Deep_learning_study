import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv('C:\\Users\\User\\Desktop\\github\\080263-master\\080263-master\\chap3\\iris.data')

X = dataset.iloc[:, : -1].values

