# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# part 1 solved

def find_resulting_number_from_commands():
    file = open("./inputs/day8.bat")
    data = file.readlines()
    data = [line for line in data]
    visited_indexes = []
    result = 0
    i = 0
    while i not in visited_indexes:
        visited_indexes.append(i)
        command = data[i].split(" ")[0]
        operation = data[i].split(" ")[1][0]
        number = int(data[i].split(" ")[1][1:])

        if command == "acc":
            if operation == "+":
                result += number
            elif operation == "-":
                result -= number
            i += 1
        elif command == "nop":
            i += 1
        elif command == "jmp":
            if operation == "+":
                i += number
            elif operation == "-":
                i -= number

    print(visited_indexes)
    print(result)
    print(i)

    print("complete program ended")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_resulting_number_from_commands()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
