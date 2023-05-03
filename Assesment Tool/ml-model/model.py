from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle

data2 = pd.read_csv('Static5.csv')
data2.drop(data2.iloc[:, 6:], inplace=True, axis=1)

labels = np.array(data2['FOS'])
data2 = data2.drop('FOS', axis=1)
data2 = np.array(data2)

x_train, x_test, y_train, y_test = train_test_split(data2, labels, test_size=0.20)
nn = MLPRegressor(random_state=5, max_iter=84)
nn.fit(x_train, y_train)

pickle.dump(nn, open('model.pkl', 'wb'))

print(nn.predict([19, 30, 26, 30, 38]))
