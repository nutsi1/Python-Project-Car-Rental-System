from rental_system import *
system = RentalSystem("Car Renting")
car1 = EconomyCar("Toyota", "Yaris", 2023, 45.0 , 10.9)
car2 = EconomyCar("Hyundai", "i10", 2022, 40.0, 11.9)
car3 = EconomyCar("Kia", "Rio", 2023, 48.0 , 10.14)
car4 = EconomyCar("Toyota", "Corolla", 2022,50.0, 17.1)
car5 = EconomyCar("Volkswagen", "Polo", 2023,47.0, 15.0)
car6 = SUV("Toyota", "RAV4", 2023,80.0, 4, False)
car7 = SUV("Honda", "CR-V", 2022,71.0, 4, True)
car8 = SUV("Nissan", "X-Trail", 2023,78.0 , 8, True)
car9 = LuxuryCar("BMW", "X5", 2024, 150.0, ["პრემიუმ აუდიო სისტემა", "360° კამერები"], False)
car10 = LuxuryCar("Mercedes", "GLE", 2024, 160.0, ["სპორტული მართვის რეჟიმი"], True)

system.add_vehicle(car1)
system.add_vehicle(car2)
system.add_vehicle(car3)
system.add_vehicle(car4)
system.add_vehicle(car5)
system.add_vehicle(car6)
system.add_vehicle(car7)
system.add_vehicle(car8)
system.add_vehicle(car9)
system.add_vehicle(car10)

customer1 = Customer("ნუცა ბალაშვილი", "001222", "555472911")
customer2 = Customer("სალომე კაკაბაძე", "001223", "579326011")
customer3 = Customer("მაია დოლიძე", "001224", "555101021")
customer4 = Customer("ნიკოლოზ სიგუა", "001225", "558781109")
customer5 = Customer("გიორგი გორგაძე", "001226", "551809154")

system.add_customer(customer1)
system.add_customer(customer2)
system.add_customer(customer3)
system.add_customer(customer4)
system.add_customer(customer5)

customer1.rent_vehicle(car1, 3, "2025-12-16")
customer1.rent_vehicle(car2, 1, "2025-12-15")
customer1.return_vehicle(car2, 2)

customer1.return_vehicle(car1)
customer1.rent_vehicle(car6, 2, "2025-12-16")

customer2.rent_vehicle(car1, 3, "2025-12-16")
customer2.rent_vehicle(car7, 1, "2025-12-16")
customer2.return_vehicle(car7, 1)

customer3.rent_vehicle(car4, 2, "2025-12-16")
customer3.rent_vehicle(car5, 2, "2025-12-16")
customer3.rent_vehicle(car8, 1, "2025-12-16")
customer3.return_vehicle(car4, 2)
customer3.return_vehicle(car5)

customer4.rent_vehicle(car4, 2, "2025-12-16")
customer4.return_vehicle(car4, 2)

customer5.rent_vehicle(car5, 5, "2025-12-16")
customer5.return_vehicle(car5)
customer5.rent_vehicle(car10, 1, "2025-12-16")
customer5.return_vehicle(car10, 3)

