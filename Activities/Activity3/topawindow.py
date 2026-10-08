import tkinter as tk
from tkinter import messagebox
import time
import threading

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Window Controller")
        self.root.geometry("400x300")
        
        # Intercept the standard window 'X' close button
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Label
        self.label = tk.Label(root, text="Click a button to stop/close the window", font=("Arial", 12))
        self.label.pack(pady=20)
        
        # Button 1: Immediate Close
        self.btn_close = tk.Button(root, text="1. Immediate Close (destroy)", command=self.close_immediately, bg="lightcoral")
        self.btn_close.pack(pady=10)
        
        # Button 2: Delayed Close
        self.btn_delay = tk.Button(root, text="2. Close After 3 Seconds", command=self.close_with_delay, bg="lightblue")
        self.btn_delay.pack(pady=10)
        
        # Button 3: Safe Exit with Prompt
        self.btn_safe = tk.Button(root, text="3. Safe Exit (With Prompt)", command=self.on_closing, bg="lightgreen")
        self.btn_safe.pack(pady=10)

    def close_immediately(self):
        print("Closing the window immediately...")
        # destroy() terminates the mainloop and frees resources
        self.root.destroy() 

    def close_with_delay(self):
        self.label.config(text="Closing in 3 seconds...")
        # Start a background thread so the GUI doesn't freeze during the wait
        threading.Thread(target=self._delay_worker, daemon=True).start()

    def _delay_worker(self):
        time.sleep(3)
        # Always interact with Tkinter widgets/methods from the main thread
        self.root.after(0, self.root.destroy)

    def on_closing(self):
        # Ask for confirmation before stopping the window
        if messagebox.askokcancel("Quit", "Do you really want to stop the window?"):
            print("Window closed safely by the user.")
            self.root.destroy()

# Main execution loop
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop() # This keeps the window running until stopped
