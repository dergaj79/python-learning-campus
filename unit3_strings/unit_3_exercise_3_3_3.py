
encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
print ("orginal encrypted message: ",encrypted_message,"\norginal encrypted_message length: ", len(encrypted_message))

# convert_message = encrypted_message[57::-1]

# print ("convert_message: ", convert_message,"\nstring_length:",len(convert_message))
uncrypted_message = (encrypted_message[57::-1])[0::2]
print ("uncrypted_message : ",uncrypted_message,"\nuncrypted message length:",len(uncrypted_message))






