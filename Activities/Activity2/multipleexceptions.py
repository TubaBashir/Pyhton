def divide_user_inputs():
    try:
        # Potential ValueError if input is not a number
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        
        # Potential ZeroDivisionError if num2 is 0
        result = num1 / num2
        print(f"📊 Result: {result}")
        
    except ValueError:
        print("❌ Input Error: Please enter numeric values only.")
        
    except ZeroDivisionError:
        print("❌ Math Error: Cannot divide a number by zero.")

divide_user_inputs()
