def convert_temperature():
    """
    Convert temperature between Celsius and Fahrenheit.
    Prompts the user for the conversion direction and the temperature value.
    """
    print("Temperature Converter")
    print("This program converts temperatures between Celsius and Fahrenheit.")
    print("Enter 'c' to convert Celsius to Fahrenheit.")
    print("Enter 'f' to convert Fahrenheit to Celsius.")
    choice = input("Enter your choice (c/f): ").strip().lower()
    if choice == 'c':
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a valid number for temperature.")
    elif choice == 'f':
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a valid number for temperature.")
    else:
        print("Invalid choice. Please enter 'c' or 'f'.")
convert_temperature()



