from customer import *
from datetime import datetime
class RentalSystem:
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.vehicles = {}
        self.customers = {}
    def add_vehicle(self, vehicle: Vehicle) -> None:
        self.vehicles[vehicle.vehicle_id] = vehicle
    def add_customer(self, customer: Customer) -> None:
        self.customers[customer.customer_id] = customer
    def find_vehicle(self, vehicle_id: str) -> Vehicle | None:
        try:
            return self.vehicles[vehicle_id]
        except KeyError:
            return None
    def find_customer(self, customer_id: str) -> Customer | None:
        try:
            return self.customers[customer_id]
        except KeyError:
            return None
    def get_available_vehicles(self) -> list:
        return list(i for i in self.vehicles.values() if i.is_available)
    def get_vehicles_by_type(self, vehicle_type: str) -> list:
        if vehicle_type == "EconomyCar":
            return [i for i in self.vehicles.values() if i.__class__.__name__ == "EconomyCar"]
        elif vehicle_type == "SUV":
            return [i for i in self.vehicles.values() if i.__class__.__name__ == "SUV"]
        elif vehicle_type == "LuxuryCar":
            return [i for i in self.vehicles.values() if i.__class__.__name__ == "LuxuryCar"]
        else:
            return []
    def get_total_revenue(self) -> float:
        return sum(i.get_total_spent() for i in self.customers.values() )
    def get_most_popular_vehicle(self) -> str:
        res = {}
        for i in self.customers.values():
            for car in i.rental_history:
                res[car[0]] = res.get(car[0], 0) + 1
        max_count = 0
        max_name = ""
        for  key, val in res.items():
            if val > max_count:
                max_count = val
                max_name = key
        return max_name
    def revenue_and_days_by_type(self, car_type: str) -> tuple[int,float]: #დამატებითი ფუნქცია,რომელსაც ვიყენებ generate_report() ფუნქციაში
        keyword = ""
        if car_type == "EconomyCar":
            keyword = "ECO"
        elif car_type == "SUV":
            keyword = "SUV"
        else:
            keyword = "LUX"
        total_rev = 0
        total_days = 0
        amnt = 0
        for i in self.customers.values():
            for a in i.rental_history:
                if a[0].startswith(keyword):
                    total_rev += a[-1]
                    total_days += a[2]
                    amnt += 1
        try:
            average_days = total_days / amnt
        except ZeroDivisionError:
            average_days = 0
        return (total_rev, average_days)
    def generate_report(self, filename: str) -> None:
        with open(filename, "w", encoding = "utf-8") as file:
            file.write("═══════════════════════════════════════════════\n")
            file.write(f"        {self.company_name} - ანგარიში        \n")
            file.write("═══════════════════════════════════════════════\n")
            file.write(f"თარიღი: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            file.write(f"ᲛᲐᲜᲥᲐᲜᲔᲑᲘᲡ ᲡᲢᲐᲢᲘᲡᲢᲘᲙᲐ:\n")
            file.write("------------------------\n")
            file.write(f"ჯამური მანქანები: {len(self.vehicles)}\n")
            file.write(f"  - ეკონომ კლასი: {len(self.get_vehicles_by_type('EconomyCar'))}\n")
            file.write(f"  - SUV: {len(self.get_vehicles_by_type('SUV'))}\n")
            file.write(f"  - ლუქსი: {len(self.get_vehicles_by_type('LuxuryCar'))}\n\n")
            file.write(f"ხელმისაწვდომი: {len(self.get_available_vehicles())}\n")
            file.write(f"დაქირავებული: {len(self.vehicles) - len(self.get_available_vehicles())}\n\n")
            file.write(f"ᲙᲚᲘᲔᲜᲢᲔᲑᲘᲡ ᲡᲢᲐᲢᲘᲡᲢᲘᲙᲐ:\n")
            file.write("------------------------\n")
            file.write(f"რეგისტრირებული კლიენტები: {len(self.customers)}\n")
            file.write(f"აქტიური დაქირავებები: {len([i for i in self.customers.values() if len(i.current_rentals) != 0])}\n\n")
            file.write(f"ᲤᲘᲜᲐᲜᲡᲣᲠᲘ ᲐᲜᲒᲐᲠᲘᲨᲘ:\n")
            file.write("------------------------\n")
            file.write(f"ჯამური შემოსავალი: {self.get_total_revenue()} ლარი\n")
            file.write(f"ყველაზე პოპულარული: {self.get_most_popular_vehicle()} ({self.vehicles[self.get_most_popular_vehicle()]})\n\n")
            file.write(f"TOP 3 ᲙᲚᲘᲔᲜᲢᲘ:\n")
            file.write("------------------------\n")
            sorted_list = sorted([(i.get_total_spent(), i.name) for i in self.customers.values()])
            file.write(f"1. {sorted_list[-1][1]} - {sorted_list[-1][0]} ლარი\n")
            file.write(f"2. {sorted_list[-2][1]} - {sorted_list[-2][0]} ლარი\n")
            file.write(f"3. {sorted_list[-3][1]} - {sorted_list[-3][0]} ლარი\n\n")
            file.write(f"ᲓᲔᲢᲐᲚᲣᲠᲘ ᲡᲢᲐᲢᲘᲡᲢᲘᲙᲐ ᲢᲘᲞᲔᲑᲘᲡ ᲛᲘᲮᲔᲓᲕᲘᲗ:\n")
            file.write("------------------------\n\n")
            for c in ["EconomyCar","SUV","LuxuryCar"]:
                if c == "EconomyCar":
                    file.write(f"📊 ᲔᲙᲝᲜᲝᲛ ᲙᲚᲐᲡᲘ (EconomyCar):\n")
                elif c == "SUV":
                    file.write(f"📊 SUV ᲙᲚᲐᲡᲘ:\n")
                else:
                    file.write(f"📊 ᲚᲣᲥᲡ ᲙᲚᲐᲡᲘ (LuxuryCar):\n")
                file.write(f"   ჯამური მანქანები: {len(self.get_vehicles_by_type(c))}\n")
                file.write(f"   ხელმისაწვდომი: {len([i for i in self.get_vehicles_by_type(c) if i.is_available])}\n")
                file.write(f"   დაქირავებული: {len([i for i in self.get_vehicles_by_type(c) if not i.is_available])}\n\n")
                file.write(f"მანქანების სია:\n")
                for i in self.get_vehicles_by_type(c):
                    file.write(f"{i.vehicle_id} - {i.brand} {i.model} ({i.year}) - {i.daily_rate} ლარი/დღე - {'ხელმისაწვდომი' if i.is_available else 'დაქირავებული'}\n")
                file.write("\n")
                file.write(f"   საერთო შემოსავალი ამ ტიპიდან: {self.revenue_and_days_by_type(c)[0]}\n")
                file.write(f"   საშუალო დაქირავების ხანგრძლივობა: {self.revenue_and_days_by_type(c)[1]:.1f}\n\n")
            file.write("═══════════════════════════════════════════════\n")
            file.write("              ანგარიშის დასასრული              \n")
            file.write("═══════════════════════════════════════════════\n")