from BussinessPerson import BussinessPerson
from BalancedSheet import BalancedSheet

class Customer(BussinessPerson):
    userID = None
    name = None
    productAmount = None

    def __init__(self, userID, name,product, purchaseProductFunc):
        self.userID = userID
        self.name = name
        self.product = product
        self.purchaseProductFunc = purchaseProductFunc

        self.productAmount = product.qty

    def Consume(self):
        self.purchaseProductFunc(self.product)
        BalancedSheet().AddToSellingReport(self)

    def CreateInformation(self):
        print(f"Customer ID: {self.userID}")
        print(f"Customer Name: {self.name}")
        print()
        print(f"Customer purchase product information:")
        print(f"Product ID: {self.product.id}")
        print(f"Product Name: {self.product.name}")
        print(f"Product Quantity: {self.productAmount}")