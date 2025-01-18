# revenue.py

from sales import sales

def calculate_revenue():
    total_revenue = sum(sale["total_sale"] for sale in sales)
    print(f"Total Revenue: ${total_revenue:.2f}")
