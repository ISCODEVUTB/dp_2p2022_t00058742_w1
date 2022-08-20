#Importamos la clase package
from package import Package

#Definimos la clase OverweightPackage
class OverweightPackage(Package):
    ov_price_pack: float = 5750.0

    def calculate(self) -> float:
        we_price: float = super().calculate()
        ov_price = self.weight - 2.0 if self.weight > 2.0 else 0.0
        return we_price + (ov_price * self.ov_price_pack)