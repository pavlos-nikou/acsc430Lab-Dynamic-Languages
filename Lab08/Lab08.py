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
    linearRegressor = LinearRegression()
    linearRegressor.fit(X_train, y_train)
    return linearRegressor

def trainDecisionTree(X_train, y_train):
    dTree = DecisionTreeClassifier()
    dTree.fit(X_train, y_train)
    return dTree

def trainLogisticRegression(X_train, y_train):
    logisticRegressor = logisticRegressor()
    logisticRegressor(X_train, y_train)
    return logisticRegressor



def printResult(classifier,y_test, y_predicted):
    df = pd.DataFrame({"Actual": y_test, "Predicted": y_predicted})
    print("Classifying Algorithm: " + classifier)
    print("Predictions where actual transaction is fraudulent:")
    print(df.loc[df['Actual'] == 1])
    print("Predictions where actual transaction is not fraudulent:")
    print(df.loc[df['Actual'] == 0])


# dTree = trainDecisionTree(X_train, y_train)
# yPredictedDTree = dTree.predict(X_test)
# printResult(y_test, yPredictedDTree)

commands = {"load": {"desc": "Load your file", "active": True},
            "cleanData":{"desc": "Remove all transactions with missing data","active": False},
            "showData": {"desc": "Apply short Exploratory Data Analysis", "active": False},
            "splitData": {"desc": "Split the data, training/test", "active": False},
            "run_Alg1":{"desc": "Train and run linear regression algorithm","active": False},
            "run_Alg2":{"desc": "Train and run decision Tree algorithm","active": False},
            "run_Alg3":{"desc": "Train and run logistic regression algorithm","active": False},
            "printCompare":{"desc": "Print a comparative table including all algorithm's performances", "active": False},
            "plotCompare":{"desc": "Display a comparative performance plot.","active": False},
            "exit":{"desc": "exit the program", "active": True}
            }

while True :
    
    i=1
    print("\n\n\nCommand:\tDescription:")
    for command in commands:
        if commands[command]["active"] == True :
            print(f'\t{i}:\t{commands[command]["desc"]}')
        i+=1

    inputCommand = input("choose a command: ")

    if inputCommand == "1" and commands["load"]["active"] == True:
        fileName = input("please give a file name:")
        print("Loading data now...")
        dataset = pd.read_csv(fileName)
        print("data loaded successfully")
        commands["cleanData"]["active"] = True

    elif inputCommand == "2" and commands["cleanData"]["active"] == True:
        print(f'Empty data:\n{dataset.isnull().sum()}')
        print("removing entries with missing data...")
        dataset = dataset.dropna()
        print(f'Empty data after clean up:\n{dataset.isnull().sum()}')
        
        commands["showData"]["active"] = True

    elif inputCommand == "3" and commands["showData"]["active"] == True:
        ExploratoryDataAnalysis(dataset)
        commands["splitData"]["active"] = True

    elif inputCommand == "4" and commands["splitData"]["active"] == True:
        print("Splitting data...")
        X_train, X_test, y_train, y_test = splitDataset(dataset)
        print("Data Split Successfully")
        commands["run_Alg1"]["active"] = True

    elif inputCommand == "5" and commands["run_Alg1"]["active"] == True:
        print("Training Model...")
        linearRegressor = trainlinearRegression(X_train, y_train)
        print("Training Complete")
        print("Testing Data...")
        yPredictedLinearR = linearRegressor.predict(X_test)
        printResult("Linear Regression",y_test, yPredictedLinearR)
        commands["run_Alg2"]["active"] = True

    elif inputCommand == "6" and commands["run_Alg2"]["active"] == True:
        doSomething()
        commands["run_Alg3"]["active"] = True

    elif inputCommand == "7" and commands["run_Alg3"]["active"] == True:
        doSomething()
        commands["printCompare"]["active"] = True

    elif inputCommand == "8" and commands["printCompare"]["active"] == True:
        doSomething()
        commands["plotCompare"]["active"] = True
        
    elif inputCommand == "9" and commands["plotCompare"]["active"] == True:
        doSomething()

    elif inputCommand == "10" and commands["cleanData"]["active"] == True:
        print("Thank You!!")
        break
    else:
        print("Wrong input pls try again\n\n\n")