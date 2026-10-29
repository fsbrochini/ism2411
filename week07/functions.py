# Self-Assessment
#
# Q1: The first bug I noticed was the lack of a colon after for sale in sales on line 10. 
# This was evident from the traceback since Python raised a syntax error before executing the code, 
# but the error explanation was not immediately intuitive to me, so I had to ask AI 
# to clarify what expected ‘:’ meant. This suggests that my first reaction to a bug is to turn to 
# AI rather than attempt to understand the error based on the traceback. However, in this case, 
# the traceback already indicated the line and the nature of the issue, so I will try to read it 
# more carefully in the future and explain the error to myself out loud before consulting AI.
#
# Q2: The function apply_discount takes two arguments: a price (a numeric value) and a tier (a string). 
# It applies a discount based on the tier: “gold” gets 15%, “silver” gets 10%, “bronze” gets 5%, and other 
# tiers get no discount. It returns the resulting value. Someone using this function would not need to read
# the body if they know the tiers and the associated discounts.
#
# AI Disclosure: I used Claude (an AI assistant) during this lab to help debug
# errors in my code and to explain what certain lines of code were doing so I
# could understand them.


# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0
    return price * (1 - discount)

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + calculate_tax(discounted, 0.07):.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90]

# Fix 1: total = sale replaced the total each time, so it ended up
# as just the last sale. Changed to += so each sale adds to the total.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Fix 2: the for loop line was missing a colon at the end, which
# caused a SyntaxError.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Fix 3: i <= len(sales) let i reach 5, but the last index is 4,
# which caused an IndexError. Changed <= to <.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
x = 100   # global variable

def double_it():
    x = 999   # local variable, different from global x
    return x * 2

print(x)           # prints 100
print(double_it()) # prints 1998
print(x)           # still 100

# Scope explanation: The x inside double_it() is a local variable.
# It only exists while the function runs, so setting it to 999
# does not touch the global x outside. That is why x prints 100
# both before and after calling the function.
