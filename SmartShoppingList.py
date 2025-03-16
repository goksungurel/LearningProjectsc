import json

class ShoppingList:
    def __init__(self):
        """Initialize an empty shopping list."""
        self.products = {}

    def add_product(self):
        """Add a new product to the shopping list."""
        product = input("Enter product name: ").strip()
        try:
            price = float(input("Enter price (₺): "))
            self.products[product] = price
            print(f"✅ {product} added to the list!")
        except ValueError:
            print("⚠️ Invalid price! Please enter a number.")

    def remove_product(self):
        """Remove a product from the shopping list."""
        product = input("Enter product name to remove: ").strip()
        if product in self.products:
            del self.products[product]
            print(f"🗑️ {product} removed!")
        else:
            print(f"⚠️ {product} not found in the list!")

    def show_list(self):
        """Display the current shopping list."""
        if not self.products:
            print("🛒 Your shopping list is empty!")
            return
        
        total = sum(self.products.values())
        print("\n📜 **Shopping List:**")
        for product, price in self.products.items():
            print(f" - {product}: {price}₺")
        print(f"\n💰 **Total Cost:** {total}₺")

    def check_budget(self):
        """Compare total cost with user-defined budget."""
        try:
            budget = float(input("Enter your budget (₺): "))
            total = sum(self.products.values())
            
            if total > budget:
                print(f"🚨 Warning! Budget exceeded! ({total}/{budget}₺)")
            else:
                print(f"✅ You're within your budget. ({total}/{budget}₺)")
        except ValueError:
            print("⚠️ Invalid budget! Please enter a number.")

    def save_list(self, filename="shopping_list.json"):
        """Save the shopping list to a JSON file."""
        with open(filename, "w") as file:
            json.dump(self.products, file)
        print(f"📝 List saved as {filename}")

    def load_list(self, filename="shopping_list.json"):
        """Load the shopping list from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.products = json.load(file)
                print("🔄 Shopping list loaded!")
        except FileNotFoundError:
            print("⚠️ No saved list found!")

    def clear_list(self):
        """Remove all items from the shopping list."""
        self.products.clear()
        print("🧹 Shopping list cleared!")

    def run(self):
        while True:
            print("\n📌 **Smart Shopping List**")
            print("1️⃣ Add Product")
            print("2️⃣ Show List")
            print("3️⃣ Remove Product")
            print("4️⃣ Clear List")
            print("5️⃣ Check Budget")
            print("6️⃣ Save List")
            print("7️⃣ Load List")
            print("0️⃣ Exit")

            choice = input("Your choice: ").strip()
            
            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.show_list()
            elif choice == "3":
                self.remove_product()
            elif choice == "4":
                self.clear_list()
            elif choice == "5":
                self.check_budget()
            elif choice == "6":
                self.save_list()
            elif choice == "7":
                self.load_list()
            elif choice == "0":
                print("👋 Exiting... Goodbye!")
                break
            else:
                print("⚠️ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.run()
