inventory = []

def add_product():
    product_name = input("Enter the product name: ")
    product_id = input("Enter the product ID: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    
    for product in inventory:
        if product['product_id'] == product_id:
            print("Product ID already exists. Please use a different ID.")
            return
    
    inventory.append({
        'product_name': product_name,
        'product_id': product_id,
        'quantity': quantity,
        'price': price
    })
    print(f"New Product '{product_name}' added")

def view_inventory():
    if not inventory:
        print("No products available in the inventory.")
        return
    
    print("Current Inventory:")
    for product in inventory:
        print(f"Name: {product['product_name']}, ID: {product['product_id']}, Quantity: {product['quantity']}, Price: {product['price']}")

def update_product_quantity():
    if not inventory:
        print("No products available in the inventory.")
        return
    
    product_id = input("Enter the product ID to update: ")
    new_quantity = int(input("Enter the new quantity: "))
    
    for product in inventory:
        if product['product_id'] == product_id:
            product['quantity'] = new_quantity
            print(f"Quantity of product ID '{product_id}' updated to {new_quantity}.")
            return
    
    print(f"Product ID '{product_id}' not found.")

def remove_product():
    global inventory  # Fixing the scope issue
    if not inventory:
        print("No products available in the inventory.")
        return
    
    product_id = input("Enter the product ID to remove: ")
    
    initial_length = len(inventory)
    inventory = [product for product in inventory if product['product_id'] != product_id]
    
    if len(inventory) < initial_length:
        print(f"Product ID '{product_id}' removed.")
    else:
        print(f"Product ID '{product_id}' not found.")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add a New Product")
        print("2. View Inventory")
        print("3. Update Product Quantity")
        print("4. Remove a Product")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_product_quantity()
        elif choice == '4':
            remove_product()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()