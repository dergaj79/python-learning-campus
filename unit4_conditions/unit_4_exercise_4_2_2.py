# 4.2.2 - this excerise will get a string from a user and print OK if the string is palindrome if not will print NOT
input_string = input ("Please enter a string: ")

rev = ''.join(reversed(input_string))
# revert_string = input_string[::-1]
print ("input_string",input_string)
# print ("revert_string",revert_string)
print ("rev",rev)

if (input_string == rev):
    print ("OK")
else:
    print("NO")




