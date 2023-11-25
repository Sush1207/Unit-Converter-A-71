def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice")

def length_converter():
    print("Length Converter")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is equal to {feet} feet")
    elif choice == 2:
        feet = float(input("Enter length in feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is equal to {meters} meters")
    else:
        print("Invalid choice")

def weight_converter():
    print("Weight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kilograms is equal to {pounds} pounds")
    elif choice == 2:
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds / 2.20462
        print(f"{pounds} pounds is equal to {kilograms} kilograms")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    print("Unit Converter")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")
    option = int(input("Enter your choice (1, 2, or 3): "))

    if option == 1:
        temperature_converter()
    elif option == 2:
        length_converter()
    elif option == 3:
        weight_converter()
    else:
        print("Invalid choice")
