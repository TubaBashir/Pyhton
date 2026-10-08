import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("PyEdit - Advanced Text Editor")
        self.root.geometry("900x600")

        # Track the current theme (Light or Dark)
        self.dark_mode = False

        # Apply a clean theme style
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.setup_ui()
        self.setup_menu()
        self.setup_shortcuts()
        self.add_new_tab()

    def setup_ui(self):
        """Creates the layout including tabs, sidebar line numbers, and status bar."""
        # Top toolbar container
        self.toolbar = ttk.Frame(self.root, padding=2)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        theme_btn = ttk.Button(self.toolbar, text="🌓 Toggle Theme", command=self.toggle_theme)
        theme_btn.pack(side=tk.LEFT, padx=5)

        # Status Bar at the bottom
        self.status_bar = ttk.Label(self.root, text=" Lines: 1 | Words: 0 ", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Tab Manager (Notebook)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def setup_menu(self):
        """Creates the window dropdown menus."""
        menubar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Tab", accelerator="Ctrl+N", command=self.add_new_tab)
        file_menu.add_command(label="Open File...", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Close Tab", accelerator="Ctrl+W", command=self.close_current_tab)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=lambda: self.get_current_text_widget().edit_undo())
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=lambda: self.get_current_text_widget().edit_redo())
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menubar)

    def setup_shortcuts(self):
        """Binds hotkeys to editor functions."""
        self.root.bind("<Control-n>", lambda e: self.add_new_tab())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-S>", lambda e: self.save_as_file())
        self.root.bind("<Control-w>", lambda e: self.close_current_tab())

    # --- Tab & Text Management ---

    def add_new_tab(self, file_path=None, content=""):
        """Creates a new text area inside a new tab frame."""
        tab_frame = ttk.Frame(self.notebook)
        
        # Scrollbars
        y_scroll = ttk.Scrollbar(tab_frame)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Text Box widget
        text_widget = tk.Text(
            tab_frame, undo=True, maxundo=-1, wrap="word",
            yscrollcommand=y_scroll.set, font=("Consolas", 12),
            padx=10, pady=10
        )
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        y_scroll.config(command=text_widget.yview)

        # Apply current theme settings to new tab
        if self.dark_mode:
            text_widget.config(bg="#1e1e1e", fg="#ffffff", insertbackground="white")
        else:
            text_widget.config(bg="#ffffff", fg="#000000", insertbackground="black")

        # Insert content if opening an existing file
        if content:
            text_widget.insert("1.0", content)

        # Track metadata inside the frame object dynamically
        tab_frame.file_path = file_path
        tab_frame.text_widget = text_widget

        tab_title = os.path.basename(file_path) if file_path else "Untitled"
        self.notebook.add(tab_frame, text=tab_title)
        self.notebook.select(tab_frame)

        # Track keyboard releases to update line/word counts
        text_widget.bind("<KeyRelease>", self.update_status_bar)

    def get_current_tab(self):
        """Returns the active frame widget container."""
        if not self.notebook.tabs():
            return None
        return self.notebook.nametowidget(self.notebook.select())

    def get_current_text_widget(self):
        """Returns the active text typing area."""
        tab = self.get_current_tab()
        return tab.text_widget if tab else None

    # --- File Operations ---

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.add_new_tab(file_path=file_path, content=content)
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file: {e}")

    def save_file(self):
        current_tab = self.get_current_tab()
        if not current_tab:
            return

        if current_tab.file_path:
            self.write_to_file(current_tab.file_path, current_tab)
        else:
            self.save_as_file()

    def save_as_file(self):
        current_tab = self.get_current_tab()
        if not current_tab:
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if file_path:
            self.write_to_file(file_path, current_tab)

    def write_to_file(self, file_path, tab):
        try:
            content = tab.text_widget.get("1.0", tk.END)[:-1] # Remove trailing extra newline added by tkinter
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            tab.file_path = file_path
            self.notebook.tab(tab, text=os.path.basename(file_path))
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

    def close_current_tab(self):
        current_tab = self.get_current_tab()
        if current_tab:
            self.notebook.forget(current_tab)
        if not self.notebook.tabs():
            self.add_new_tab() # Always keep at least one tab open

    # --- UI Polish ---

    def update_status_bar(self, event=None):
        text_widget = self.get_current_text_widget()
        if not text_widget:
            return
        
        # Calculate line position
        row, _ = text_widget.index(tk.INSERT).split('.')
        
        # Calculate word counts
        content = text_widget.get("1.0", tk.END).strip()
        words = len(content.split()) if content else 0
        
        self.status_bar.config(text=f" Lines: {row} | Words: {words} ")

    def on_tab_change(self, event):
        self.update_status_bar()

    def toggle_theme(self):
        """Switches dynamically between light mode and dark mode."""
        self.dark_mode = not self.dark_mode
        
        for tab_id in self.notebook.tabs():
            tab = self.notebook.nametowidget(tab_id)
            text_widget = tab.text_widget
            if self.dark_mode:
                text_widget.config(bg="#1e1e1e", fg="#ffffff", insertbackground="white")
            else:
                text_widget.config(bg="#ffffff", fg="#000000", insertbackground="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
