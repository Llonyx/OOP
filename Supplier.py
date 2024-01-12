from BussinessPerson import BussinessPerson

class Supplier(BussinessPerson):
    userID = None
    name = None
    productAmount = None

    def __init__(self, userID, name, product, restockProductFunc):
        self.userID = userID
        self.name = name
        self.product = product
        self.restockProductFunc = restockProductFunc

        self.productAmount = product.qty

    def RestockProduct(self):
        self.restockProductFunc(self.product)

    def CreateInformation(self):
        print(f"Supplier ID: {self.userID}")
        print(f"Supplier Name: {self.name}")
        print()
        print(f"Supplier restock product information:")
        print(f"Product ID: {self.product.id}")
        print(f"Product Name: {self.product.name}")
        print(f"Product Quantity: {self.productAmount}")
