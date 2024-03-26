import csv
import myUtils as utils

def openCsvFile(fileName):
    products = []
    file = open("All_Products.csv", "r")
    csvFile = csv.DictReader(file)
    for line in csvFile:
        products.append(line)
    return products

def createObject(product):
    if product["Product_Type"] == "Electronics":
        newProduct = utils.Electronics(product["SerialNumber"], product["Title"], product["regularPrice"], product["Manufacturer/Author"], product["Discount"])
    if product["Product_Type"] == "TV":
        newProduct = utils.Tvs(product["SerialNumber"], product["Title"], product["regularPrice"], product["Manufacturer/Author"], product["Discount"], product["Size"], product["SmartTv"])
    if product["Product_Type"] == "Book":
        newProduct = utils.Books(product["SerialNumber"], product["Title"], product["regularPrice"], product["Manufacturer/Author"], product["Discount"])
    return newProduct
def createObjectsFromList(productList):
    objectList = []
    for product in productList:
        objectList.append(createObject(product))
    return objectList


productList = openCsvFile("All_Products.csv")
prodcutListObjs = createObjectsFromList(productList)
print(prodcutListObjs[4])