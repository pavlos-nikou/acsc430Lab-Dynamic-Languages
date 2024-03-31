import matplotlib
import numpy as np
import pandas as pd

def get_yearly_average(df):
    salesData = df.drop(["month_number", "total_units", "total_profit"],axis=1)
    return salesData.mean()


commands = [
    [1, "Print month with the biggest profit"],
    [2, "Print average sales for all products"],
    [3, "Print records with toothpaste sales > 6000 and face cream sales < 3000"],
    [4, "Line plot of total profit for all months (X: Month, Y: profit)"],
    [5, "Multiline plot of units sold per month for each product"],
    [6, "Scatterplot showing correlation between face cream and shampoo sales"],
    [7, "Bar chart of shampoo sales for all months"],
    [8, "Calculate yearly average sales of moisturizer using DataFrame.to_numpy()"],
    [9, "Line plot of total profit for all months"],
    [10, "Exit"]
]

df = pd.read_csv("sales.csv")
print("Welcome!!\nsales.csv was loaded successfully")



while True:
    print("Command\t\tCommand Description\n")
    for command in commands:
        print(f"{command[0]}\t\t{command[1]}")
    inputCommand = input("command:")
    if inputCommand == "1":
        continue
    if inputCommand == "2":
        continue
    if inputCommand == "3":
        continue
    if inputCommand == "4":
        continue
    if inputCommand == "5":
        continue
    if inputCommand == "6":
        continue
    if inputCommand == "7":
        continue
    if inputCommand == "8":
        continue
    if inputCommand == "9":
        continue
    if inputCommand == "10":
        print("Goodby!!")
        break