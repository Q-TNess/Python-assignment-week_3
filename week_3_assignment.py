#--Creating the calculate_discount function while applying the if conditional statement for a discount < 20%
def calculate_discount(price,discount_percent):
   if discount_percent < 20:
      return price
   return price - (price * discount_percent / 100)

#-- examples
print("Final price =",calculate_discount(150,10))
print("Final price =",calculate_discount(200,25))
print("Final price =",calculate_discount(600,55))