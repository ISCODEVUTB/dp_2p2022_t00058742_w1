from abc import ABC,abstractmethod
from position import Location
from enumerat import PersonType,DocumentType
import random


#   Definimos la clase persona
class Person(ABC):
  
  
  id:str
  national_id:str
  id_type:DocumentType
  name:str
  last_name:str
  person_type:PersonType
  email:str

  def __init__(
    self,id:str,national_id:str,id_type:DocumentType,
    name:str,last_name:str,person_type:str,email:str
  ) -> None:

    self.email = email
    self.id = id
    self.id_type = id_type
    self.name = name
    self.person_type = person_type
    self.last_name = last_name
    self.national_id = national_id
   
  
  #  getters metodos
  def get_email(self)->str:
    return self.email

  def get_id(self)->str:
    return self.id

  def get_national_id(self)->str:
    return self.national_id
  
  def get_id_type(self)->DocumentType:
    return self.id_type
  
  def get_name(self)->str:
    return self.name
  
  def get_national_id(self)->str:
    return self.national_id

  def get_last_name(self)->str:
    return self.last_name

  @abstractmethod
  def validation_biometrict(self)->bool:
    return True
    
  @abstractmethod
  def toString(self)->str:
    return f'id {self.id} name {self.name }  last name {self.last_name} email {self.email} document type {self.id_type}  national id {self.national_id}   '