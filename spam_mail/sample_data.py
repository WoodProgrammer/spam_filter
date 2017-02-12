#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


cols=["label","message"]
mail_datas=pd.read_table("text_data.tsv",names=cols)

vect=CountVectorizer()

X_mail_train,X_mail_tester,y_mail_train,y_mail_tester=train_test_split(mail_datas.message,mail_datas.label,random_state=1)

mnb=MultinomialNB()

#vect.fit(X_mail_train)

X_mail_train_matris=vect.fit_transform(X_mail_train)
print X_mail_train_matris.toarray()
mnb=MultinomialNB()
mnb.fit(X_mail_train_matris.toarray(),y_mail_train)
print mnb.predict(X_mail_tester)


x=["Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's abacvdqwevs"]
vect=CountVectorizer()
data=vect.fit_transform(x)
