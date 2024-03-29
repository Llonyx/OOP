class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class BalancedSheet(metaclass=SingletonMeta):
    buyingReport = []
    sellingReport = []

    def AddToBuyingReport(self, buyingProduct):
        self.buyingReport.append(buyingProduct)

    def AddToSellingReport(self, sellingReport):
        self.sellingReport.append(sellingReport)

    def CreateBuyingReport(self):
        if(len(self.buyingReport) == 0):
            print("Currently, the buying report is empty")

        print("Today's buying report")
        for report in self.buyingReport:
            report.CreateInformation()

    def CreateSellingReport(self):
        if(len(self.sellingReport) == 0):
            print("Currently, the buying report is empty")

        print("Today's selling report")
        for report in self.sellingReport:
            report.CreateInformation()