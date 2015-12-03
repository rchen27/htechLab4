# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:36:53 2015

@author: rchen27
"""
import re
import string
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

stop = stopwords.words("english")
stop= map(lambda x: x.encode('ascii','ignore'), stop)
words = []

def processString(line):
    line = line.rstrip()
    line = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', line)
    line = filter(lambda x: x in string.printable, line)
    line = line.replace('#', '')
    line = line.replace('depression', '')
    line = line.replace('depressed', '')
    #line = line.replace('rt', '')
    line = line.lower()
    split = line.split(' ')
    split = [word for word in split if '@' not in word]
    line = ' '.join(split) 
    line = ''.join([i for i in line if not i.isdigit()])
    line = line.translate(string.maketrans("",""), string.punctuation)
    split = line.split(' ')
    split = [word for word in split if word not in stop]
    split = [word for word in split if '@' not in word]
    #split = [word for word in split if 'rt' not in word]
    split = [''.join(sorted(set(word), key=word.index)) for word in split]
    st = LancasterStemmer()
    split = [str(st.stem(word.decode('utf-8'))) for word in split] 
    split = filter(None, split) 
    line = ' '.join(split) 
    return line

def createFeatureVectors(x_train, x_test):
    wordSet = set()
    for sample in x_train:
        for word in sample.split(' '):
            wordSet.add(word)
    global words
    words = list(wordSet)
    print len(words)
    trainFeatures = []
    for sample in x_train:
        feature = np.zeros(len(words))
        for word in sample.split(' '):
            ind = words.index(word)
            feature[ind] += 1
        trainFeatures.append(feature)
    testFeatures = []
    for sample in x_test:
        feature = np.zeros(len(words))
        for word in sample.split(' '):
            if word in words:
                ind = words.index(word)
                feature[ind] += 1
        testFeatures.append(feature)
    return np.array(trainFeatures), np.array(testFeatures)        

#post process data
def norm(x_train, x_test):
    
    for i in range(len(x_train)):
        x_train[i] = x_train[i] / np.linalg.norm(x_train[i], ord=2)
    for i in range(len(x_test)):
        x_test[i] = x_test[i] / np.linalg.norm(x_test[i], ord=2)
        if (np.any(np.isnan(x_test[i]))):
            x_test[i] = [0]*len(x_test[i])
    return x_train, x_test 
      
xs_pos = []
ys_pos = []
currUser = ''
for line in open ('finalDepUserTweets.txt'):
    if '=====' in line:
        xs_pos.append(currUser)
        ys_pos.append(1)
        currUser = ''
    else:
        currUser += ' ' + processString(line)

xs_neg = []
ys_neg = []
currUser = ''
for line in open ('finalNormUserTweets.txt'):
    if '=====' in line:
        xs_neg.append(currUser)
        ys_neg.append(0)
        currUser = ''
    else:
        currUser += ' ' + processString(line)


print len(xs_pos), len(xs_neg)

numPos = 35
numNeg = 50
x_train, y_train = xs_pos[:numPos] + xs_neg[:numNeg], ys_pos[:numPos] + ys_neg[:numNeg]
x_test, y_test = xs_pos[numPos:] + xs_neg[numNeg:], ys_pos[numPos:] + ys_neg[numNeg:]

#print len(x_train), len(y_train), len(x_test), len(y_test)

x_train, x_test = createFeatureVectors(x_train, x_test)
x_train, x_test = norm(x_train, x_test)

results = [0]*6

for i in range(10):

    model = GaussianNB()
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    results[0] += score
    print 'Naive Bayes', score
    
    neigh = KNeighborsClassifier(n_neighbors=6)
    neigh.fit(x_train, y_train)
    score = neigh.score(x_test, y_test)
    results[1] += score
    print 'KNN', score
    
    logreg = linear_model.LogisticRegression()
    logreg.fit(x_train, y_train)
    score = logreg.score(x_test, y_test)
    results[2] += score
    print 'Logistic Regression' , score
    
    mostWeighted = []
    maxes = np.argpartition(logreg.coef_[0], -30)[-30:]
    for i in range(len(maxes)):
        mostWeighted.append(  (words[maxes[i]].encode('ascii','ignore'), logreg.coef_[0][maxes[i]]))
    #print mostWeighted
    
    model = DecisionTreeClassifier(max_depth=11)
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    results[3] += score
    print 'Decision Tree', score
    
    mostWeighted = []
    maxes = np.argpartition(np.array(model.feature_importances_), -30)[-30:]
    for i in range(len(maxes)):
        mostWeighted.append(  (words[maxes[i]].encode('ascii','ignore'), model.feature_importances_[maxes[i]]))
    #print mostWeighted
    
    
    model = SVC(gamma=2, C=1)
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    results[4] += score
    print 'SVC', score
    
    scores = []
    params = []
    for t in range(1, 20, 2):
        for d in range(1, 20, 5):
            model = RandomForestClassifier(max_depth=d, n_estimators=t)
            model.fit(x_train, y_train)
            scores.append(model.score(x_test, y_test))
            params.append((t, d))
    ind = scores.index(max(scores))
    results[5] += max(scores)
    print 'Random Forest', scores[ind], params[ind]
    model = RandomForestClassifier(max_depth=params[ind][1], n_estimators=params[ind][0])
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    print 'Random Forest', score
    
    mostWeighted = []
    maxes = np.argpartition(np.array(model.feature_importances_), -30)[-30:]
    for i in range(len(maxes)):
        mostWeighted.append( (words[maxes[i]].encode('ascii','ignore'), model.feature_importances_[maxes[i]]))
    #print mostWeighted
    
results = [x/10.0 for x in results]
print results
N = 6
plt.rcParams.update({'font.size': 20})
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, results, width, color='b')


# add some text for labels, title and axes ticks
ax.set_ylabel('Percentage Correct')
ax.set_title('Test Accuracies of Each Classifier')
ax.set_xticks(ind + width/2)
ax.set_xticklabels(('Naive Bayes', '5-NN', 'Logistic Regression','Decision Tree', 'SVC', 'Random Forest'))
plt.ylim([.5, .85])


plt.show()
fig.set_size_inches(17.5, 9.5)
fig.savefig('results.png', dpi=100)
'''
Prints the percentage of people in x_test that we diagnose with depression
'''
def predictDepression(x_train, x_test, y_train, y_test):
    model = SVC(gamma=2, C=1)
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    print 'SVC', score
    pred = list(model.predict(x_test))
    print float(pred.count(1)) / len(x_test)

predictDepression(x_train, x_test, y_train, y_test)
