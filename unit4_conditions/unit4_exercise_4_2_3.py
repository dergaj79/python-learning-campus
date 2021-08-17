# 4.2.3 - this excerise will get a temperature value and convert it to farinait or celcuies:
input_String = input ("Insert the temperature you would like to convert: ")

input_temp_value = int (input_String[0:len(input_String)-1])
if (input_String.endswith("C") or input_String.endswith("c") ):
    fahrenheit_temp = str (((input_temp_value * 9) / 5) + 32)
    print("The convert temp Fahrenheit: ", fahrenheit_temp + "F")

elif (input_String.endswith("F") or input_String.endswith("f") ):
    celsius_temp = str (((input_temp_value - 32) * 5 ) / 9)
    print("The convert temp Celsius: ", celsius_temp + "C")
else:
    print("wrong input value please enter a value with sofix as follows 'F' or 'f'  or 'c' or 'C' ")  


# def temp_covertor (temp_string_to_convert):
#     input_temp_value = int (temp_string_to_convert[0:len(input_String)-1])
#     if (temp_string_to_convert.endswith("F")):    
#         print (temp_string_to_convert)
#         celsius_temp = str (((input_temp_value - 32) * 5 ) / 9)
#         print("The convert temp Celsius: ", celsius_temp + "C")
#         return celsius_temp

#     if (input_String.endswith("C")):
#         input_temp_value = int (temp_string_to_convert[0:len(input_String)-1])
#         print (input_temp_value)
#         fahrenheit_temp = str (((input_temp_value * 9) / 5) + 32)
#         print("The convert temp Fahrenheit: ", fahrenheit_temp + "F")
#         return fahrenheit_temp
