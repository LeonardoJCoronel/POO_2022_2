from account import Account

class User(Account):
        
    def _init_(self, id, nombre, genero, telefono, edad):
        super()._init_(id, nombre, genero, telefono, edad)