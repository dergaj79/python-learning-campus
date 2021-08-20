# this exercise 5.3.6
#small = 1cm
# big = 5cm
# number_of_smalls_pecs +number_of_big_pecs == x
from builtins import print


def chocolate_maker(small, big, x):
    total_small= small*1
    total_big= big*5
    return (total_small + total_big) == x or total_big == x or total_small == x

print(chocolate_maker(3,1,8))
print(chocolate_maker(3,1,9))
print(chocolate_maker(3,2,10))