from account import Account

class Driver(Account):
    licencia : str
    
    def _init_(self, id, nombre, genero, telefono, edad, licencia):
         super()._init_(id, nombre, genero, telefono, edad)
         self.licencia = licencia