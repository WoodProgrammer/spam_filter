from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

mnba=MultinomialNB()
x=["Free entry in 2 a wkly comp to win FA Cup", "final tkts 21st May 2005. Text FA" ,"to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's","abacvdqwevs"]
y = np.array([1, 2, 3, 4])
vect=CountVectorizer()
x_train=vect.fit(x)
data=vect.fit_transform(x)

print x
print data.toarray()
mnba.fit(data.toarray(),y)
print mnba.predict(data[0])
'''
import numpy as np
X = np.random.randint(5, size=(6, 100))
y = np.array([1, 2, 3, 4, 5, 6])
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X, y)
print X[0]
print(clf.predict(X[0]))
'''
