from InventoryController import InventoryController
class WarehouseManagementSystem:
    def __init__(self):
        self.inventoryController = InventoryController()

    def AddProduct(self, product):
        self.inventoryController.AddItem(product)

    def SellProduct(self, product):
        self.inventoryController.SellItem(product)

    def DisplayProduct(self):
        self.inventoryController.CreateInventoryItemList()
