# defining the function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price - (price * (discount_percent / 100))
        print(f"The discount price of this product is {discount}")
    else:
        print(f"The price of this product is {price}")

# prompting the user to enter original price and discount percentage
original_price = int(input("Enter original price of product: "))
discount_percent = int(input("Enter discount percentage: "))

# Calling the function
calculate_discount(original_price, discount_percent)