
number = int (input("Enter three digits (each digit for one pig)):"))
first_digit = int(number/100)
second_digit = (int((number%100)/10))
third_digit = int(number%10)

total_value = first_digit + second_digit + third_digit

print("Sum of all blocks collected by all pigs     : " , total_value)
print("the number of blocks collected by each pig  : " , int(total_value/3))
print ("barrer of divided of sum by number of pigs  : " , total_value%3)
print ("the barrar is true of false                 : " , total_value%3 == 0)
