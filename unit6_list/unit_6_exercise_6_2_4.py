def list_exercise624():
    x = [4, 5, 6]
    y = [1, 2, 3]
    print(x)
    print(y)
    marge_list = extend_list_x(x, y)
    print(marge_list)


def extend_list_x(list_x, list_y):
    list_y.insert(3, list_x[0])
    list_y.insert(4, list_x[1])
    list_y.insert(5, list_x[2])
    print(type(list_y))
    return list_y


def main():
    list_exercise624()


if __name__ == "__main__":
    main()
