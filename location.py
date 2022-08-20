class Location:
    country: str
    state: str
    city: str
    address_line1: str
    address_line2: str
    zip_code: int

    def __init__(self, country: str, state: str, city: str, address_line1: str, address_line2: str, zip_code: int) -> None:
        self.country = country
        self.state = state
        self.city = city
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.zip_code = zip_code

    def get_country(self) -> str:
        return self.country

    def set_country(self, country: str) -> None:
        self.country = country

    def get_state(self) -> str:
        return self.state

    def set_state(self, state: str) -> None:
        self.state = state

    def get_city(self) -> str:
        return self.city

    def set_city(self, city: str) -> None:
        self.city = city
    def toString(self) -> str:
        return f"Country: {self.country}, State: {self.state}, City: {self.city}, Address Line 1: {self.address_line1}, Address Line 2: {self.address_line2}, Zip Code: {self.zip_code}"