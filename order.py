from package import Package
from customer import Customer
from enumerat import OrderStatus
from location import Location
import string
import random

#Definimos la clase order 
class Order:
    ID: str
    package: Package
    is_paid: bool
    price: float
    receiver: Customer
    sender: Customer
    status: OrderStatus
    location: Location
#definimos el constructor
    def __init__(self, package: Package, is_paid: bool, price: float, receiver: Customer, sender: Customer, status: OrderStatus, location: Location) -> None:
        self.package = package
        self.is_paid = is_paid
        self.price = price
        self.receiver = receiver
        self.sender = sender
        self.status = status
        self.location = location
#metodos getter
    def get_package(self) -> Package:
        return self.package

    def set_receiver(self, receiver: Customer) -> None:
        self.receiver = receiver

    def get_sender(self) -> Customer:
        return self.sender

    def set_sender(self, sender: Customer) -> None:
        self.sender = sender

    def get_status(self) -> OrderStatus:
        return self.status

    def set_status(self, status: OrderStatus) -> None:
        self.status = status

    def get_location(self):
        return self.location
        
    def set_package(self, package: Package) -> None:
        self.package = package

    def get_is_paid(self) -> bool:
        return self.is_paid

    def set_is_paid(self, is_paid: bool) -> None:
        self.is_paid = is_paid

    def get_price(self):
        return self.price

    def set_price(self, price: float) -> None:
        self.price = price

    def get_receiver(self) -> Customer:
        return self.receiver

    

    def set_location(self, location: Location) -> None:
        self.location = location
      #Retorno 
    def toString(self) -> str:
        return f"Package id: {self.package.ID}, Is paid: {self.is_paid}, Price: {self.price}, Reciever: {self.receiver.name} {self.receiver.last_name}, Sender: {self.sender.name} {self.sender.last_name}, Status: {self.status}, Location: {self.location.country} - {self.location.state} - {self.location.city}"