items = {
    "Electronics": {
        "laptop": 999.99,
        "smartphone": 699.99
    },
    "Clothing": {
        "t-shirt": 19.99,
        "jeans": 49.99
    },
    "Groceries": {
        "milk": 2.99,
        "bread": 1.99
    }
}

bought = {item: 0 for category in items.values() for item in category}

def showitems():
    print("------------Items for Sale------------\n")
    item_number = 1
    item_mapping = {}
    for category, items_in_category in items.items():
        print(f"Category: {category}\n")
        for item, price in items_in_category.items():
            print(f"{item_number}. {item} - ${price}")
            item_mapping[item_number] = item
            item_number += 1
        print("\n")
    return item_mapping

def buyitems():
    print("------------Buy Items------------\n")
    while True:
        item_mapping = showitems()
        try:
            while True:
                item_number = int(input("Enter the number of the item you want to buy (or 0 to stop): "))
                if item_number == 0:
                    return
                if item_number not in item_mapping:
                    print("Invalid item number. Please try again.")
                    continue
                item = item_mapping[item_number]
                quantity = input("Enter the quantity you want to buy: ")
                if not quantity.isdigit():
                    print("Invalid quantity. Please try again.")
                    continue
                bought[item] += int(quantity)
                print(f"{quantity} {item} bought successfully.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def showcart():
    print("------------Your Cart------------\n")
    for item, quantity in bought.items():
        if quantity > 0:
            print(f"{item} - {quantity}")

def checkout():
    print("------------Checkout------------\n")
    total = 0
    for item, quantity in bought.items():
        total += items[[category for category in items if item in items[category]][0]][item] * quantity
    print(f"Total: ${total}")
    while True:
        confirm = input("Confirm purchase? Yes or No\n").lower()
        if confirm == "yes":
            print("Purchase confirmed. Thank you for shopping with us.")
            receipt()
            break
        elif confirm == "no":
            print("Purchase cancelled.")
            break
        else:
            print("Invalid input. Please try again.")

def receipt():
    print("------------Receipt------------\n")
    total = 0
    for item, quantity in bought.items():
        if quantity > 0:
            print(f"{item} - {quantity}")
            total += items[[category for category in items if item in items[category]][0]][item] * quantity
    print(f"Total: ${total}")

def main():
    while True:
        print("------------Main Menu------------\n")
        print("1. Buy Items")
        print("2. Show Cart")
        print("3. Checkout")
        print("4. Show Receipt")
        print("5. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            buyitems()
        elif choice == "2":
            showcart()
        elif choice == "3":
            checkout()
        elif choice == "4":
            receipt()
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()



    #this is the first sample