import pandas as pd
import matplotlib.pyplot as plt
import time as t
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score


# pavlos nikou
# st026276
# Lab08

def ExploratoryDataAnalysis(dataset):
    print("Data Info:")
    print(dataset.info())# Print information about the dataset
    print("\nData Structure:")
    print(dataset.head())# Print the first few rows of the dataset to understand its structure
    classCount = dataset["Class"].value_counts()# Count the number of instances for each class in the "Class" column
    # Create a bar plot to visualize the distribution of genuine and fraud instances
    classCount.plot(kind="bar", figsize=(8,5), color = ("g", "r"))
    plt.title("Genuine vs Fraud")
    plt.text(0, classCount[0]/2, classCount[0], ha = 'center', color = "black")
    plt.text(1, classCount[1]/2, classCount[1], ha = 'center', color = "black")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.show()
    

def splitDataset(dataset):#split the data
    X = dataset.drop(columns=['Class'])
    y = dataset['Class']
    return train_test_split(X, y, test_size=0.3, random_state=0)

def trainlinearRegression(X_train, y_train): #train linear regression model
    linearRegressor = LinearRegression()
    linearRegressor.fit(X_train, y_train)
    return linearRegressor

def trainDecisionTree(X_train, y_train):#train decision Tree model
    dTree = DecisionTreeClassifier()
    dTree.fit(X_train, y_train)
    return dTree

def trainLogisticRegression(X_train, y_train):#train logisticRegression Model
    logisticRegressor = LogisticRegression()
    logisticRegressor.fit(X_train, y_train)
    return logisticRegressor



def printResult(classifier,y_test, y_predicted):
    df = pd.DataFrame({"Actual": y_test, "Predicted": y_predicted})
    print("Classifying Algorithm: " + classifier)
    print("Predictions where actual transaction is fraudulent:")
    print(df.loc[df['Actual'] == 1])#get instances where the actual transaction was a fraud
    print("Predictions where actual transaction is not fraudulent:")
    print(df.loc[df['Actual'] == 0])#get instances where the actual transaction was not a fraud
    print(f"{classifier} Performance:")
    if classifier == "Linear Regression":
        mse = mean_squared_error(y_test, y_predicted)# get mean squared error linear regression
        print("Mean Squared Error (MSE):", mse)
        return mse
    else:
        # get accuracy precision and recall for decision tree and logistic regression
        accuracy = accuracy_score(y_test, y_predicted)
        precision = precision_score(y_test, y_predicted)
        recall = recall_score(y_test, y_predicted)
        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        return accuracy, precision, recall
    

def doSomething():
    print("i did something")


