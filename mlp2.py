from datetime import datetime
startTime = datetime.now()
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
# Importing the dataset
df = pd.read_csv('Data.csv')
df=df.replace('?',np.nan)

#df=df.dropna(subset=['rbc','pc','pcc','ba','htn','dm','cad','appet','pe','ane','class'])
X =df.iloc[:, :-1].values
Y = df.iloc[:, 24].values

#missing values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 0:14])
X[:,0:14] = imputer.transform(X[:,0:14])
x=pd.DataFrame(X)
y=pd.DataFrame(Y)
x=x.replace(np.nan,'nun')
y=y.replace(np.nan,'nun')
X=np.array(x)
Y=np.array(y)


# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
for i in range(14,24):
 X[:, i] = labelencoder_X.fit_transform(X[:, i])
x=pd.DataFrame(X)

# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
Y = labelencoder_y.fit_transform(Y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)
print("---------------------------------------------------------")
print("Shape of training data: ", X_train.shape)
print("Shape of test data    : ", X_test.shape )
print("---------------------------------------------------------")

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Multi-layer perceptron to the Training set
from sklearn.neural_network import MLPClassifier
clf=MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(5, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=100, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5,
       random_state=1, shuffle=True, solver='lbfgs', tol=0.0001,
       validation_fraction=0.1, verbose=False, warm_start=False)
#MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5,2),random_state=1)
print(clf.fit(X_train,y_train))
clf.classes_

print("weights between input and first hidden layer:")
print(clf.coefs_[0])
print("\nweights between first hidden and second hidden layer:")
print(clf.coefs_[1])
print("\n wights between second hidden layer and output layer:")
print(clf.coefs_[2])

print("Generalising access to each neuron")
#generalising access to each neuron
for i in range(len(clf.coefs_)):
    number_neurons_in_layer = clf.coefs_[i].shape[1]
    for j in range(number_neurons_in_layer):
        weights = clf.coefs_[i][:,j]
        print("i,j,weight vector of H(i,j)")
        print(i, j, weights, end=", ")
        print()
    print()
    
#bias values
print("Bias values for first hidden layer:")
print(clf.intercepts_[0])
print("\nBias values for second hidden layer:")
print(clf.intercepts_[1])

import numpy as np
from matplotlib import pyplot as plt
npoints = 50
X, Y = [], []
# class 0
X.append(np.random.uniform(low=-2.5, high=2.3, size=(npoints,)) )
Y.append(np.random.uniform(low=-1.7, high=2.8, size=(npoints,)))

# class 1
X.append(np.random.uniform(low=-7.2, high=-4.4, size=(npoints,)) )
Y.append(np.random.uniform(low=3, high=6.5, size=(npoints,)))
learnset = []
learnlabels = []
for i in range(2):
    # adding points of class i to learnset
    points = zip(X[i], Y[i])
    for p in points:
        learnset.append(p)
        learnlabels.append(i)
        
from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(20, 3), max_iter=150, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)
mlp.fit(learnset, learnlabels)
print("Training set score: %f" % mlp.score(learnset, learnlabels))
print("Test set score: %f" % mlp.score(learnset, learnlabels))
mlp.classes_


#predictions
predictions = clf.predict(X_test)
print(predictions) 

# printing all the evaluation metrics
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report    
print(confusion_matrix(y_test,predictions))
print(accuracy_score(y_test, predictions))
print(classification_report(y_test,predictions))

