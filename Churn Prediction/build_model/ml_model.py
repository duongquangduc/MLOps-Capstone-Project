# import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pickle

# preprocessing data
training_data = pd.read_csv('churnpredictiondata.csv')
training_data.describe()

X = training_data.iloc[:, :-1].values
y = training_data.iloc[:, -1].values


# split training testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# minkowski is for ecledian distance
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)

# model training
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
y_prob = classifier.predict_proba(X_test)[:,1]

cm = confusion_matrix(y_test, y_pred)
print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

# model predictions
new_prediction = classifier.predict(sc.transform(np.array([[10,200]])))
new_prediction_proba = classifier.predict_proba(sc.transform(np.array([[40,20000]])))[:,1]

new_pred = classifier.predict(sc.transform(np.array([[200,50000]])))
new_pred_proba = classifier.predict_proba(sc.transform(np.array([[42,50000]])))[:,1]

# saving models
model_file = "classifier.pickle"
pickle.dump(classifier, open(model_file,'wb'))
scaler_file = "sc.pickle"
pickle.dump(sc, open(scaler_file,'wb'))
