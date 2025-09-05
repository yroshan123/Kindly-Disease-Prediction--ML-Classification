# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report 

def ep(sarr):
    # Importing the dataset
    df = pd.read_csv('Data.csv')
    df=df.replace('?',np.nan)
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
    from sklearn.preprocessing import LabelEncoder
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
    #Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    # Fitting Random Forest Classification to the Training set
    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    acc = accuracy_score(y_test,y_pred)
    conf = confusion_matrix(y_test,y_pred)
    y_out = classifier.predict(sarr)
    print(y_out)
    if y_out == 0:
        st = []
        st.append("Accuracy is"+str(acc))
        st.append("Confusion matrix is\n"+str(conf))
        st.append("The patient doesn't have Chronic Kidney Disease")
        return st
    else:
        st = []
        st.append("Accuracy is"+str(acc))
        st.append("Confusion matrix is\n"+str(conf))
        st.append("The patient has a chance of Chronic Kidney Disease")
        return st