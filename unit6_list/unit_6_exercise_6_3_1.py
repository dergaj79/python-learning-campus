def list_exercise631():
    list_1 = [0.6, 1, 2, 3]
    list_2 = [3, 2, 0.6, 1]
    list_3 = [9, 0, 5, 10.5]
    list_1.sort()
    list_2.sort()
    list_3.sort()
    print(list_1)
    print(list_2)
    print(list_3)
    result_1 = are_lists_equal(first_list=list_1, second_list=list_2)
    result_2 = are_lists_equal(first_list=list_1, second_list=list_3)
    print(result_1)
    print(result_2)


def are_lists_equal(first_list, second_list):
    return second_list == first_list


def main():
    list_exercise631()


if __name__ == "__main__":
    main()
