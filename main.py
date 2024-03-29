from WarehouseManagementSystem import WarehouseManagementSystem

if __name__ == "__main__":
    warehouseManagementSystem = WarehouseManagementSystem()

    menuOption= 0
    while(menuOption != 4):
        print("1. List of Goods")
        print("2. Transaction")
        print("3. Today's Balanced Sheet Report")
        print("4. Exit")
        menuOption = int(input("Please choose the option: "))
        print()
        if(menuOption == 1):
            warehouseManagementSystem.DisplayProduct()

        elif(menuOption == 2):
            print("1. Restock product")
            print("2. Sell product")
            transactionOption = int(input("Please choose the option: "))
            print()
            if(transactionOption == 1):
                try:
                    productID = input("Product ID: ")
                    productName = input("Product Name: ")
                    productQty = int(input("Product Quantity: "))

                    product = warehouseManagementSystem.CreateProductOrder(productID, productName, productQty)
                    if(not warehouseManagementSystem.IsProductValdiate(product)):
                       raise ValueError
                    
                    id = input("Input Supplier ID: ")
                    name = input("Supplier name: ")
                    supplier = warehouseManagementSystem.CreateSupplier(id, name, product)
                    if(not warehouseManagementSystem.IsUserValidate(supplier)):
                        raise ValueError
                    
                    warehouseManagementSystem.Consume(supplier)
                    
                except ValueError:
                    print("Invalid!, Please check your input")              
            elif(transactionOption == 2):
                try:
                    productID = input("Product ID: ")
                    productName = input("Product Name: ")
                    productQty = int(input("Product Quantity: "))

                    product = warehouseManagementSystem.CreateProductOrder(productID, productQty, productName) 
                    if(not warehouseManagementSystem.IsProductValdiate(product)):
                       raise ValueError
                    
                    id = input("Input Customer ID: ")
                    name = input("Customer name: ")
                    customer = warehouseManagementSystem.CreateCustomer(id, name, product, warehouseManagementSystem.SellProduct)
                    if(not warehouseManagementSystem.IsUserValidate(supplier)):
                        raise ValueError
                    
                    warehouseManagementSystem.Consume(customer)

                except ValueError:
                    print("Invalid!, Please check your input")             
            else:
                print("Invalid option")
            print()
        elif(menuOption == 3):
            print("1. Purchase Report")
            print("2. Selling Report")
            balancedSheetOption = int(input("Please choose the option: "))
            print()
            if(balancedSheetOption == 1):
                warehouseManagementSystem.CreateBuyingReport()
            elif(balancedSheetOption == 2):
                warehouseManagementSystem.CreateSellingReport()
            else:
                print("Invalid Option")
        elif(menuOption == 4):
            print("Shutting Down...")
        else:
            print("Invalid option")
        print()