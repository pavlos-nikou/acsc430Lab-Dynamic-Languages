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
    def __str__(self):
        return f'\tProduct Name: {self.title}\n\tSerial Number: {self.serialNumber}\n\tRegular Price: {self.regularPrice}\n\n'
    
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
        return float(self.regularPrice)-(float(self.regularPrice) * float(self.discount))
    def __str__(self):
        return f'\tProduct Name:{self.title}\n\tSerial Number: {self.serialNumber}\n\tManufacturer: {self.mafct}\n\tRegular Price: {self.regularPrice}\n\tDiscount Price({float(self.discount)*100:.2f}%): {self.computeDiscount():.2f}\n\n'
    
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
        return float(self.regularPrice)-(float(self.regularPrice) * float(self.discount))
    def __str__(self):
        return f'\tProduct Name:{self.title}\n\tSerial Number: {self.serialNumber}\n\tAuthor: {self.author}\n\tYear Published: {self.yearPublished}\n\tRegular Price: {self.regularPrice}\n\tDiscount Price({float(self.discount)*100:.2f}%): {self.computeDiscount():.2f}\n\n'
    
    
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
    def __str__(self):
        return f'\tProduct Name:{self.title}\n\tSerial Number: {self.serialNumber}\n\tManufacturer: {self.mafct}\n\tSize: {self.size}"\n\tSmartTv: {self.smartTV}\n\tRegular Price: {self.regularPrice}\n\tDiscount Price({float(self.discount)*100:.2f}%): {self.computeDiscount():.2f}\n\n'