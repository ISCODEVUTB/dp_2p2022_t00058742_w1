#Realizamos la importacion de librerias
from abc import abstractmethod, ABC
from customer import Customer

#Definimos la clase package
class Package(ABC):
    id: str 
    gr_price: float = 5750.0
    cod: int
    descript: str
    weight: float
    customer: Customer


#Definimos el cosntructor 
    def __init__(self,cod,descript,weight,customer):
        self.code = cod
        self.description = descript
        self.weight = weight
        self.customer = customer



#Definimos los metodos para obtener cada uno de los atributos.
    def get_id(self) -> str:
        return self.id

    def get_grams_price(self) -> float:
        return self.gr_price

    def get_code(self) -> int:
        return self.code

    def set_code(self, cod: int) -> None:
        self.code = cod
    
    def get_description(self) -> str:
        return self.descript

    def set_description(self, descript: str) -> None:
        self.descript = descript

    def get_weight(self) -> float:
        return self.weight

    def set_weight(self, weight: float) -> None:
        self.weight = weight

    def get_customer(self) -> Customer:
        return self.customer

    def set_customer(self, customer: Customer) -> None:
        self.customer = customer


#Metodo para realizar el calculo de peso por precio.
    @abstractmethod
    def calculate(self) -> float:
        return self.weight * self.gr_price