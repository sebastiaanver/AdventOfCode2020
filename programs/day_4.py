import numpy as np
import re


def part_1(lines: list) -> None:
    correct_passport = 0
    reg_exp = re.compile("([a-z]{3}):")

    for passport in lines:
        passport_fields_re = re.findall(reg_exp, passport)

        if (len(passport_fields_re) == 8) or (len(passport_fields_re) == 7 and "cid" not in passport_fields_re):
            correct_passport += 1

    print("Number of correct passports: ", correct_passport)


def special_match(string: str, search=re.compile(r'[a-f0-9]{6}').search) -> bool:
    return bool(search(string))


def check_fields(field_name:  str,  value: str) -> bool:
    if field_name == "byr":
        value = int(value)
        return 1920 <= value <= 2002
    elif field_name == "iyr":
        value = int(value)
        return 2010 <= value <= 2020
    elif field_name == "eyr":
        value = int(value)
        return 2020 <= value <= 2030
    elif field_name == "hgt":
        if value.isdigit():
            return False
        if value[-2:] == "in":
            value = int(value[:-2])
            return 59 <= value <= 76
        if value[-2:] == "cm":
            value = int(value[:-2])
            return 150 <= value <= 193
        else:
            return False
    elif field_name == "hcl":
        return value[0] == "#" and special_match(value[1:])
    elif field_name == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field_name == "pid":
        return len(value) == 9
    elif field_name == "cid":
        return True


def part_2(lines: list) -> None:
    correct_passport = 0
    for passport in lines:
        checks = []
        values = []
        passport_split = passport.split("\n")
        for passport_line in passport_split:
            passport_line = passport_line.split(" ")
            for field in passport_line:
                field_name, value = field.split(":")
                checks.append(check_fields(field_name, value))
                values.append(field_name)

        if len(values) == sum(checks) and ((len(values) == 8) or (len(values) == 7 and "cid" not in values)):
            correct_passport += 1

    print("Number of correct passports: ", correct_passport)


if __name__ == '__main__':
    file_name = "../input_files/day_4.txt"
    file = open(file_name, "r")
    lines = "".join(file.readlines())
    lines = lines.split("\n\n")

    # Problem 1
    part_1(lines)

    # Problem 2
    part_2(lines)
