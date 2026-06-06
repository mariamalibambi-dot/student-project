# Water Billing System

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
