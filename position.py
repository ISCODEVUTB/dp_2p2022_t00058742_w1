#Definimos la clase position
class Position:
    #Def de atributos
    latitude: float
    longitude: float
#Metodo constructor
    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude
#Metodos de la clase
    def get_latitude(self) -> float:
        return self.latitude

    def set_latitude(self, latitude: float) -> None:
        self.latitude = latitude

    def get_longitude(self) -> float:
        return self.longitude

    def set_longitude(self, longitude: float) -> None:
        self.longitude = longitude
#Metodo toString
    def toString(self) -> str:
        return f"Latit: {self.latitude}, Long: {self.longitude}"
