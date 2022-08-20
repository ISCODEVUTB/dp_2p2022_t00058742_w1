from person import Person
from enumerat import DocumentType,Role
from .bank_account import BankAccount
#Definimos la clase internal pasando por parametro la clase importada person
class Internal (Person):
#Definimos sus atributos 
  role:Role
  account:BankAccount

  def __init__(self, id: str, national_id: str, id_type: DocumentType,
    name: str, last_name: str, person_type: str, email: str,role:Role,account:BankAccount) -> None:
    super().__init__(id, national_id, id_type, name, last_name, person_type, email)
    self.role = role
    self.account = BankAccount
#Retornamos el role
  def get_role(self)->Role:
    return self.role