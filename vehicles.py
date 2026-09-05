class Vehicle:
    _vehicle_counter = 0
    def __init__(self, brand: str, model: str, year: int, daily_rate: float):
        Vehicle._vehicle_counter += 1
        self.vehicle_id = f"V{Vehicle._vehicle_counter:03d}"
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.is_available = True
    def calculate_rental_cost(self, days: int) -> float:
        return self.daily_rate * days
    def rent(self) -> bool:
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False
    def return_vehicle(self) -> None:
        self.is_available = True
    def get_info(self) -> str:
        return f"მარკა: {self.brand}, მოდელი: {self.model}, წელი: {self.year}, ფასი: {self.daily_rate}, სტატუსი: {'ხელმისაწვდომი' if self.is_available else 'დაქირავებული'}"
    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"
class EconomyCar(Vehicle):
    _eco_counter = 0
    def __init__(self, brand: str, model: str, year: int, daily_rate: float, fuel_efficiency: float):
        super().__init__(brand, model, year, daily_rate)
        EconomyCar._eco_counter += 1
        vehicle_id = f"ECO{EconomyCar._eco_counter:03d}"
        self.vehicle_id = vehicle_id
        self.fuel_efficiency = fuel_efficiency
    def calculate_rental_cost(self, days: int) -> float:
        return self.daily_rate * days * 0.85 if days >= 7 else self.daily_rate * days
    def get_fuel_info(self) -> str:
        return f"საწვავის ხარჯვა: {self.fuel_efficiency} ლ/100კმ (ეკონომიური)"
class SUV(Vehicle):
    _suv_counter = 0
    def __init__(self, brand: str, model: str, year: int, daily_rate: float, seats: int, has_4wd: bool):
        super().__init__(brand, model, year, daily_rate)
        SUV._suv_counter += 1
        vehicle_id = f"SUV{SUV._suv_counter:03d}"
        self.vehicle_id = vehicle_id
        self.seats = seats
        self.has_4wd = has_4wd
    def calculate_rental_cost(self, days: int) -> float:
        return (self.daily_rate + 10) * days
    def get_capacity_info(self) -> str:
        otxiotxze = "✓" if self.has_4wd else 'x'
        return f"ადგილები: {self.seats} | 4x4: {otxiotxze}"
class LuxuryCar(Vehicle):
    _luxury_counter = 0
    def __init__(self, brand: str, model: str, year: int, daily_rate: float, features: list, requires_deposit: bool = True):
        super().__init__(brand, model, year, daily_rate)
        LuxuryCar._luxury_counter += 1
        vehicle_id = f"LUX{LuxuryCar._luxury_counter:03d}"
        self.vehicle_id = vehicle_id
        self.features = features
        self.requires_deposit = requires_deposit
    def calculate_rental_cost(self, days: int) -> float:
        return (self.daily_rate + 20) * days
    def get_deposit_amount(self) -> float:
        return self.daily_rate * 3