class InventoryController:
    __inventoryList = []
    
    def AddItem(self, product):
        existingProduct = self.GetExistingProduct(product)
        
        if(existingProduct == None):
            self.__inventoryList.append(product)
            return
        
        existingProduct.qty += product.qty

    def SellItem(self, product):
        existingProduct = self.GetExistingProduct(product)

        if(existingProduct == None):
            print("[Inventory Controller] product is not found")
            return
        
        if(existingProduct.qty < product.qty):
            print("[Inventory Controller] product quantity is less than you expected")
            return
        
        existingProduct.qty -= product.qty

        if(existingProduct.qty == 0):
            self.__inventoryList.remove(existingProduct)
        

    def CreateInventoryItemList(self):
        inventoryData = iter(self.__inventoryList)
        idx = 1
        while True:
            try:
                productData = next(inventoryData)
                print(f"{idx}. Product ID = {productData.id} ")
                print(f"   Product Name = {productData.name} ")
                print(f"   Product Quantity = {productData.qty} ")
                idx += 1
            except StopIteration:
                break

    def GetExistingProduct(self, product):
        for item in self.__inventoryList:
             if(item.id == product.id):
                 return item
        return None