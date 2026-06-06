[12:01, 6/6/2026] UMMU-HILDAT: # Water Billing System

customers = {}
readings = {}
RATE = 5.0

def add_customer():
    meter = input("Meter number: ")
    name = input("Name: ")
    address = input("Address: ")
    customers[meter] = {'name': name, 'address': address}
    print("Customer added!")

def record_reading():
    meter = input("Meter number: ")
    reading = float(input("Current reading: "))
    readings[meter] = reading
    print("Reading recorded!")

def calculate_bill():
    meter = input("Meter number: ")
    if meter in readings:
        consumption = readings[meter]
        bill = consumption * RATE
        print(f"Bill: ${bill:.2f}")
    else:
        print("No reading found!")

def main():
    while True:
        print("\n1. Add Customer")
        print("2. Record Readi…
[12:43, 6/6/2026] UMMU-HILDAT: # Water Billing System

customers = {}
meter_readings = {}
RATE = 5.0

def add_customer():
    meter = input("Meter number: ")
    name = input("Name: ")
    address = input("Address: ")
    customers[meter] = {'name': name, 'address': address}
    meter_readings[meter] = {'previous': 0, 'current': 0}
    print("Customer added!")

def record_reading():
    meter = input("Meter number: ")
    if meter not in customers:
        print("Customer not found!")
        return
    old_current = meter_readings[meter]['current']
    meter_readings[meter]['previous'] = old_current
    new_reading = float(input("Enter current reading: "))
    meter_readings[meter]['current'] = new_reading
    print("Reading recorded!")

def calculate_bill():
    meter = input("Meter number: ")
    if meter in meter_readings:
        current = meter_readings[meter]['current']
        previous = meter_readings[meter]['previous']
        consumption = current - previous
        if consumption < 0:
            print("Error: Current reading cannot be less than previous!")
            return
        bill = consumption * RATE
        print("\n--- BILL ---")
        print(f"Previous Reading: {previous}")
        print(f"Current Reading: {current}")
        print(f"Consumption: {consumption} units")
        print(f"Rate: ${RATE}")
        print(f"Total Bill: ${bill:.2f}")
        print("------------")
    else:
        print("No reading found!")

def main():
    while True:
        print("\n1. Add Customer")
        print("2. Record Reading")
        print("3. Calculate Bill")
        print("4. Exit")
        choice = input("Choice: ")
        if choice == '1':
            add_customer()
        elif choice == '2':
            record_reading()
        elif choice == '3':
            calculate_bill()
        elif choice == '4':
            break

if _name_ == "_main_":
    main()
