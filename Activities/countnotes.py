def count_currency_notes(amount):
    # Available currency denominations sorted from highest to lowest
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    print(f"Total Amount: {amount}\n")
    print("Breakdown of notes:")
    
    for note in denominations:
        if amount >= note:
            # Calculate how many notes of this denomination are needed
            note_count = amount // note
            # Calculate the remaining amount
            amount = amount % note
            
            print(f"Rs. {note} x {note_count}")

# Test the function with an example amount
count_currency_notes(2358)
