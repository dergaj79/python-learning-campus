# this exercise 5.2.1
print(" exercise number 1")
a = 1
def foo1():
    print(a)

foo1()
print(a)

#####################
print(" exercise number 2")
b=1
def foo2():
    b=2
    print(b)


foo2()
print(b)

####################
# print(" exercise number 3")
# c=1
# def foo3():
#     c=c+1
#     print(c)
#
#
# foo3()
# print(c)
###################################
print(" exercise number 4")

d=1
def foo4():
    global d
    d=2
    print(d)


foo4()
print(d)

