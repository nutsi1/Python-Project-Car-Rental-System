#customer.py
from vehicles import *
class Customer:
    _customer_counter = 0
    def __init__(self, name: str, license_number: str, phone: str):
        Customer._customer_counter += 1
        self.customer_id = f"CUST{Customer._customer_counter:03d}"
        self.name = name
        self.license_number = license_number
        self.phone = phone
        self.current_rentals = []
        self.rental_history = []
    def rent_vehicle(self, vehicle: Vehicle, days: int, start_date: str) -> bool:
        if not vehicle.is_available:
            return False
        else:
            self.current_rentals.append((vehicle.vehicle_id, start_date, days, vehicle.calculate_rental_cost(days)))
            vehicle.rent()
            return True
    def return_vehicle(self, vehicle: Vehicle, days_late: int = 0) -> float:
        if vehicle.vehicle_id not in [i[0] for i in self.current_rentals]:
            return 0.0
        else:
            days_late = max(days_late, 0)
            late_fee = vehicle.daily_rate * 1.5 * days_late
            index_count = 0
            total_cost = 0
            for i in self.current_rentals:
                if i[0] == vehicle.vehicle_id:
                    total_cost = i[-1]
                    break
                index_count += 1
            self.rental_history.append(
                (vehicle.vehicle_id, self.current_rentals[index_count][1], self.current_rentals[index_count][2],
                 self.current_rentals[index_count][3], days_late, total_cost + late_fee))
            self.current_rentals.pop(index_count)
            vehicle.return_vehicle()
            return late_fee + total_cost
    def get_current_rentals(self) -> list:
        return self.current_rentals

    def get_rental_history(self) -> str:
        if not self.rental_history:
            return "დაქირავებების ისტორია ცარიელია."
        header = (
            f"{'ID':<12} "
            f"{'თარიღი':<15} "
            f"{'დღეები':<9} "
            f"{'ფასი':<10} "
            f"{'დაგვიანება':<10}   "
            f"{'გადასახადი':<12}"
        )

        line = "-" * len(header)
        rows = [header, line]

        for vehicle_id, start_date, days, cost, days_late, total in self.rental_history:
            rows.append(
                f"{vehicle_id:<12} "
                f"{str(start_date):<15} "
                f"{days:<9} "
                f"{cost:<10.2f} "
                f"{days_late:<10} "
                f"{total:<12.2f}"
            )

        return "\n".join(rows)
    def get_total_spent(self) -> float:
        res = 0
        for i in self.rental_history:
            res += i[-1]
        return res
    def __str__(self) -> str:
        return f"Customer: {self.name} (ID: {self.customer_id})"