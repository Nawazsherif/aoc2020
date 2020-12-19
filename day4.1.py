# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def check_passport_isvalid(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    count = 0
    for field in required_fields:
        if str(passport).__contains__(field):
            count += 1
    return count == 7


def sum_of_valid_passports():
    file = open("./inputs/day4.bat", "r")
    complete_passport = ""
    valid_passport_count = 0
    for line in file:
        if line == "\n":
            valid_passport_count += int(check_passport_isvalid(complete_passport))
            complete_passport = ""
        else:
            complete_passport += line
    valid_passport_count += int(check_passport_isvalid(complete_passport))
    print(valid_passport_count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum_of_valid_passports()