# all commands with an active flag to chech if available on not
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
    # print all commands
    i=1
    print("\n\n\nCommand:\tDescription:")
    for command in commands:
        if commands[command]["active"] == True :
            print(f'\t{i}:\t{commands[command]["desc"]}')
        i+=1
    # get command
    inputCommand = input("Choose a command: ")

    if inputCommand == "1" and commands["load"]["active"] == True:
        fileName = input("Please give a file name:")
        print("Loading data now...")
        dataset = pd.read_csv(fileName)
        print("data loaded successfully")
        commands["cleanData"]["active"] = True #activate next command

    elif inputCommand == "2" and commands["cleanData"]["active"] == True:
        print(f'Empty data:\n{dataset.isnull().sum()}') #print the count of missing data in each column before clean up
        print("removing entries with missing data...")
        dataset = dataset.dropna()# remove rows with missing data
        print(f'Empty data after clean up:\n{dataset.isnull().sum()}')#print the count of missing data in each column after clean up
        commands["showData"]["active"] = True

    elif inputCommand == "3" and commands["showData"]["active"] == True:
        ExploratoryDataAnalysis(dataset)
        commands["splitData"]["active"] = True#activate next command

    elif inputCommand == "4" and commands["splitData"]["active"] == True:
        print("Splitting data...")
        X_train, X_test, y_train, y_test = splitDataset(dataset)# split the data
        print("Data Split Successfully")
        commands["run_Alg1"]["active"] = True#activate next command

    elif inputCommand == "5" and commands["run_Alg1"]["active"] == True:
        print("Training Model...")
        startTime = t.time()
        linearRegressor = trainlinearRegression(X_train, y_train)
        linearRegresionTTime = t.time() - startTime
        print("Training Complete\n")
        print(f"training took: {linearRegresionTTime}s\n\n")
        print("Testing Data...")
        yPredictedLinearR = linearRegressor.predict(X_test)#use the x test values to test the model
        mse = printResult("Linear Regression",y_test, yPredictedLinearR)
        commands["run_Alg2"]["active"] = True#activate next command

    elif inputCommand == "6" and commands["run_Alg2"]["active"] == True:
        print("Training Model...")
        startTime = t.time()
        dTree = trainDecisionTree(X_train, y_train)
        dTreeTTime = t.time() - startTime
        print("Training Complete\n")
        print(f"training took: {dTreeTTime}s\n\n")
        print("Testing Data...")
        yPredictedDTree = dTree.predict(X_test)#use the x test values to test the model
        dTreeAccuracy, dTreePrec, dTreeRec = printResult("Decision Tree",y_test, yPredictedDTree)
        commands["run_Alg3"]["active"] = True#activate next command

    elif inputCommand == "7" and commands["run_Alg3"]["active"] == True:
        print("Training Model...")
        startTime = t.time()
        logisticRegressor = trainLogisticRegression(X_train, y_train)
        logisticRegressorTTime = t.time() - startTime
        print("Training Complete\n")
        print(f"training took: {t.time() - startTime}s\n\n")
        print("Testing Data...")
        yPredictedLogisticR = logisticRegressor.predict(X_test)#use the x test values to test the model
        logRAccuracy, logRPrec, logRRec = printResult("Logistic Regression",y_test, yPredictedLogisticR)
        commands["printCompare"]["active"] = True#activate next command

    elif inputCommand == "8" and commands["printCompare"]["active"] == True:#print time and performance of each model
        print("Performance Report:")
        print(f'\tLinear Regression:\n\t\tTraining Time: {linearRegresionTTime:.2f}\tPerformance (Mean Squared Error): {mse:.2f}')
        print(f'\tPrecision Tree:\n\t\tTraining Time: {dTreeTTime:.2f}\tAccuracy: {dTreeAccuracy:.2f}\tPrecision: {dTreePrec:.2f}\tRecall: {dTreeRec:.2f}')
        print(f'\tLogistic Regression:\n\t\tTraining Time: {logisticRegressorTTime:.2f}\tAccuracy: {logRAccuracy:.2f}\tPrecision: {logRPrec:.2f}\tRecall: {logRRec:.2f}')
        
        
        commands["plotCompare"]["active"] = True#activate next command
        
    elif inputCommand == "9" and commands["plotCompare"]["active"] == True:
        
        x = ["Decision Tree", "Logistic Regression"]
        accs = [dTreeAccuracy, logRAccuracy]
        precs = [dTreePrec, logRPrec]
        recs = [dTreeRec, logRRec]

        X_axis = np.arange(len(x))
        bar_width = 0.2
        
        figure, axis = plt.subplots(2, 2, figsize=(8, 6))
        #trying to print barplot with multiple bars for each model
        axis[0, 0].bar(X_axis - 1.1*bar_width, accs, bar_width, label='Accuracy')
        axis[0, 0].bar(X_axis, precs, bar_width, label='Precision')
        axis[0, 0].bar(X_axis + 1.1*bar_width, recs, bar_width, label='Recall')
        axis[0, 0].set_xticks(X_axis)
        axis[0, 0].set_xticklabels(x)
        axis[0, 0].set_ylabel('Scores')
        axis[0, 0].set_title('Model Comparison')
        axis[0, 0].legend()

        axis[0, 1].bar("linear Regression", mse, 0.01, label='MSE')
        axis[0, 1].set_title('linear Regression Score')

        # x = [linear Regresion]
        # axis[1,:].bar()



        plt.tight_layout()
        plt.show()

    elif inputCommand == "10" and commands["exit"]["active"] == True:
        print("Thank You!!")
        break
    else:
        print("Wrong input please try again\n\n\n")