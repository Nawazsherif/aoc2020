# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re
import pytest

valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_passport_isvalid(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    count = 0
    passport = passport.replace("\n", " ")
    passport = passport.split(" ")
    if "" in passport:
        passport.remove("")

    passport_keys = list(map(lambda x: x.split(":")[0], passport))
    passport_values = list(map(lambda x: x.split(":")[1], passport))
    passport_dict = dict(zip(passport_keys, passport_values))

    for field in required_fields:
        if str(passport).__contains__(field):
            if field in passport_validations:
                count += int(passport_validations.get(field, lambda x: False)(passport_dict.get(field)))
    return count == 7


def check_pid_is_valid(x):
    return len(x) == 9


def check_hgt_is_valid(x):
    unit_validations = {
        "cm": lambda y: 150 <= y <= 193,
        "in": lambda z: 59 <= z <= 76
    }
    str_len = len(x)
    height = x[0:str_len - 2]
    unit = x[str_len - 2:]
    if unit in unit_validations and str_len > 2:
        hgt_is_valid = unit_validations.get(unit, lambda z: False)(int(height))
        return bool(hgt_is_valid)
    return False


def check_hcl_is_valid(x):
    pattern = "^#[0-9a-f]{6}$"
    is_hcl_valid = re.match(pattern, x)
    return bool(is_hcl_valid)


passport_validations = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "ecl": lambda x: x in valid_ecl,
    "pid": lambda x: check_pid_is_valid(x),
    "hcl": lambda x: check_hcl_is_valid(x),
    "hgt": lambda x: check_hgt_is_valid(x)
}


def test_byr_validation():
    assert passport_validations.get("byr", lambda x: False)("2003").__eq__(False), "invalid byr"
    assert passport_validations.get("byr", lambda x: False)("1919").__eq__(False), "invalid byr"
    assert passport_validations.get("byr", lambda x: False)("1920").__eq__(True), "valid byr"
    assert passport_validations.get("byr", lambda x: False)("2002").__eq__(True), "valid byr"


def test_pid_validation():
    assert passport_validations.get("pid", lambda x: False)("000000000").__eq__(True), "valid pid"
    assert passport_validations.get("pid", lambda x: False)("012345678").__eq__(True), "valid pid"
    assert passport_validations.get("pid", lambda x: False)("321930083").__eq__(False), "invalid pid"
    assert passport_validations.get("pid", lambda x: False)("000032432444").__eq__(False), "invalid pid"


def test_hcl_validation():
    assert passport_validations.get("hcl", lambda x: False)("#026abc").__eq__(True), "valid hcl"
    assert passport_validations.get("hcl", lambda x: False)("0123456").__eq__(False), "valid hcl"
    assert passport_validations.get("hcl", lambda x: False)("#21930083").__eq__(False), "invalid hcl"
    assert passport_validations.get("hcl", lambda x: False)("#abclo2").__eq__(False), "invalid hcl"


def test_ecl_validation():
    assert passport_validations.get("ecl", lambda x: False)("amb").__eq__(True), "invalid ecl"
    assert passport_validations.get("ecl", lambda x: False)("blu").__eq__(True), "invalid ecl"
    assert passport_validations.get("ecl", lambda x: False)("brn").__eq__(True), "valid ecl"
    assert passport_validations.get("ecl", lambda x: False)("grn").__eq__(True), "valid ecl"
    assert passport_validations.get("ecl", lambda x: False)("nsa").__eq__(False), "valid ecl"


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
