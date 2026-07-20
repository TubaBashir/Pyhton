import math

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def perimeter_square(side):
    return 4 * side

def circumference_circle(radius):
    return 2 * math.pi * radius

def perimeter_triangle(side1, side2, side3):
    return side1 + side2 + side3

def main():
    print("📐 Geometric Perimeter Calculator")
    print("1. Rectangle\n2. Square\n3. Circle (Circumference)\n4. Triangle")
    
    choice = input("Choose a shape (1-4): ").strip()
    
    try:
        if choice == '1':
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            print(f"✅ Perimeter: {perimeter_rectangle(l, w):.2f}")
            
        elif choice == '2':
            s = float(input("Enter side length: "))
            print(f"✅ Perimeter: {perimeter_square(s):.2f}")
            
        elif choice == '3':
            r = float(input("Enter radius: "))
            print(f"✅ Circumference: {circumference_circle(r):.2f}")
            
        elif choice == '4':
            s1 = float(input("Enter side 1: "))
            s2 = float(input("Enter side 2: "))
            s3 = float(input("Enter side 3: "))
            print(f"✅ Perimeter: {perimeter_triangle(s1, s2, s3):.2f}")
            
        else:
            print("❌ Invalid selection!")
            
    except ValueError:
        print("❌ Please enter numeric values only.")

if __name__ == "__main__":
    main()
