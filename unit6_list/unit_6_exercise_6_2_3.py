def list_exercise623():
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    result = format_list(my_list)
    #print(result)
    print(f"{result[0][0]}"+"," + f" {result[0][1]}"+ "," + f" {result[0][2]}"+ "," + f" and {result[1]}")


def format_list(my_list):
    pair_list = my_list[0:-1:2]
    last_item = my_list[-1]
    #return string_format
    return pair_list,last_item


def main():
    list_exercise623()

if __name__ == "__main__":
    main()