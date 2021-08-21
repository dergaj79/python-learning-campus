
def list_exercise621():
    list_1 = [1,2,3,4]
    list_2 = [5,6,7]
    list_3 = list_1 + list_2
    list_4 =  [list_1 + list_2]
    print("list_1" ,list_1)
    print("list_2" ,list_2)
    print("list_3" ,list_3)
    print("list_4", list_4)
    print(len(list_3))
    print(len(list_4))
    print(list_1[2] + list_3[4])
    #print(list_4[3])
    print(list_4[0][3])
    print(len(list_2*list_1[1]))


def main():
    list_exercise621()

if __name__ == "__main__":
    main()