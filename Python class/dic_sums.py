# question 
# 
# inventory = {
    # "pen":{"qty":100,"price":20},
    # "pencil":{"qty":50,"price":5},
    # "notebook":{"qty":200,"price":150},
    # "A4paper":{"qty":1000,"price":2},}


# function 
# buy("pencil",5)
# sell("pencil",2)
# revenue() -- what are sales done in all product the total price 


# 1. Start with the inventory dictionary
inventory = {
    "pen": {"qty": 100, "price": 20},
    "pencil": {"qty": 50, "price": 5},
    "notebook": {"qty": 200, "price": 150},
    "A4paper": {"qty": 1000, "price": 2},
}

# 2. Create a dictionary to track total sales (revenue) per product
sales = {product: 0 for product in inventory}

# create a dic for purchases 
purchases = {product: 0 for product in inventory}


# 3. Define the buy function (add stock)
# def buy(product, qty):
#     # Increase the quantity of the product in inventory
#     inventory[product]["qty"] += qty


def buy(product, qty):
    inventory[product]["qty"] += qty
    cost = qty * inventory[product]["price"]
    purchases[product] += cost
    print(f"Bought {qty} {product}(s) for {cost}")


# 4. Define the sell function (reduce stock and add to sales)
def sell(product, qty):
    # Check if enough stock is available
    if qty <= inventory[product]["qty"]:
        # Reduce stock
        inventory[product]["qty"] -= qty
        # Add revenue: quantity sold * unit price
        sales[product] += qty * inventory[product]["price"]
    else:
        print("Not enough stock to sell")

# 5. Define revenue function (total revenue from all products)
def revenue():
    # Sum of all values in sales dictionary
    return sum(sales.values())

# 6. Example usage
buy("pencil", 5)      # buys 5 pencils (stock becomes 55)
sell("pencil", 2)     # sells 2 pencils (stock becomes 53, revenue adds 2*5 = 10)
sell("pen", 3)        # another example

# 7. Print current inventory and total revenue
print("Inventory:", inventory)
print("Sales per product:", sales)
print("Total revenue:", revenue())
print("Purchases per product:", purchases)
