class Product:
    def __init__(self, sn, title, price):
        self.serialNumber = sn
        self.title = title
        self.regularPrice = price
    def setRegularPrice(self, newPrice):
        self.regularPrice = newPrice
    def getRegularPrice(self):
        return self.regularPrice
    def setSerialNumber(self, newSn):
        self.serialNumber = sn
    def getSerialNumber(self):
        return self.serialNumber
    def setTitle(self, newTitle):
        self.title = newTitle
    def getTitle(self):
        return self.title
    
class Electronics(Product):
    def __init__(self, sn, title, price, manufacturer, discount):
        super().__init__(sn, title, price)
        self.mafct = manufacturer
        self.discount = discount
    def setManufacturer(self, newManufacturer):
        self.mafct = newManufacturer
    def setManufacturer(self):
        return self.mafct
    def setDiscount(self, newDiscount):
        self.discount = newDiscount
    def getDiscount(self):
        return self.discount
    def computeDiscount(self):
        return self.regularPrice * self.discount
    
class Books(Product):
    def __init__(self, sn, title, price, auth, discount, yearPublished=None):
        super().__init__(sn, title, price)
        self.author = auth
        self.yearPublished = yearPublished
        self.discount = discount
    def setAuthor(self, newAuthor):
        self.setAuthor = newAuthor
    def getAuth(self):
        return self.author
    def setYear(self, newYear):
        self.yearPublished = newYear
    def getYear(self):
        return self.yearPublished
    def getDiscount(self):
        return self.discount
    def computeDiscount(self):
        return self.regularPrice * self.discount
    
class Tvs(Electronics):
    def __init__(self, sn, title, price, manufacturer, discount, size, smartTv):
        super().__init__(sn, title, price, manufacturer, discount)
        self.size = size
        self.smartTV = smartTv
    def setSize(self, newSize):
        self.size = newSize
    def getSize(self):
        return self.size
    def setSmartTv(self, newSmartTv):
        self.smartTV = newSmartTv
    def getSmartTv(self):
        return self.smartTV