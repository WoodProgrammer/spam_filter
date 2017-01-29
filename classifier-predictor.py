import numpy as np
import csv
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import re



def dict_creator_miner(file_url):

    default_word_dict={'money': 0, 'guaranteed': 0, 'free': 0, 'subscribe': 0, 'girl': 0}
    word_dict={'money': 0, 'guaranteed': 0, 'free': 0, 'subscribe': 0, 'girl': 0}
    datas=[]
    with open(file_url) as f:
        content = f.readlines()

    for line in content:

        for key in word_dict:
            if key=="id":
                word_dict["id"]=id
            elif key=="stat":
                word_dict["stat"]=stat
            else:
                money_match=re.search( r"{0}".format(key), line, re.M|re.I)
                if money_match:
                    word_dict[key]+=1
                else:
                    pass


    for keys in word_dict.keys():
        datas.append(word_dict[key])

    return datas




label_stat=[]
def get_spam_stat():
    df = pd.read_csv('spam_data.csv', index_col='id')
    return df,df["stat"]


X , Y = get_spam_stat()


clf = GaussianNB()

clf.fit(X, Y)

x=np.array(dict_creator_miner("example.txt"))
print x
print(clf.predict([[x]]))

clf_pf = GaussianNB()

clf_pf.partial_fit(X, Y, np.unique(Y))
'''
print(clf_pf.predict([[-0.8, -1]]))
'''
