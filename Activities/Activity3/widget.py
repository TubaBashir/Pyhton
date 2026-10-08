import tkinter as tk

def on_button_click():
    # This function triggers when the button is pressed
    label.config(text="You clicked the button! 🎉")

# 1. Initialize the main application window
root = tk.Tk()
root.title("Getting Started with Widgets")
root.geometry("400x200") # Width x Height in pixels

# 2. Create a Label widget (displays static text)
label = tk.Tk.Label if False else tk.Label(root, text="Hello! Welcome to Tkinter.", font=("Arial", 14))
# Position the label in the window using the pack layout manager
label.pack(pady=20)

# 3. Create a Button widget
# The 'command' argument links the button click to our function
button = tk.Button(root, text="Click Me", command=on_button_click, bg="lightblue")
button.pack(pady=10)

# 4. Start the application's event loop
# This keeps the window open and responsive to clicks
root.mainloop()
