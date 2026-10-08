import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================
# BACKEND CORE ARCHITECTURE
# ==========================================


class MenuItem:

    def __init__(self, item_id, name, price, category):
        self.id = item_id
        self.name = name
        self.price = price
        self.category = category


class Order:

    def __init__(self, order_id, table_number):
        self.order_id = order_id
        self.table_number = table_number
        self.items = {}  # Format: {MenuItem: quantity}
        self.status = "Active"  # Active or Settled
        self.tax_rate = 0.05  # 5% Service Tax

    def add_item(self, menu_item, quantity=1):
        if menu_item in self.items:
            self.items[menu_item] += quantity
        else:
            self.items[menu_item] = quantity

    def calculate_subtotal(self):
        return sum(item.price * qty for item, qty in self.items.items())

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        return subtotal + (subtotal * self.tax_rate)


class RestaurantBackend:

    def __init__(self):
        # Seed initial restaurant menu items
        self.menu = {
            1: MenuItem(1, "Classic Cheeseburger", 299.00, "Mains"),
            2: MenuItem(2, "Margherita Pizza", 399.00, "Mains"),
            3: MenuItem(3, "Caesar Salad", 199.00, "Starters"),
            4: MenuItem(4, "French Fries", 129.00, "Starters"),
            5: MenuItem(5, "Iced Americano", 149.00, "Beverages"),
            6: MenuItem(6, "Chocolate Brownie", 179.00, "Desserts"),
        }
        self.orders = {}
        self.reservations = {}  # Format: {table_no: guest_name}
        self.order_counter = 1001

        # Track tables 1 through 10
        for i in range(1, 11):
            self.reservations[i] = "Available"

    def create_order(self, table_number):
        order_id = self.order_counter
        self.orders[order_id] = Order(order_id, table_number)
        self.order_counter += 1
        return self.orders[order_id]


# ==========================================
# FRONTEND INTERFACE: TKINTER GUI
# ==========================================


