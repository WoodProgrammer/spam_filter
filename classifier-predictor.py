import numpy as np
import csv
import pandas as pd
from sklearn.naive_bayes import GaussianNB


label_stat=[]
def get_spam_stat():
    df = pd.read_csv('spam_data.csv', index_col='id')
    return df,df["stat"]


X , Y = get_spam_stat()


clf = GaussianNB()

clf.fit(X, Y)

print(clf.predict([[0,0,0,0,1,1]]))

clf_pf = GaussianNB()

clf_pf.partial_fit(X, Y, np.unique(Y))
'''
print(clf_pf.predict([[-0.8, -1]]))
'''
print X
