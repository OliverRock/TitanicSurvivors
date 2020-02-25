import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder


class KNNTitanic:
    data = pd.read_csv("data/titanic.csv")
    data = data[["Survived", "Sex", "Age", "Fare"]]

    LE = LabelEncoder()
    data["Sex"] = LE.fit_transform(data["Sex"])

    data = data.fillna(data.mean())

    X = data[["Age", "Fare", "Sex"]]
    y = data['Survived']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    knn = KNeighborsClassifier(n_neighbors=7)

    knn.fit(X_train, y_train)

    scoreOntrianing = knn.score(X_train, y_train)

    scoreontestdata = knn.score(X_test, y_test)

    print("accuracy: " + str(scoreontestdata))

    """male = 1
    female = 0
    
    age = 22
    ticket_price = 7.25
    sex = female
    
    
    result = knn.predict(np.array([[age, ticket_price, sex]]))"""

    def predict(self, age, ticket_price, sex):
        result = KNNTitanic.knn.predict(np.array([[age, ticket_price, sex]]))
        if result == 1:
            return "Survive"
        else:
            return "Die"
