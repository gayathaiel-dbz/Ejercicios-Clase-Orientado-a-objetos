class Cuenta:
    def __init__(self):
        self.saldo = self.saldo
    
    @property 
    def saldo(self):
        return self._saldo
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
    
    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            return True
        return False