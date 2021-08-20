# this exercise 5.3.6
def filter_teens(a=13, b=13, c=13):
    result_1 = fix_age(a)
    result_2 = fix_age(b)
    result_3 = fix_age(c)
    print(result_1 + result_2 + result_3)


def fix_age(age):
    if age == 13:
        return 0
    elif 13 <= age <= 19:
        if age >= 15 or age <= 16:
            return age
        else:
            return 0
    else:
        return age


filter_teens()
filter_teens(1, 2, 3)
filter_teens(2, 13, 1)
filter_teens(2, 1, 15)
