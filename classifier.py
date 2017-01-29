import numpy as np
import csv
import pandas as pd

from numpy import genfromtxt
label_stat=[]
def get_spam_stat():
    mail_data = pd.read_csv("spam_data.csv", index_col=0)
    return mail_data["stat"]
'''

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()

clf.fit(X, Y)

print(clf.predict([[3, 2]]))

clf_pf = GaussianNB()

clf_pf.partial_fit(X, Y, np.unique(Y))

print(clf_pf.predict([[-0.8, -1]]))
'''
print(get_spam_stat())
