#Importamos la clase package
from package import Package

#Definimos la clase StandarPackage
class StandarPackage(Package):
    price_u: float = 5750.0
#Hacemos uso del metodo calcuate para calcular el precio por peso
    def calculate(self) -> float:
        w_price: float = super().calculate()
        return w_price + self.price_u