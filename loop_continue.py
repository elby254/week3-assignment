#example of loop continue
for number in range (1,10):
    if number % 2 == 0: # we use % for statement division 
        continue #skip the rest of the loop for even numbers
    print (number)