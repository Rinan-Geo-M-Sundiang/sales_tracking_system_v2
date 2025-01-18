# main.py

from products import add_product
from sales import record_sale
from revenue import calculate_revenue
from best_seller import analyze_sales
from view import view_products

# Global product inventory
products = {}

def main():
    while True:
        try:
            action = input("\nWhat would you like to do? (add/record/view/revenue/analyze/exit): ").strip().lower()

            if action == "add":
                add_product(products)
            elif action == "record":
                record_sale(products)
            elif action == "view":
                view_products(products)
            elif action == "revenue":
                calculate_revenue()
            elif action == "analyze":
                analyze_sales(products)
            elif action == "exit":
                print("Thank you for using the Real-Time Sales Tracking System!")
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")


main()
