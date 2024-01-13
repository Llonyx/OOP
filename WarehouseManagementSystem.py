from InventoryController import InventoryController
from Supplier import Supplier
from Customer import Customer
from Product import Product
from BalancedSheet import BalancedSheet

class WarehouseManagementSystem:
    def __init__(self):
        self.inventoryController = InventoryController()

    def AddProduct(self, product):
        self.inventoryController.AddItem(product)

    def SellProduct(self, product):
        self.inventoryController.SellItem(product)

    def DisplayProduct(self):
        self.inventoryController.CreateInventoryItemList()

    def CreateProductOrder(self, productID, productQty, productName):
        product = Product(productID, productQty, productName)
        return product
    
    def CreateSupplier(self, id, name, product):
        supplier = Supplier(id, name, product, self.AddProduct)
        return supplier
    
    def CreateCustomer(self, id, name, product):
        customer = Customer(id, name, product, self.SellProduct)
        return customer
    
    def Consume(self, bussinessPerson):
        bussinessPerson.Consume()

    def CreateBuyingReport(self):
        BalancedSheet.CreateBuyingReport()

    def CreateSellingReport(self):
        BalancedSheet.CreateSellingReport()

    def IsProductValdiate(self, product):
        if(len(product.id) == 0 or len(product.qty) == 0 or len(product.name) == 0):
            return False
        return True
    
    def IsUserValidate(self, bussinessMan):
        if(len(bussinessMan) == 0 or len(bussinessMan) == 0):
            return False
        return True