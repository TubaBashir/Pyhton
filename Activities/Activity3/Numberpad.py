import tkinter as tk

class NumberPad:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Pad")
        self.root.resizable(False, False)

        # String variable to track the display text
        self.display_var = tk.StringVar(value="")

        # 1. Digital Display Screen
        display_frame = tk.Frame(root, bg="#eaeaea", bd=2, relief="sunken")
        display_frame.pack(padx=10, pady=10, fill="x")
        
        display_label = tk.Label(
            display_frame, 
            textvariable=self.display_var, 
            font=("Arial", 20, "bold"), 
            anchor="e", 
            bg="white", 
            fg="black", 
            height=2, 
            padx=10
        )
        display_label.pack(fill="x")

        # 2. Keypad Buttons Layout
        # Standard numpad ordering (7-8-9 on top)
        buttons = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['C', '0', 'Enter']
        ]

        # Container for the grid layout
        grid_frame = tk.Frame(root)
        grid_frame.pack(padx=10, pady=5)

        # Build the grid using nested loops
        for row_idx, row in enumerate(buttons):
            for col_idx, text in enumerate(row):
                # Dynamically set colors for action buttons vs numbers
                if text in ['C', 'Enter']:
                    bg_color = "#ff9f0a" if text == 'Enter' else "#d4d4d2"
                    fg_color = "white" if text == 'Enter' else "black"
                else:
                    bg_color = "#505050"
                    fg_color = "white"

                # Create the button object
                btn = tk.Button(
                    grid_frame, 
                    text=text, 
                    font=("Arial", 16, "bold"),
                    bg=bg_color, 
                    fg=fg_color, 
                    width=5, 
                    height=2,
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row_idx, column=col_idx, padx=4, pady=4)

    def on_button_click(self, char):
        """Handles button logic updates based on key presses."""
        current_text = self.display_var.get()

        if char == 'C':
            # Clear the display screen
            self.display_var.set("")
        elif char == 'Enter':
            # Print output to terminal and reset
            print(f"Submitted Value: {current_text}")
            self.display_var.set("")
        else:
            # Append clicked numbers to the display string
            self.display_var.set(current_text + char)

# Initialize and run the application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberPad(root)
    root.mainloop()
