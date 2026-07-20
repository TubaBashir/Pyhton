def convert_number(value_str, from_base):
    """
    Takes an input string and its current base, parses it to an integer,
    and returns its representations in all four standard bases.
    """
    # 1. Parse the string into a standard decimal integer based on its input type
    try:
        decimal_val = int(value_str.strip(), from_base)
    except ValueError:
        return None

    # 2. Convert the standard integer out to all formatting targets
    # We use string slicing [2:] to strip off the prefixes (0b, 0o, 0x)
    return {
        "decimal": str(decimal_val),
        "binary": bin(decimal_val)[2:],
        "octal": oct(decimal_val)[2:],
        "hexadecimal": hex(decimal_val)[2:].upper()
    }

def main():
    print("🔢 Universal Number System Converter")
    print("Select your input base:")
    print("1. Decimal (Base 10)\n2. Binary (Base 2)\n3. Octal (Base 8)\n4. Hexadecimal (Base 16)")
    
    choice = input("Enter choice (1-4): ").strip()
    
    # Map selection choices to numeric base values
    base_map = {"1": 10, "2": 2, "3": 8, "4": 16}
    
    if choice not in base_map:
        print("❌ Invalid base selection.")
        return
        
    target_base = base_map[choice]
    user_input = input("Enter the number to convert: ")
    
    results = convert_number(user_input, target_base)
    
    if results is None:
        print(f"❌ Error: '{user_input}' is not a valid base-{target_base} number!")
    else:
        print(f"\n📊 Conversions for input '{user_input}':")
        print(f"🔹 Decimal (Base 10) : {results['decimal']}")
        print(f"🔹 Binary (Base 2)   : {results['binary']}")
        print(f"🔹 Octal (Base 8)    : {results['octal']}")
        print(f"🔹 Hexadecimal (16)  : {results['hexadecimal']}")

if __name__ == "__main__":
    main()
