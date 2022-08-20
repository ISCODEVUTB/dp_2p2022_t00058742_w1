#Definimos la clase BankAccount
class BankAccount :
  account_id:str
  bank_name:str
  bank_id:str
  amount:float  = 0.0
  #Definimos el constructor
  def __init__(self,account_id:str,bank_name:str,bank_id:str) -> None:
    self.account_id = account_id
    self.bank_name = bank_name
    self.bank_id = bank_id
  #Definimos los metodos de obtencion de datos  
  def get_account_id(self) -> str:
        return self.account_id

  def set_account_id(self, account_id: str) -> None:
        self.account_id = account_id

  def get_bank_name(self) -> str:
        return self.bank_name

  def set_bank_name(self, bank_name: str) -> None:
        self.bank_name = bank_name


  def deposit(self,amount:float)->bool:
    self.amount = self.amount + amount
    return True
