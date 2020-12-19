# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def calculateSeatID(seatBinary):
    upper_row = 127
    lower_row = 0
    upper_column = 7
    lower_column = 0

    for digit in seatBinary:
        rows_by_two = (upper_row - lower_row + 1) / 2
        columns_by_two = (upper_column - lower_column + 1) / 2
        if digit == "F":
            upper_row = upper_row - rows_by_two
        if digit == "B":
            lower_row = lower_row + rows_by_two
        if digit == "L":
            upper_column = upper_column - columns_by_two
        if digit == "R":
            lower_column = lower_column + columns_by_two

    return lower_row * 8 + lower_column


def calculate_test():
    assert calculateSeatID("FBFBBFFRLR") == 357


def getMaxSeatID():
    max_seat_id = 0
    list_of_ids = []
    file = open("./inputs/day5.bat", "r")
    for line in file:
        seat_id = calculateSeatID(line)
        list_of_ids.append(int(seat_id))
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    list_of_ids.sort()

    # part 2 code
    last_index = len(list_of_ids) - 1
    for i in range(list_of_ids[0], list_of_ids[last_index]):
        if i not in list_of_ids:
            print("missing seat id " + str(i))
    print("max seat id " + str(max_seat_id))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getMaxSeatID()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
