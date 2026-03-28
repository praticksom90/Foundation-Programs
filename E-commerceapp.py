
products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Smartphone", "price": 25000},
    {"id": 3, "name": "Headphones", "price": 3000},
    {"id": 4, "name": "Keyboard", "price": 1500},
    {"id": 5, "name": "Mouse", "price": 800}
]

cart = []  


def show_products():
    print("\n🛍 Available Products")
    for p in products:
        print(f"{p['id']}. {p['name']} - ₹{p['price']}")

def add_to_cart():
    product_id = int(input("Enter product ID to add: "))

    for p in products:
        if p["id"] == product_id:
            cart.append(p)
            print(f"✅ {p['name']} added to cart\n")
            return

    print("❌ Product not found\n")

def remove_from_cart():
    if not cart:
        print("🛒 Cart is empty\n")
        return

    show_cart()
    index = int(input("Enter cart item number to remove: ")) - 1

    if 0 <= index < len(cart):
        removed = cart.pop(index)
        print(f"❌ {removed['name']} removed from cart\n")
    else:
        print("Invalid choice\n")

def show_cart():
    if not cart:
        print("🛒 Cart is empty\n")
        return

    print("\n🛒 Your Cart:")
    total = 0
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']} - ₹{item['price']}")
        total += item["price"]

    print(f"💰 Total: ₹{total}\n")

def checkout():
    if not cart:
        print("🛒 Cart is empty. Add items first.\n")
        return

    show_cart()
    confirm = input("Proceed to payment? (y/n): ").lower()

    if confirm == "y":
        print("\n💳 Processing payment...")
        print("✅ Payment successful!")
        print("📦 Order placed successfully!\n")
        cart.clear()
    else:
        print("❌ Checkout cancelled\n")


def main():
    while True:
        print("🛒 PYTHON E-COMMERCE STORE")
        print("1) View Products")
        print("2) Add to Cart")
        print("3) Remove from Cart")
        print("4) View Cart")
        print("5) Checkout")
        print("0) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            show_cart()
        elif choice == "5":
            checkout()
        elif choice == "0":
            print("👋 Thank you for shopping!")
            break
        else:
            print("❌ Invalid choice\n")

if __name__ == "__main__":
    main()
