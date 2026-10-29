# Reflection
#
# 1. The most surprising thing about lists was how you can easily slice
#    them. I had assumed I would have to use a loop to get parts of a
#    list, but using [::2] gets every other item in the list. Also the
#    negative indexes were new to me. This means that I can easily get
#    the last item in a list by counting from the end.
#
# 2. In my pressure washing business I had written down all the prices
#    of jobs in Excel and then added them up manually. Using a list in
#    Python I can store all the prices and then use the functions sum(),
#    max() and min() to get the total, best and worst jobs straight away.
#    I can also use a loop to filter out any jobs above a certain price.


# Exercise 1: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index practice
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3: Slicing
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4: Modify
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5: Tuple comparison
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples can't be changed, which is useful for coordinates because")
    print("a location should stay fixed and never get changed by accident.")
print(coords)

# Exercise 6: Average of a list of sales
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7: Accumulator pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print("Original:", prices)
print("Discounted:", discounted)

# Exercise 8: Filter above threshold
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
