print ("this is a solution to exericse 3.4.3")
print ()
input_string = input ("Please enter a string: ")

split_string_value = len(input_string)//2
print("string length:",len(input_string))
# print("split_string_value: ",split_string_value)
string_first_part = input_string[0:split_string_value].lower()
string_last_part = input_string[split_string_value:len(input_string)].upper()
print("final_string: ",string_first_part+string_last_part)