while True:
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(f"          {system.company_name} - მენიუ        ")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("1. მანქანების ფუნქციონალი")
    print("2. მომხმარებლების ფუნქციონალი")
    print("3. Admin ფუნქციონალი")
    print("4. პროგრამის დასრულება\n")
    choice = input("შეიყვანეთ სასურველი ოპერაცია(1-4):\n")
    if choice == "1":
        while True:
            print("1. გადასახადის გამოთვლა(დღეების მიხედვით)")
            print("2. მაქანის აღწერა")
            print("3. საწვავის ხარჯვა(მხოლოდ ეკონომიური მანქანებისთვის)")
            print("4. გაბარიტების ინფორმაცია(მხოლოდ SUV მანქანებისთვის)")
            print("5. დეპოზიტის რაოდენობის გამოთვლა(მხოლოდ ლუქს მანქანებისთვის)")
            print("6. უკან დაბრუნება\n")
            op = input("აირჩიეთ(1-6):\n")
            if op == "6":
                break
            elif op == "1":
                car_id = input("შეიყვანეთ მანქანის ID: ")
                try:
                    days = int(input("შეიყვანეთ დღეების რაოდენობა: \n"))
                except ValueError:
                    days = 0
                if car_id not in system.vehicles.keys() or days <= 0:
                    print("არავალიდური მონაცემები.\n")
                else:
                    print(f"გადასახადი შეადგენს: {system.vehicles[car_id].calculate_rental_cost(days)} ლარს.\n")
            elif op == "2":
                car_id = input("შეიყვანეთ მანქანის ID: \n")
                if car_id not in system.vehicles.keys():
                    print("არავალიდური მონაცემები.\n")
                else:
                    print(f"{system.vehicles[car_id].get_info()}")
            elif op == "3":
                car_id = input("შეიყვანეთ მანქანის ID: \n")
                if car_id not in system.vehicles.keys():
                    print("არავალიდური მონაცემები.\n")
                elif not isinstance(system.vehicles[car_id], EconomyCar):
                    print("არ არის ეკონომ ტიპის მანქანა.\n")
                else:
                    print(f"{system.vehicles[car_id].get_fuel_info()}\n")
            elif op == "4":
                car_id = input("შეიყვანეთ მანქანის ID: \n")
                if car_id not in system.vehicles.keys():
                    print("არავალიდური მონაცემები.\n")
                elif not isinstance(system.vehicles[car_id], SUV):
                    print("არ არის SUV ტიპის მანქანა.\n")
                else:
                    print(f"{system.vehicles[car_id].get_capacity_info()}\n")
            elif op == "5":
                car_id = input("შეიყვანეთ მანქანის ID: \n")
                if car_id not in system.vehicles.keys():
                    print("არავალიდური მონაცემები.\n")
                elif not isinstance(system.vehicles[car_id], LuxuryCar):
                    print("არ არის ლუქს ტიპის მანქანა.\n")
                else:
                    if system.vehicles[car_id].requires_deposit:
                        print(f"დეპოზიტის რაოდენობა: {system.vehicles[car_id].get_deposit_amount()}.\n")
                    else:
                        print(f"დეპოზიტი არ არის საჭირო.\n")
            else:
                print("არჩეული ოპერაცია არ მოიძებნება\n")
    elif choice == "2":
        while True:
            print("1. მანქანის დაქირავება")
            print("2. მანქანის დაბრუნება")
            print("3. მიმდინარე დაქირავებები")
            print("4. დაქირავებების ისტორია")
            print("5. მთლიანი დანახარჯის გამოთვლა")
            print("6. უკან დაბრუნება\n")
            op = input("აირჩიეთ(1-6):\n")
            if op == "6":
                break
            elif op == "1":
                per_id = input("შეიყვანეთ მომხმარებლის ID: ")
                car_id = input("შეიყვანეთ მანქანის ID: ")
                try:
                    days = int(input("შეიყვანეთ დღეების რაოდენობა: "))
                except ValueError:
                    days = 0
                date = input("შეიყვანეთ თარიღი(YYYY-MM-DD):\n")
                try:
                    valid_date = datetime.strptime(date, "%Y-%m-%d").date()
                except ValueError:
                    valid_date = None
                if per_id not in system.customers.keys() or car_id not in system.vehicles.keys() or days <= 0 or valid_date is None:
                    print("არავალიდური მონაცემები.\n")
                else:
                    ans = system.customers[per_id].rent_vehicle(system.vehicles[car_id], days, date)
                    if ans:
                        print("წარმატებით გაქირავდა.\n")
                    else:
                        print("მანქანა უკვე დაქირავებულია.\n")
            elif op == "2":
                per_id = input("შეიყვანეთ მომხმარებლის ID: ")
                car_id = input("შეიყვანეთ მანქანის ID: ")
                try:
                    days = int(input("შეიყვანეთ დაგვიანებული დღეების რაოდენობა: \n"))
                except ValueError:
                    days = -1
                if per_id not in system.customers.keys() or car_id not in system.vehicles.keys() or days < 0:
                    print("არავალიდური მონაცემები.\n")
                else:
                    ans = system.customers[per_id].return_vehicle(system.vehicles[car_id], days)
                    if ans == 0.0:
                        print("მომხმარებელს ეს მანქანა არ ჰყავდა დაქირავებული.\n")
                    else:
                        print(f"მანქანა დაბრუნებულია, გადასახდელია {ans} ლარი.\n")
            elif op == "3":
                per_id = input("შეიყვანეთ მომხმარებლის ID: \n")
                if per_id not in system.customers.keys():
                    print("არავალიდური მონაცემები.\n")
                else:
                    if len(system.customers[per_id].get_current_rentals()) == 0:
                        print("მიმდინარე დაქირავებები ვერ მოიძებნა.\n")
                    else:
                        print(system.customers[per_id].get_current_rentals())
            elif op == "4":
                per_id = input("შეიყვანეთ მომხმარებლის ID: \n")
                if per_id not in system.customers.keys():
                    print("არავალიდური მონაცემები.\n")
                else:
                    print(system.customers[per_id].get_rental_history() + "\n")
            elif op == "5":
                per_id = input("შეიყვანეთ მომხმარებლის ID: \n")
                if per_id not in system.customers.keys():
                    print("არავალიდური მონაცემები.\n")
                else:
                    print(f"სულ დახარჯულია {system.customers[per_id].get_total_spent()}\n")
            else:
                print("არჩეული ოპერაცია არ მოიძებნება\n")
    elif choice == "3":
        while True:
            print("1. მანქანის დამატება")
            print("2. მომხმარებლის დამატება")
            print("3. მანქანის ძებნა(ID-ით)")
            print("4. მომხმარებლის ძებნა(ID-ით)")
            print("5. ხელმისაწვდომი მანქანები")
            print("6. მანქანები ტიპის მიხედვით")
            print("7. მთლიანი შემოსავლის გამოთვლა")
            print("8. ყველაზე პოპულარული მანქანა")
            print("9. დეტალური ანგარიში")
            print("10. უკან დაბრუნება\n")
            op = input("აირჩიეთ(1-10):\n")
            if op == "10":
                break
            elif op == "1":
                print("1. ეკონომ მანქანა")
                print("2. SUV")
                print("3. ლუქს მანქანა\n")
                car_type = input("აირჩიეთ მანქანის ტიპი(1-3):\n")
                if car_type == "1":
                    brand = input("მიუთითეთ ბრენდი: ")
                    model = input("მიუთითეთ მოდელი: ")
                    try:
                        year = int(input("მიუთითეთ წელი: "))
                    except ValueError:
                        year = 0
                    try:
                        rate = float(input("მიუთითეთ დღიური ფასი: "))
                    except ValueError:
                        rate = 0
                    try:
                        fuel = float(input("მიუთითეთ საწვავის ხარჯვა(ლ/100კმ): \n"))
                    except ValueError:
                        fuel = 0
                    if rate <= 0 or fuel <= 0 or year < 1990 or year > 2025:
                        print("არავალიდური მონაცემები.\n")
                    else:
                        system.add_vehicle(EconomyCar(brand, model, year, rate, fuel))
                        print("მანქანა წარმატებით დაემატა.\n")
                elif car_type == "2":
                    brand = input("მიუთითეთ ბრენდი: ")
                    model = input("მიუთითეთ მოდელი: ")
                    try:
                        year = int(input("მიუთითეთ წელი: "))
                    except ValueError:
                        year = 0
                    try:
                        rate = float(input("მიუთითეთ დღიური ფასი: "))
                    except ValueError:
                        rate = 0
                    try:
                        seats = int(input("მიუთითეთ ადგილების რაოდენობა: "))
                    except ValueError:
                        seats = 0
                    try:
                        has4x4 = bool(input("მიუთითეთ აქვს თუ არა 4x4 სისტემა(True/False): \n"))
                    except ValueError:
                        has4x4 = None
                    if rate <= 0 or seats <= 0 or year < 1990 or year > 2025 or has4x4 is None:
                        print("არავალიდური მონაცემები.\n")
                    else:
                        system.add_vehicle(SUV(brand, model, year, rate, seats, has4x4))
                        print("მანქანა წარმატებით დაემატა.\n")
                elif car_type == "3":
                    brand = input("მიუთითეთ ბრენდი: ")
                    model = input("მიუთითეთ მოდელი: ")
                    try:
                        year = int(input("მიუთითეთ წელი: "))
                    except ValueError:
                        year = 0
                    try:
                        rate = float(input("მიუთითეთ დღიური ფასი: "))
                    except ValueError:
                        rate = 0
                    features = input("მიუთითეთ მახასიათებლები(გამოყავით მძიმით): ")
                    try:
                        deposit = bool(input("მიუთითეთ საჭიროებს თუ არა დეპოზიტს(True/False): \n"))
                    except ValueError:
                        deposit = None
                    if rate <= 0 or year < 1990 or year > 2025 or ',' not in features or deposit is None:
                        print("არავალიდური მონაცემები.\n")
                    else:
                        system.add_vehicle(LuxuryCar(brand, model, year, rate, features.split(','), deposit))
                        print("მანქანა წარმატებით დაემატა.\n")
                else:
                    print("არავალიდური მონაცემები.\n")
            elif op == "2":
                name = input("შეიყვანეთ მომხმარებლის სახელი: ")
                dl_number = input("შეიყვანეთ მართვის მოწმობის ნომერი: ")
                ph_number = input("შეიყვანეთ ტელეფონის ნომერი: \n")
                if not ph_number.startswith("5") or len(ph_number) != 9:
                    print("არავალიდური მონაცემები.\n")
                else:
                    system.add_customer(Customer(name, dl_number, ph_number))
                    print("მომხმარებელი წარმატებით დაემატა.\n")
            elif op == "3":
                car_id = input("შეიყვანეთ მანქანის ID: \n")
                car = system.find_vehicle(car_id)
                if car is None:
                    print("ამ ID-ით მანქანა არ იძებნება.\n")
                else:
                    print(car)
            elif op == "4":
                person = input("შეიყვანეთ მომხმარებლის ID: \n")
                if person is None:
                    print("ამ ID-ით მომხმარებელი არ იძებნება.\n")
                else:
                    print(system.find_customer(person))
            elif op == "5":
                if len(system.get_available_vehicles())  == 0:
                    print("არცერთი მანქანა არაა ხელმისაწვდომი.")
                else:
                    for i in  system.get_available_vehicles():
                        print(i)
            elif op == "6":
                car_type = input("შეიყვანეთ მანქანის ტიპი(EconomyCar, SUV, LuxuryCar): \n")
                if car_type not in ["EconomyCar", "SUV", "LuxuryCar"]:
                    print("არავალიდური მონაცემები.\n")
                else:
                    for i in system.get_vehicles_by_type(car_type):
                        print(i)
            elif op == "7":
                print(f"საერთო შემოსავალი: {system.get_total_revenue()}")
            elif op == "8":
                print(f"ყველაზე პოპულარული მანქანა: {system.vehicles[system.get_most_popular_vehicle()]}")
            elif op == "9":
                file_name = input("მიუთითეთ ფაილის სახელი: \n")
                system.generate_report(file_name + '.txt')
                print("ფაილი წარმტებით დაგენერირდა.\n")
            else:
                print("არჩეული ოპერაცია არ მოიძებნება\n")
    elif choice == "4":
        print("მომსახურება დასრულებულია.")
        break
    else:
        print("არჩეული ოპერაცია არ მოიძებნება\n")