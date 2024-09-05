#creating the function
def calculate_discount(original_price, discount_percentage):
    if discount_percentage >= 20:
        discount = original_price * (discount_percentage / 100)
        final_price = original_price - discount
        return final_price
    else:
        return original_price
# asking the user for input   
original_price = (float(input("What is the price of the item? ")))
discount_percentage = (float(input("What percentage is the discount? ")))

#calling the function and displaying the result
final_price = calculate_discount(original_price, discount_percentage)
print(f"The resulting price is {final_price}")
 
    




