# Question:
# Given a dictionary of products and their prices, find the product with the highest price.

# Question:
# Given a dictionary of products and their prices, find the product with the highest price.

products = {
    "Laptop": 75000,
    "Phone": 50000,
    "Tablet": 30000,
    "Monitor": 20000
}

print(len(products))   # 3 → total items


count = 0   # counter

for product in products:
    count += 1   # increase every loop
    print(product)

print("Loop executed:", count)   # 3


# Number of items = number of loop executions

# ✅ 1. Key print
for product in products:
    print(product)   # Laptop, Phone...


# ✅ 2. Value print
for product in products:
    print(products[product])   # 75000, 50000...


# ✅ 3. Key + Value together
for product in products:
    print(product, products[product])



# ✅ 4. Type check
for product in products:
    print(type(product))   # <class 'str'>


# ✅ 5. Condition check
for product in products:
    if products[product] > 40000:
        print(product)


# ✅ 6. Index-like counter (C style feeling 😄)
i = 0
for product in products:
    print(i, product)
    i += 1


# ✅ 7. Using items() 
for key, value in products.items():
    print(key, value)

# for product in products:
#     # print(product, products[product])
#     # print(product)
#     print(products)

# highest_product = ""
# highest_price = 0

# for product in products:
#     if products[product] > highest_price:
#         highest_price = products[product]
#         highest_product = product

# print("Products:", products)
# print("Product with highest price:", highest_product)
# print("Price:", highest_price)


