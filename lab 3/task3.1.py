def calculate_power_bill():
    """
    Calculate the power bill based on units consumed.
    Slab rates:
        - First 100 units: Rs. 5 per unit
        - Next 100 units (101-200): Rs. 7 per unit
        - Above 200 units: Rs. 10 per unit
    """
    try:
        units = int(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return
        if units <= 100:
            bill = units * 5
        elif units <= 200:
            bill = 100 * 5 + (units - 100) * 7
        else:
            bill = 100 * 5 + 100 * 7 + (units - 200) * 10
        print(f"Total power bill for {units} units is Rs. {bill}")
    except ValueError:
        print("Please enter a valid integer for units.")

calculate_power_bill()

