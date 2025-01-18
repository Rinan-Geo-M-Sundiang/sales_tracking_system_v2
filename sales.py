# sales.py

sales = []

def record_sale(products):
    try:
        # Input sale details
        product_id = input("Enter product ID: ").strip()
        if product_id not in products:
            raise ValueError(f"Product ID {product_id} not found in inventory.")

        try:
            quantity_sold = int(input("Enter quantity sold: ").strip())
            if quantity_sold < 0:
                raise ValueError("Sold quantity must be a non-negative integer.")
        except ValueError:
            raise ValueError("Invalid quantity. Please enter a valid integer.")

        # Check if there's enough stock
        product = products[product_id]
        if product["quantity"] < quantity_sold:
            raise ValueError(f"Insufficient stock! Only {product['quantity']} items available.")

        # Update the product quantity and record sale
        product["quantity"] -= quantity_sold
        sales.append({"product_id": product_id, "quantity": quantity_sold, "total_sale": product["price"] * quantity_sold})

        print(f"Sale recorded: {quantity_sold} of {product['name']} sold.")

    except ValueError as e:
        print(f"Error: {e}")
