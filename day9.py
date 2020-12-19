# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


PREAMBLE = 25

VALUE = 0

# Not sum of first preamble numbers
def find_invalid_number():
    file = open("./inputs/day9.bat")
    data = file.readlines()
    data = [int(line) for line in data]
    value__not_achieved_by_sum = 0

    for i in range(PREAMBLE, len(data) - 1):
        status = False
        stored_values = data[i - 25:i]
        print(len(stored_values))
        for j in stored_values:
            for k in stored_values:
                if j + k == data[i]:
                    print(j, k, data[i])
                    status = True
        if status.__eq__(False):
            value__not_achieved_by_sum = data[i]

    print(value__not_achieved_by_sum)

    # part 2

    for i in range(4, int(len(data) / 2)):
        for j in data:
            index = data.index(j)
            combination = data[index:index + i]
            if sum(combination) == value__not_achieved_by_sum:
                required_value = min(combination) + max(combination)
                print("value needed", required_value)
    print("complete program ended")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_invalid_number()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
