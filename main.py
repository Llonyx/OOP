from WarehouseManagementSystem import WarehouseManagementSystem
from BalancedSheet import BalancedSheet
from Supplier import Supplier
from Customer import Customer
from Product import Product

if __name__ == "__main__":
    warehouseManagementSystem = WarehouseManagementSystem()

    menuOption= 0
    while(menuOption != 3):
        print("1. List of Goods")
        print("2. Transaction")
        print("3. Today's Balanced Sheet Report")
        print("4. Exit")
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
                BalancedSheet().AddToBuyingReport(supplier)              
            elif(transactionOption == 2):
                id = input("Input Customer ID: ")
                name = input("Customer name: ")
                productID = input("Product ID: ")
                productName = input("Product Name: ")
                productQty = int(input("Product Quantity: "))
                product = Product(productID, productQty, productName) 
                customer = Customer(id, name, product, warehouseManagementSystem.SellProduct)
                customer.PurchaseProduct()
                BalancedSheet().AddToSellingReport(customer)
            else:
                print("Invalid option")
        elif(menuOption == 3):
            print("1. Purchase Report")
            print("2. Selling Report")
            balancedSheetOption = int(input("Please choose the option: "))
            if(balancedSheetOption == 1):
                BalancedSheet().CreateBuyingReport()
            elif(balancedSheetOption == 2):
                BalancedSheet().CreateSellingReport()
            else:
                print("Invalid Option")
        elif(menuOption == 4):
            print("Shutting Down...")
        else:
            print("Invalid option")