 Water Billing System Algorithm

## Step-by-Step Process:

1. *START*
2. *Display Menu*
   - Add Customer
   - Record Reading
   - Calculate Bill
   - View Reports
   - Exit
3. *Get User Choice*
4. *IF* choice is Add Customer:
   - Input customer name, address, meter number
   - Save to database/file
5. *IF* choice is Record Reading:
   - Input meter number
   - Input current reading
   - Calculate consumption (current - previous)
   - Save reading
6. *IF* choice is Calculate Bill:
   - Get consumption units
   - Apply tariff rate
   - Calculate total amount
   - Generate bill
7. *IF* choice is View Reports:
   - Display all customers and their bills
8. *Loop* back to step 2 until Exit
9. *END*

## Billing Formula:
- Consumption = Current Reading - Previous Reading
- Bill Amount = Consumption × Rate per Unit
