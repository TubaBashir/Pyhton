import math
import re
import tkinter as tk
from tkinter import messagebox, ttk

# ---------------------------------------------------------
# BACKEND CORE LOGIC: PASSWORD EVALUATION
# ---------------------------------------------------------


def evaluate_password(password):
    """Evaluates password strength based on entropy, patterns, and character types."""
    score = 0
    feedback = []

    # 1. Check for basic empty input
    if not password:
        return 0, "Empty", ["Please enter a password."], "#d3d3d3", 0.0

    # 2. Common Dictionary & Keyboard Patterns Blocklist
    blocklist = [
        "password",
        "qwerty",
        "123456",
        "123456789",
        "welcome",
        "letmein",
        "admin",
    ]
    if password.lower() in blocklist or any(
        x in password.lower() for x in blocklist[:3]
    ):
        return (
            1,
            "Very Weak (Common Pattern)",
            [
                "❌ Avoid common passwords, keyboard paths, or repetitive sequences."
            ],
            "#ff4d4d",
            10.0,
        )

    # 3. Calculate Character Pool Size & Entropy
    pool_size = 0
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += 32

    # Calculate Shannon Entropy: E = L * log2(R)
    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0

    # 4. Detailed Component Checklist
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Make it longer (aim for 12+ characters).")

    if has_upper and has_lower:
        score += 1
    else:
        feedback.append("⚠️ Mix uppercase (A-Z) and lowercase (a-z) letters.")

    if has_digit:
        score += 1
    else:
        feedback.append("⚠️ Add at least one number (0-9).")

    if has_special:
        score += 1
    else:
        feedback.append(
            "⚠️ Include at least one special symbol (!@#$%^&*)."
        )

    # 5. Cap the score baseline based on entropy thresholds
    # < 28 bits = very weak; 28-35 = weak; 36-59 = medium; 60-127 = strong; 128+ = very strong
    if entropy >= 60:
        score += 1

    # 6. Final Strength Mapping
    if score <= 2 or entropy < 36:
        return 1, "Weak", feedback, "#ff4d4d", entropy
    elif score <= 4 or entropy < 60:
        return 2, "Moderate", feedback, "#ffa64d", entropy
    elif score == 5:
        return 3, "Strong", ["✅ Good complexity and length."], "#33cc33", entropy
    else:
        return (
            4,
            "Very Strong",
            ["🏆 Excellent, secure password!"],
            "#009900",
            entropy,
        )


# ---------------------------------------------------------
# FRONTEND INTERFACE: TKINTER APPLICATION
# ---------------------------------------------------------


class PasswordCheckerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Strength Advisor")
        self.root.geometry("520x450")
        self.root.resizable(False, False)

        # Style configurations
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Main window layout container
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Application Title
        title_label = ttk.Label(
            main_frame,
            text="Password Strength Evaluator",
            font=("Helvetica", 16, "bold"),
        )
        title_label.pack(pady=(0, 15))

        # Password Entry Section
        entry_label = ttk.Label(
            main_frame, text="Enter Password:", font=("Helvetica", 11)
        )
        entry_label.pack(anchor="w", pady=(5, 2))

        self.password_var = tk.StringVar()
        self.password_var.trace_add("write", self.on_password_change)

        self.entry_box = ttk.Entry(
            main_frame,
            textvariable=self.password_var,
            font=("Consolas", 12),
            show="*",
        )
        self.entry_box.pack(fill=tk.X, pady=(0, 5))

        # Visibility Toggle Checkbox
        self.reveal_var = tk.BooleanVar(value=False)
        self.reveal_btn = ttk.Checkbutton(
            main_frame,
            text="Show Password",
            variable=self.reveal_var,
            command=self.toggle_visibility,
        )
        self.reveal_btn.pack(anchor="w", pady=(0, 15))

        # Visual Strength Meter (Progress Bar Component)
        self.progress_bar = ttk.Progressbar(
            main_frame, orient="horizontal", length=100, mode="determinate"
        )
        self.progress_bar.pack(fill=tk.X, pady=(5, 5))

        # Text Summary Metrics
        self.status_label = ttk.Label(
            main_frame,
            text="Strength: Empty",
            font=("Helvetica", 12, "bold"),
            foreground="#777777",
        )
        self.status_label.pack(anchor="w", pady=(5, 2))

        self.entropy_label = ttk.Label(
            main_frame,
            text="Entropy: 0.00 bits",
            font=("Helvetica", 10, "italic"),
        )
        self.entropy_label.pack(anchor="w", pady=(0, 15))

        # Actionable Suggestions Display Box
        suggest_label = ttk.Label(
            main_frame, text="System Recommendations:", font=("Helvetica", 11, "bold")
        )
        suggest_label.pack(anchor="w")

        self.feedback_box = tk.Text(
            main_frame,
            height=6,
            bg="#f9f9f9",
            wrap=tk.WORD,
            font=("Helvetica", 10),
            state=tk.DISABLED,
        )
        self.feedback_box.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

    def toggle_visibility(self):
        """Shows or masks the input characters."""
        if self.reveal_var.get():
            self.entry_box.config(show="")
        else:
            self.entry_box.config(show="*")

    def on_password_change(self, *args):
        """Monitors typing in real-time to adjust metrics instantly."""
        password = self.password_var.get()
        tier, dynamic_text, messages, hex_color, raw_entropy = evaluate_password(
            password
        )

        # 1. Update visual metrics bar
        # Map tiers 1-4 to percentages 25%-100%
        progress_val = 0 if dynamic_text == "Empty" else (tier * 25)
        self.progress_bar["value"] = progress_val

        # 2. Update descriptive labels
        self.status_label.config(
            text=f"Strength: {dynamic_text}", foreground=hex_color
        )
        self.entropy_label.config(text=f"Entropy: {raw_entropy:.2f} bits")

        # 3. Update instructions panel dynamically
        self.feedback_box.config(state=tk.NORMAL)
        self.feedback_box.delete("1.0", tk.END)
        for remark in messages:
            self.feedback_box.insert(tk.END, f"{remark}\n")
        self.feedback_box.config(state=tk.DISABLED)


# Execution Point
if __name__ == "__main__":
    app_window = tk.Tk()
    app = PasswordCheckerApp(app_window)
    app_window.mainloop()
