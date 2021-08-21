# this exercise 5.3.4
def last_early(my_str):
    last_char =my_str[-1]
    result= False
    for char in my_str[0:-1]:
        if (char==last_char):
            result= True
            return result
    return result

result_value_0 = last_early("happy birthday")
result_value_1 = last_early("best of luck")
result_value_2 = last_early("WOW")
result_value_3 = last_early("X")
print(result_value_0)
print(result_value_1)
print(result_value_2)
print(result_value_3)