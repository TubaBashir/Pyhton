import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        # Get values from entry boxes
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
        
        birth_date = date(year, month, day)
        today = date.today()
        
        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future!")
            return
            
        # Calculation logic
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Display the result
        label_result.config(text=f"You are {age} years old!", fg="#1b4332")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numbers only.")

# Initialize the main app window
app = tk.Tk()
app.title("Age Calculator")
app.geometry("350x250")
app.config(padx=20, pady=20)

# Create layout elements (Labels and Entry Fields)
tk.Label(app, text="Year (YYYY):").grid(row=0, column=0, pady=5, sticky="w")
entry_year = tk.Entry(app)
entry_year.grid(row=0, column=1, pady=5)

tk.Label(app, text="Month (MM):").grid(row=1, column=0, pady=5, sticky="w")
entry_month = tk.Entry(app)
entry_month.grid(row=1, column=1, pady=5)

tk.Label(app, text="Day (DD):").grid(row=2, column=0, pady=5, sticky="w")
entry_day = tk.Entry(app)
entry_day.grid(row=2, column=1, pady=5)

# Calculate Button
btn_calculate = tk.Button(app, text="Calculate Age", command=calculate_age, bg="#2d6a4f", fg="white", width=15)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=15)

# Result Label
label_result = tk.Label(app, text="", font=("Arial", 12, "bold"))
label_result.grid(row=4, column=0, columnspan=2, pady=5)

# Start the application loop
app.mainloop()
