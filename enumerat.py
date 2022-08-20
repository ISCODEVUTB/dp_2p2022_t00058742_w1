from enum import Enum


class DocumentType(Enum):
    DNI = 1
    PASSPORT = 2

class PersonType(Enum):
    NATURAL = 1
    LEGAL= 2

class Role(Enum):
    ADMIN = 1
    USER = 2
    DRIVER = 3
    
class InvoiceStatus(Enum):
    PROCESSING = 1
    SENT = 2
    REJECTED = 3
    CANCELLED = 4

class PaymentMethodsTypes(Enum):
    CREDIT = 1
    DEBIT = 2
    TRANSFER = 3
    CASH = 4
    
class OrderStatus(Enum):
    PENDING = 1
    PAYMENT_DUE_DATE = 2

class DeliveryStatus (Enum):
    DELIVERY = 1
    CANCELLED = 2 
    REJECTED = 3
    TRANSIT = 4 
    PICKUP_AVAILABLE = 5
    DELAYED = 6 
    DRAFTED = 7