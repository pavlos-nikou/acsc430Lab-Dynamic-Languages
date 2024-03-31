import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_yearly_average(df):
    salesData = df.drop(["month_number", "total_units", "total_profit"],axis=1)
    return salesData.mean()

def get_most_profit_month(df):
    return df.loc[df['total_profit'].idxmax()]

def get_product_over_under(df, product, min, max):
    overDf = df[df[product] > min]
    return overDf[overDf[product]< max]

def plotLine(xAxis, yAxis, xLabel, yLabel, style = {"line-color":"b", "line-style":"-","marker":""}):
    plt.title("Monthly Profit")
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    styleStr = f"{style["marker"]}{style["line-style"]}{style["line-color"]}"
    print(styleStr)
    plt.plot(xAxis, yAxis, styleStr)
    plt.show()

def plot_units_sold(products, months):
    for product in products:
        print(type(product))
        plt.plot(months, products[product], label = product)
    plt.legend()
    plt.show()

def scatter_products(productX, productY, xLabel, yLabel):
    plt.scatter(productX, productY)
    plt.title(f'Correlation between {xLabel} and {yLabel}')
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

def bar_plot_product(product, months):
    plt.bar(months, product)
    plt.show()


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

salesDf = pd.read_csv("sales.csv")
print("Welcome!!\nsales.csv was loaded successfully")



while True:
    print("Command\t\tCommand Description\n")
    for command in commands:
        print(f"{command[0]}\t\t{command[1]}")
    inputCommand = input("command:")
    if inputCommand == "1":
        print("Month with biggest profit:")
        print(get_most_profit_month(salesDf))
    if inputCommand == "2":
        print("The average sales for each product are :\n")
        print(get_yearly_average(salesDf))
        print("")
    if inputCommand == "3":
        print(get_product_over_under(salesDf, "toothpaste", 3000, 6000))
    if inputCommand == "4":
        plotLine(salesDf["month_number"], salesDf["total_profit"], "Months", "Total Profit")
    if inputCommand == "5":
        plot_units_sold(salesDf.drop(["month_number", "total_units", "total_profit"], axis = 1), salesDf["month_number"])
    if inputCommand == "6":
        scatter_products(salesDf["facecream"], salesDf["shampoo"],"Face Cream", "Shampoo")
    if inputCommand == "7":
        bar_plot_product(salesDf["shampoo"], salesDf["month_number"])
    if inputCommand == "8":
        continue
    if inputCommand == "9":
        months = salesDf["month_number"].to_numpy()
        profit = salesDf["total_profit"].to_numpy()
        plotLine(months, profit, "Months", "Total Profit",{"line-color":"r", "line-style":":","marker":"o"})
    if inputCommand == "10":
        print("Goodby!!")
        break