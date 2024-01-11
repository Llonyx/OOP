from WarehouseManagementSystem import WarehouseManagementSystem
from Supplier import Supplier
from Customer import Customer
from Product import Product

if __name__ == "__main__":
    warehouseManagementSystem = WarehouseManagementSystem()

    menuOption= 0
    while(menuOption != 3):
        print("1. List of Goods")
        print("2. Transaction")
        print("3. Exit")
        menuOption = int(input("Please choose the option: "))
        
        if(menuOption == 1):
            warehouseManagementSystem.DisplayProduct()

        elif(menuOption == 2):
            print("1. Restock product")
            print("2. Sell product")
            transactionOption = int(input("Please choose the option: "))
            if(transactionOption == 1):
                id = input("Input Supplier ID: ")
                name = input("Supplier name: ")
                productID = input("Product ID: ")
                productName = input("Product Name: ")
                productQty = int(input("Product Quantity: "))
                product = Product(productID, productQty, productName) 
                supplier = Supplier(id, name, product, warehouseManagementSystem.AddProduct)
                supplier.RestockProduct()
        else:
            print("Shutting Down...")