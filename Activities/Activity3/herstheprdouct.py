class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int, category: str = "General"):
        """
        Initializes a new Product instance.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def display_details(self) -> str:
        """
        Returns a beautifully formatted string of the product details.
        """
        status = "In Stock" if self.stock > 0 else "Out of Stock"
        return (
            f"--- Product Catalog Details ---\n"
            f"ID: {self.product_id}\n"
            f"Name: {self.name}\n"
            f"Category: {self.category}\n"
            f"Price: ${self.price:.2f}\n"
            f"Stock: {self.stock} units ({status})\n"
            f"-------------------------------"
        )

    def update_stock(self, quantity: int):
        """
        Updates the stock quantity. Positive numbers add stock, negative numbers reduce it.
        """
        if self.stock + quantity < 0:
            print(f"Error: Cannot reduce stock below 0. Current stock for '{self.name}': {self.stock}")
        else:
            self.stock += quantity
            print(f"Stock updated successfully. New '{self.name}' stock: {self.stock}")

    def apply_discount(self, percentage: float):
        """
        Applies a percentage discount to the product price.
        """
        if 0 < percentage < 100:
            discount_amount = self.price * (percentage / 100)
            self.price -= discount_amount
            print(f"Applied {percentage}% discount. New price for '{self.name}': ${self.price:.2f}")
        else:
            print("Invalid discount percentage. Must be between 0 and 100.")


# ==========================================
# Example Usage / Implementation
# ==========================================
if __name__ == "__main__":
    # 1. Create a new product instance
    my_product = Product(
        product_id="PROD-9021", 
        name="Wireless Noise-Canceling Headphones", 
        price=199.99, 
        stock=45, 
        category="Electronics"
    )

    # 2. Display the product
    print(my_product.display_details())

    # 3. Simulate a customer purchase (reduces stock by 2)
    print("\n[Simulating Purchase]")
    my_product.update_stock(-2)

    # 4. Apply a holiday sale discount
    print("\n[Applying Holiday Sale]")
    my_product.apply_discount(15)

    # 5. Display the final updated product details
    print("\n" + my_product.display_details())
