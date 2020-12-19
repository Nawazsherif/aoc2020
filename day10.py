# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

threshold_value = 3


def find_adapter_sequence():
    file = open("./inputs/day10.bat")
    data = file.readlines()
    data = [int(line) for line in data]
    print(data)
    starting_point = 0
    one_volt_difference = 0
    two_volt_difference = 0
    # since last adapter has one three volt difference
    three_volt_difference = 1
    first_seq = []
    i = starting_point

    while True:
        if i + 1 in data:
            one_volt_difference += 1
            first_seq.append(i)
            i = i + 1
        elif i + 2 in data:
            two_volt_difference += 1
            first_seq.append(i)
            i = i + 2
        elif i + 3 in data:
            three_volt_difference += 1
            first_seq.append(i)
            i = i + 3
        else:
            first_seq.append(i)
            break
    print(one_volt_difference)
    print(three_volt_difference)
    print(one_volt_difference * three_volt_difference)
    print(max(data))
    print(first_seq)
    print(len(first_seq) - 1)
    print(len(data))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_adapter_sequence()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
