import pandas as pd
import matplotlib.pyplot as plt
import time as t

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier


# pavlos nikou
# st026276
# Lab08

def ExploratoryDataAnalysis(dataset):
    print("Data Info:")
    print(dataset.info())
    print("\nData Structure:")
    print(dataset.head())
    classCount = dataset["Class"].value_counts()
    bars = classCount.plot(kind="bar", figsize=(8,5), color = ("g", "r"))
    plt.title("Genuine vs Fraud")
    plt.text(0, classCount[0]/2, classCount[0], ha = 'center', color = "black")
    plt.text(1, classCount[1]/2, classCount[1], ha = 'center', color = "black")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.show()
    

def splitDataset(dataset):
    X = dataset.drop(columns=['Class'])
    y = dataset['Class']
    return train_test_split(X, y, test_size=0.3, random_state=0)

def trainlinearRegression(X_train, y_train):
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor

def trainDecisionTree(X_train, y_train):
    dTree = DecisionTreeClassifier()
    dTree.fit(X_train, y_train)
    return dTree



def printResult(classifier,y_test, y_predicted):
    df = pd.DataFrame({"Actual": y_test, "Predicted": y_predicted})
    print("Classifying Algorithm: " + classifier)
    print("Predictions where actual transaction is fraudulent:")
    print(df.loc[df['Actual'] == 1])
    print("Predictions where actual transaction is not fraudulent:")
    print(df.loc[df['Actual'] == 0])
    

fileName = "fraud.csv"
dataset = pd.read_csv(fileName)

# ExploratoryDataAnalysis(dataset)

X_train, X_test, y_train, y_test = splitDataset(dataset)

# regressor = trainlinearRegression(X_train, y_train)
# yPredictedLinearR = regressor.predict(X_test)
# printResult(y_test, yPredictedLinearR)

dTree = trainDecisionTree(X_train, y_train)
yPredictedDTree = dTree.predict(X_test)
printResult(y_test, yPredictedDTree)


# print("Training set - X:", X_train.shape, " y:", y_train.shape)
# print("Testing set - X:", X_test.shape, " y:", y_test.shape)

commands = {}

while True:











# print(dataset.describe)
# missing_values = dataset.isnull().sum()
# while True:
#     print("Command\tDescription")
#     command = input("imput command:")