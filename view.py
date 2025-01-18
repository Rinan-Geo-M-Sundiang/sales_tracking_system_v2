# view.py

def view_products(products):
    if not products:
        print("No products available.")
    else:
        print("\nCurrent Inventory:")
        for product_id, details in products.items():
            print(f"- {details['name']} (ID: {product_id}): {details['quantity']} in stock")
