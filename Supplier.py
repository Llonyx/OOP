from BussinessPerson import BussinessPerson

class Supplier(BussinessPerson):
    userID = None
    name = None

    def __init__(self, userID, name, product, restockProductFunc):
        self.userID = userID
        self.name = name
        self.product = product
        self.restockProductFunc = restockProductFunc

    def RestockProduct(self):
        self.restockProductFunc(self.product)
