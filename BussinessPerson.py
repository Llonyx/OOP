from abc import ABC, abstractproperty, abstractmethod

class BussinessPerson:
    @abstractproperty
    def userID(self):
        pass
    
    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def CreateInformation(self):
        pass
