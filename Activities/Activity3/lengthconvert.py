class LengthConverter:
    """
    A comprehensive length converter that converts between metric and imperial units
    by normalizing all values to meters as the base unit.
    """
    
    # Conversion factors relative to 1 meter (Base Unit = meters)
    CONVERSION_TO_METERS = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }
    
    UNIT_NAMES = {
        'mm': 'Millimeters',
        'cm': 'Centimeters',
        'm': 'Meters',
        'km': 'Kilometers',
        'in': 'Inches',
        'ft': 'Feet',
        'yd': 'Yards',
        'mi': 'Miles'
    }

    def __init__(self, value: float, unit_from: str):
        self.value = value
        self.unit_from = unit_from.lower()
        
        if self.unit_from not in self.CONVERSION_TO_METERS:
            raise ValueError(f"Invalid unit '{unit_from}'. Supported units: {list(self.CONVERSION_TO_METERS.keys())}")

    def convert_to(self, unit_to: str) -> float:
        unit_to = unit_to.lower()
        if unit_to not in self.CONVERSION_TO_METERS:
            raise ValueError(f"Invalid target unit '{unit_to}'. Supported units: {list(self.CONVERSION_TO_METERS.keys())}")
        
        # Step 1: Convert input value to meters
        value_in_meters = self.value * self.CONVERSION_TO_METERS[self.unit_from]
        
        # Step 2: Convert from meters to the target unit
        result = value_in_meters / self.CONVERSION_TO_METERS[unit_to]
        return result

    def convert_to_all(self) -> dict:
        """Converts the stored value into all available length units."""
        return {unit: self.convert_to(unit) for unit in self.CONVERSION_TO_METERS.keys()}


def display_menu():
    print("\n" + "=" * 45)
    print("      📏 ADVANCED PYTHON LENGTH CONVERTER      ")
    print("=" * 45)
    print("Supported Units:")
    print("  mm : Millimeters  |  cm : Centimeters  |  m  : Meters")
    print("  km : Kilometers   |  in : Inches       |  ft : Feet")
    print("  yd : Yards        |  mi : Miles")
    print("-" * 45)


def main():
    display_menu()
    
    while True:
        try:
            print("\nEnter 'q' to quit the application.")
            val_input = input("Enter the numerical value to convert: ").strip()
            if val_input.lower() == 'q':
                print("Exiting Length Converter. Goodbye!")
                break
                
            value = float(val_input)
            
            unit_from = input("Enter source unit (e.g., m, ft, km, in): ").strip().lower()
            if unit_from == 'q':
                break
                
            # Initialize converter instance
            converter = LengthConverter(value, unit_from)
            
            print("\nChoose conversion mode:")
            print("1. Convert to a single specific unit")
            print("2. Convert to ALL units at once (Big Example view)")
            choice = input("Select option (1 or 2): ").strip()
            
            if choice == '1':
                unit_to = input("Enter target unit (e.g., cm, yd, mi): ").strip().lower()
                converted_val = converter.convert_to(unit_to)
                print(f"\n✅ {value} {converter.UNIT_NAMES[unit_from]} = {converted_val:.6f} {converter.UNIT_NAMES[unit_to]}")
                
            elif choice == '2':
                print(f"\n📊 Conversion breakdown for {value} {converter.UNIT_NAMES[unit_from]}:")
                all_results = converter.convert_to_all()
                for unit, res in all_results.items():
                    print(f"   • {res:12.6f} {converter.UNIT_NAMES[unit]} ({unit})")
            else:
                print("⚠️ Invalid menu choice. Please select 1 or 2.")
                
        except ValueError as e:
            print(f"❌ Input Error: {e}")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting.")
            break

if __name__ == "__main__":
    main()
