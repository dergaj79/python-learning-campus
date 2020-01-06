# a= 10
# b= 10
# a =4
# print (a,b)
I_am_hungry = 2
number_of_sandwitches = 4
# number_of_sandwitches == 4
cups_of_coffee = 3
# print(not (number_of_sandwitches != 5))
# print(number_of_sandwitches == 4  and cups_of_coffee == 4)
# print((number_of_sandwitches == 4 )  or (cups_of_coffee == 4 ))
# str1 = "break"
# str2 =  'breakfast'
# print (str1 in str2)

# help()
# brothers_num =  3
# is_big_family = brothers_num > 20 
# print(is_big_family)

# true_or_false = "alpha" < "beta"
# print(true_or_false)
# true_or_false = 18
# print ( true_or_false <= 22 < 30)
# print (true_or_false = not(10))

# name  = input ("Please enter your name: ")
# print("********************************")
# print("Your name is : " , name)
# print ("Dasta" in name)
# print (name.swapcase)
# number = int(input ("Please enter a number : "))

# number = input ("Please enter a number : ")
# print(int(number))
# print(int(number)** 2)
# print(float(number))
# print(number)

# fairy_tale = "The Ugly Ducking"
# swan_height = 90.7
# eggs_num = 4

# print (int(swan_height))
# # print (int(fairy_tale))
# surprise = bool(eggs_num)
# print (str(surprise))

number = int (input("Enter three digits (each digit for one pig)):"))
first_digit = int(number/100)
second_digit = (int((number%100)/10))
third_digit = int(number%10)
# print(first_digit)
# print(second_digit)
# print(third_digit)

total_value = first_digit + second_digit + third_digit
# isSumDivedByNumberOfPigsWithOutBarrer

print("Sum of all blocks collected by all pigs     : " , total_value)
print("the number of blocks collected by each pig  : " , int(total_value/3))
print ("barrer of divided of sum by number of pigs  : " , total_value%3)
print ("the divide have barrer or not               : " , total_value%3 == 0)






