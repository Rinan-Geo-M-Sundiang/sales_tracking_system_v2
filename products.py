# products.py

def add_product(products):
    try:
        # Input product details
        product_id = input("Enter product ID: ").strip()
        if product_id in products:
            raise ValueError(f"Product ID {product_id} already exists.")

        product_name = input("Enter product name: ").strip()
        if not product_name:
            raise ValueError("Product name cannot be empty.")

        try:
            product_price = float(input("Enter product price: ").strip())
            if product_price < 0:
                raise ValueError("Price must be a non-negative number.")
        except ValueError:
            raise ValueError("Invalid price. Please enter a valid number.")

        try:
            product_quantity = int(input("Enter product quantity: ").strip())
            if product_quantity < 0:
                raise ValueError("Quantity must be a non-negative integer.")
        except ValueError:
            raise ValueError("Invalid quantity. Please enter a valid integer.")

        # Add the product to the dictionary
        products[product_id] = {
            'name': product_name,
            'price': product_price,
            'quantity': product_quantity
        }
        print("Product added successfully!")

    except ValueError as e:
        print(f"Error: {e}")
