print ("this is a solution to exericse 3.4.2")
print ()
input_string = input ("Please enter a string: ")
extracted_first_char_from_givan_string = input_string[0]
print("extract first char from givan string: ",extracted_first_char_from_givan_string)
print("Orginal entered string is: ", input_string)
string_after_replaced_by_e_char = input_string[1:len(input_string)].replace(extracted_first_char_from_givan_string,"e",-1)
print ("new string: ",input_string.replace(input_string[1:len(input_string)],string_after_replaced_by_e_char) )


