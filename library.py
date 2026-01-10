def convert_temperature():
    print("--- Universal Temperature Converter ---")
    print("Choose the input unit:")
    print("1. Celsius (C)")
    print("2. Fahrenheit (F)")
    print("3. Kelvin (K)")
    
    choice = input("Enter choice (1/2/3): ")
    
    try:
        temp = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input! Please enter a numerical value.")
        return

    if choice == '1': # Input is Celsius
        f = (temp * 1.8) + 32
        k = temp + 273.15
        print(f"{temp}°C is equal to {f:.2f}°F and {k:.2f}K")
        
    elif choice == '2': # Input is Fahrenheit
        c = (temp - 32) / 1.8
        k = c + 273.15
        print(f"{temp}°F is equal to {c:.2f}°C and {k:.2f}K")
        
    elif choice == '3': # Input is Kelvin
        c = temp - 273.15
        f = (c * 1.8) + 32
        print(f"{temp}K is equal to {c:.2f}°C and {f:.2f}°F")
        
    else:
        print("Invalid unit selection.")

if __name__ == "__main__":
    convert_temperature()
