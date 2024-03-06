print()
print('DISCOUNTED PRODUCT')
print()

# Receiving the name and value of the product
product_name = (input('Enter the product name: '))
value = (float(input('Enter the value of the product: ')))

# Discount calculation
discount = value * 0.12
total = value - discount

# Print the result
print()
print('COUPON')
print()
print(f'Product: {product_name}')
print(f'Value: {value:.2f} $')
print(f'Discount 12% OFF applied: {discount:.2f} $')
print()
print(f'Total: {total} $')
print()
