def calculate_discount(price, discount_percent):
  """
  This function calculates the final price after applying a discount.

  Args:
      price: The original price of the item.
      discount_percent: The discount percentage (0 to 100).

  Returns:
      The final price after applying the discount.
  """
  discount = price * discount_percent / 100
  if discount_percent >= 20:
    return price - discount
  else:
    return price

# User input for price and discount
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (0 to 100): "))

# Calculate and print final price
final_price = calculate_discount(original_price, discount_percent)

print(f"Original price: Ksh. 4{original_price:.2f}")
print(f"Discount: {discount_percent}%")

if final_price != original_price:
  print(f"Final price after discount: Ksh. {final_price:.2f}")
else:
  print("No discount applied.")

