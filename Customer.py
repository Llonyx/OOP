from BussinessPerson import BussinessPerson

class Customer(BussinessPerson):
    userID = None
    name = None

    def __init__(self, userID, name, purchaseProductFunc):
        self.userID = userID
        self.name = name
        self.purchaseProductFunc = purchaseProductFunc

    def PurchaseProduct(self, product):
        self.purchaseProductFunc(product)