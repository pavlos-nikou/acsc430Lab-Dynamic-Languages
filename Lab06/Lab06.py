import csv
import myUtils as utils

def openCsvFile(fileName):
    products = []
    file = open(fileName, "r")
    csvFile = csv.DictReader(file)
    for line in csvFile:
        products.append(line)
    return products

# create product as objects
def createObject(product):
    if product["Product_Type"] == "Electronics":
        newProduct = utils.Electronics(product["SerialNumber"], product["Title"], product["regularPrice"], product["Manufacturer/Author"], product["Discount"])
    if product["Product_Type"] == "TV":
        newProduct = utils.Tvs(product["SerialNumber"], product["Title"], product["regularPrice"], product["Manufacturer/Author"], product["Discount"], product["Size"], product["SmartTv"])
    if product["Product_Type"] == "Book":
        newProduct = utils.Books(product["SerialNumber"], product["Title"], product["regularPrice"], product["Manufacturer/Author"], product["Discount"], product["yearPublished"])
    return newProduct
# creates a list of objects from the product list and returns it
def createObjectsFromList(productList):
    objectList = []
    for product in productList:
        objectList.append(createObject(product))
    return objectList

# prints out the proudct list depending on the type the user needs
def listProducts(products, category = ""):
    if category == "" : 
        for product in products:
            print(product.__str__())
    elif category == "Electronics":
        for product in products:
            if isinstance(product, utils.Electronics):
                print(product.__str__())
    elif category == "Books":
        for product in products:
            if isinstance(product, utils.Books):
                print(product.__str__())
    else:
        print("this type of products does not exist\nplease try again\n\n")

def main():
    while True:
        print("Commands:\t Description:\n")
        print('loadCsv\t\tLoad product data from CSV\nlistPrd\t\tList products by product type\naddProd\t\tAdd product\nexit\t\tExit the program')
        command = input("-->")

        if command == "loadCsv":
            fileName = input("Please provide the name of the file you would like to load:\n\t")
            productList = openCsvFile(fileName)
            prodcutListObjs = createObjectsFromList(productList)
            print(f"Loaded {len(prodcutListObjs)} products successfully!\n\n")

        if command == "listPrd":
            category = input("press enter for all product or type the desired category:")
            listProducts(prodcutListObjs, category)

        if command == "addProd":
            product = {}
            product["SerialNumber"] = input("product Serial Number:")
            product["Title"] = input("product Title:")
            product["regularPrice"] = input("product Price:")
            product["Product_Type"] = input("product Type:")

            if product["Product_Type"] == "Electronics" or product["Product_Type"] == "TV":
                product["Manufacturer/Author"] = input("product Manufacturer:")
                product["Discount"] = input("product Discount:")

            if product["Product_Type"] == "TV":
                product["Size"]  = input("TV Size:")
                product["SmartTv"] = input("smart Tv?:")

            if product["Product_Type"] == "Book":
                product["Manufacturer/Author"] = input("Author:")
                product["yearPublished"] = input("year published :")
                product["Discount"] = input("product Discount:")
            prodcutListObjs.append(createObject(product))
        # if command == "save": 
        #     file = file
        if command == "exit":
            print("goodbye!!")
            
            break

main()