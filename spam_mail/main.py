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
#print mail_datas

##spliting train-test datas

X_mail=mail_datas["message"]
y_label=mail_datas.label

X_mail_train,X_mail_tester,y_mail_train,y_mail_tester=train_test_split(X_mail,y_label,random_state=1)

vect=CountVectorizer()
X_train_dtm=vect.fit(X_mail_train)

mail_train=vect.transform(X_mail_train)
#print mail_train.toarray()
datas=pd.DataFrame(mail_train.toarray(),columns=vect.get_feature_names())
train_examiner=vect.get_feature_names()
#print train_examiner[-50:]
X_train_mail_counts = np.sum(mail_train.toarray(), axis=0)

datas_sorted_by_counts=pd.DataFrame({'token':train_examiner, 'count':X_train_mail_counts}).sort('count')
#datas_sorted_by_counts



##SPAM_RATIO CALCULATING
mail_data_mapping=pd.DataFrame()
mail_datas['label'] = mail_datas.label.map({'ham':0, 'spam':1})



spam_mails=mail_datas[mail_datas.label==1] #spam mail code is 1
ham_mails=mail_datas[mail_datas.label==0]#ham mail code is 0


vect.fit(mail_datas.message)
all_tokens = vect.get_feature_names()



ham_dtm = vect.transform(ham_mails.message)
spam_dtm = vect.transform(spam_mails.message)


ham_counts = np.sum(ham_dtm.toarray(), axis=0)
spam_counts = np.sum(spam_dtm.toarray(), axis=0)
token_counts = pd.DataFrame({'token':all_tokens, 'ham':ham_counts, 'spam':spam_counts})

token_counts['ham'] = token_counts.ham + 1
token_counts['spam'] = token_counts.spam + 1


token_counts['spam_ratio'] = token_counts.spam / token_counts.ham
#print token_counts.sort('spam_ratio')
#print vect.transform(X_mail_train)

y_label=mail_datas['label']
X_mail_train,X_mail_tester,y_mail_train,y_mail_tester=train_test_split(X_mail,y_label,random_state=1)

mnb=MultinomialNB()

vect.fit(X_mail_train)

X_mail_train_matris=vect.fit_transform(X_mail_train)

#print X_mail_train_matris

mnb.fit(X_mail_train_matris.toarray(),y_mail_train)

X_test_dtm = vect.transform(X_mail_tester)

print X_test_dtm

#print mnb.predict(out_of_sample_data)
predicted_classes=mnb.predict(X_test_dtm)
print metrics.accuracy_score(y_mail_tester,predicted_classes)
