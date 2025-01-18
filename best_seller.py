# best_seller.py

from sales import sales

def analyze_sales(products):
    # Create a dictionary to store total sales per product
    sales_per_product = {}
    for sale in sales:
        if sale["product_id"] in sales_per_product:
            sales_per_product[sale["product_id"]] += sale["quantity"]
        else:
            sales_per_product[sale["product_id"]] = sale["quantity"]

    if sales_per_product:
        best_selling_product_id = max(sales_per_product, key=sales_per_product.get)
        best_selling_product = products[best_selling_product_id]
        print(f"Best-Selling Product: {best_selling_product['name']} (ID: {best_selling_product_id}) - {sales_per_product[best_selling_product_id]} sold")
    else:
        print("No sales recorded yet.")
