def list_exercise632():
    list_1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list_1))


def longest(my_list):
    res =  max(my_list, key=len)
    return res


def main():
    list_exercise632()


if __name__ == "__main__":
    main()
