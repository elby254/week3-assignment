def subtraction (x, y): # x=price, y=discount_percentage
     return x-y

#define values of x and y
price=100
discount_percentage=20

result= subtraction(100, 20)
if result >=20:
     print(result)
else:
     print(price)     


#Find final price
def subtraction (x, y): # x=price, y=discount_percentage
    discount_amount = x * (y / 100)   # calculate discount
    final_price = x - discount_amount # apply discount
    return final_price                # return the result

#define values of x and y 
price= 1000
discount_percentage=75

#call the function
print(subtraction(price, discount_percentage))







