# Algorithm

## Water Billing Calculation

1. Read customer meter number
2. Get previous reading from database
3. Input current reading
4. Calculate consumption:
   - consumption = current_reading - previous_reading
5. Calculate bill:
   - bill = consumption × rate_per_unit
6. Generate bill receipt
7. Update database with new reading