class RestaurantApp:

    def __init__(self, root):
        self.backend = RestaurantBackend()
        self.root = root
        self.root.title("GourmetOS - Restaurant Management System")
        self.root.geometry("1024x650")

        # Track UI selections
        self.current_active_order = None

        # Create UI notebook tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.setup_order_billing_tab()
        self.setup_tables_reservations_tab()
        self.setup_menu_management_tab()

    # ------------------------------------------
    # TAB 1: ORDERING & BILLING SYSTEM
    # ------------------------------------------
    def setup_order_billing_tab(self):
        order_frame = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(order_frame, text=" POS & Billing ")

        # Left Column: Menu Inventory Selector
        left_pane = ttk.LabelFrame(
            order_frame, text=" Digital Menu Catalog ", padding=10
        )
        left_pane.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Menu Tree view grid
        columns = ("id", "name", "price", "category")
        self.menu_tree = ttk.Treeview(
            left_pane, columns=columns, show="headings", selectmode="browse"
        )
        self.menu_tree.heading("id", text="Item ID")
        self.menu_tree.heading("name", text="Item Name")
        self.menu_tree.heading("price", text="Price (₹)")
        self.menu_tree.heading("category", text="Category")

        self.menu_tree.column("id", width=60, anchor="center")
        self.menu_tree.column("name", width=180, anchor="w")
        self.menu_tree.column("price", width=90, anchor="e")
        self.menu_tree.column("category", width=100, anchor="center")
        self.menu_tree.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Controls below menu
        ctrl_frame = ttk.Frame(left_pane)
        ctrl_frame.pack(fill=tk.X)

        ttk.Label(ctrl_frame, text="Table No:").grid(
            row=0, column=0, padx=5, sticky="w"
        )
        self.table_spin = ttk.Spinbox(
            ctrl_frame, from_=1, to=10, width=5, wrap=True
        )
        self.table_spin.grid(row=0, column=1, padx=5)

        ttk.Label(ctrl_frame, text="Qty:").grid(
            row=0, column=2, padx=15, sticky="w"
        )
        self.qty_spin = ttk.Spinbox(ctrl_frame, from_=1, to=20, width=5)
        self.qty_spin.set(1)
        self.qty_spin.grid(row=0, column=3, padx=5)

        add_btn = ttk.Button(
            ctrl_frame, text="Add to Ticket", command=self.add_item_to_order
        )
        add_btn.grid(row=0, column=4, padx=20)

        # Right Column: Current Active Receipt Breakdown
        right_pane = ttk.LabelFrame(
            order_frame, text=" Live Order Receipt ", padding=10
        )
        right_pane.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, width=420)

        self.receipt_txt = tk.Text(
            right_pane,
            font=("Consolas", 10),
            bg="#fdfdfd",
            state=tk.DISABLED,
            width=50,
        )
        self.receipt_txt.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # Billing Process Panel
        billing_panel = ttk.Frame(right_pane)
        billing_panel.pack(fill=tk.X)

        checkout_btn = ttk.Button(
            billing_panel,
            text="Generate Invoice & Close",
            command=self.finalize_bill,
        )
        checkout_btn.pack(fill=tk.X, side=tk.BOTTOM, pady=2)

        self.refresh_menu_display()

    # ------------------------------------------
    # TAB 2: TABLE BOOKING & RESERVATIONS
    # ------------------------------------------
    def setup_tables_reservations_tab(self):
        table_frame = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(table_frame, text=" Table Bookings ")

        # Left list overview
        list_pane = ttk.LabelFrame(
            table_frame, text=" Dining Room Floor Summary ", padding=10
        )
        list_pane.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        self.table_tree = ttk.Treeview(
            list_pane, columns=("table", "status"), show="headings"
        )
        self.table_tree.heading("table", text="Table Number")
        self.table_tree.heading("status", text="Current Occupant Status")
        self.table_tree.pack(fill=tk.BOTH, expand=True)

        # Right configuration form
        form_pane = ttk.LabelFrame(
            table_frame, text=" Modify Booking Assignment ", padding=10
        )
        form_pane.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, width=350)

        ttk.Label(form_pane, text="Select Table ID:").pack(
            anchor="w", pady=(10, 2)
        )
        self.booking_table_spin = ttk.Spinbox(form_pane, from_=1, to=10, width=10)
        self.booking_table_spin.pack(anchor="w", pady=(0, 15))

        ttk.Label(form_pane, text="Guest Name / Status Tag:").pack(
            anchor="w", pady=(5, 2)
        )
        self.guest_name_entry = ttk.Entry(form_pane, font=("Helvetica", 10))
        self.guest_name_entry.pack(fill=tk.X, pady=(0, 20))

        assign_btn = ttk.Button(
            form_pane, text="Confirm Assignment", command=self.update_reservation
        )
        assign_btn.pack(fill=tk.X, pady=5)

        clear_btn = ttk.Button(
            form_pane,
            text="Mark Table Available",
            command=self.clear_reservation,
        )
        clear_btn.pack(fill=tk.X, pady=5)

        self.refresh_table_display()

    # ------------------------------------------
    # TAB 3: RESTAURANT INVENTORY MANAGEMENT
    # ------------------------------------------
    def setup_menu_management_tab(self):
        config_frame = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(config_frame, text=" Manage Menu Config ")

        form_pane = ttk.LabelFrame(
            config_frame, text=" Create New Culinary Item ", padding=15
        )
        form_pane.pack(fill=tk.X, pady=(0, 15))

        # Interactive form layout grid
        ttk.Label(form_pane, text="Item Name:").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        self.new_name_entry = ttk.Entry(form_pane, width=30)
        self.new_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_pane, text="Price (₹):").grid(
            row=0, column=2, sticky="w", padx=25, pady=5
        )
        self.new_price_entry = ttk.Entry(form_pane, width=15)
        self.new_price_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(form_pane, text="Category:").grid(
            row=1, column=0, sticky="w", padx=5, pady=5
        )
        self.new_cat_combo = ttk.Combobox(
            form_pane,
            values=["Starters", "Mains", "Desserts", "Beverages"],
            width=27,
            state="readonly",
        )
        self.new_cat_combo.grid(row=1, column=1, padx=5, pady=5)
        self.new_cat_combo.current(1)

        submit_btn = ttk.Button(
            form_pane, text="Save Item to Catalog", command=self.add_new_menu_item
        )
        submit_btn.grid(row=1, column=3, columnspan=2, padx=5, pady=5, sticky="e")

    # ==========================================
    # LOGIC CONTROLLER FUNCTIONS
    # ==========================================

    def refresh_menu_display(self):
        """Clears and re-populates the POS catalog lists."""
        for item in self.menu_tree.get_children():
            self.menu_tree.delete(item)

        for item_id, item in self.backend.menu.items():
            self.menu_tree.insert(
                "",
                tk.END,
                values=(item.id, item.name, f"{item.price:.2f}", item.category),
            )

    def refresh_table_display(self):
