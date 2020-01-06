def last_early(my_str):
    string_index = len(my_str)-1
    print("numbe of char to scanning: ", string_index)
    last_char = my_str[-1]
    print("last char for input string:", last_char) 
    
    if last_char in my_str[0:-1:1]: 
        print("true") 
    else: print("false") 
    return my_str

input_String = input ("Enter string to to find if the last char is exiting before: ")
last_early(input_String)