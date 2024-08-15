def add_product(inventory):
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the product quantity: "))

    for product in inventory:
        if product['name'].lower() == name.lower():
            print(f"Product '{name}' already exists in the inventory.")
            return

    new_product = {'name': name, 'price': price, 'quantity': quantity}
    inventory.append(new_product)
    print(f"Product '{name}' added to the inventory.")

def update_product_quantity(inventory):
    name = input("Enter the product name to update: ")

    for product in inventory:
        if product['name'].lower() == name.lower():
            new_quantity = int(input(f"Enter the new quantity for '{name}': "))
            product['quantity'] = new_quantity
            print(f"Quantity for '{name}' updated to {new_quantity}.")
            return

    print(f"Product '{name}' not found in the inventory.")

def view_inventory(inventory):
    if not inventory:
        print("The inventory is empty.")
        return

    print("\nCurrent Inventory:")
    for product in inventory:
        print(f"Name: {product['name']}, Price: ${product['price']:.2f}, Quantity: {product['quantity']}")
    print()

def main():
    inventory = []

    while True:
        print("\nInventory Management System")
        print("1. Add a new product")
        print("2. Update product quantity")
        print("3. View inventory")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            update_product_quantity(inventory)
        elif choice == '3':
            view_inventory(inventory)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()