import re


def part_1(lines: list) -> None:
    vowels = "aeiou"
    illegal_values = {"ab", "cd", "pq", "xy"}

    nice_string_count = sum(
        1
        for line in lines
        if len([letter for letter in line if letter in vowels]) >= 3
        and not any(val in line for val in illegal_values)
        and re.search(r"([a-z])\1", line)
    )

    print(nice_string_count)


def part_2(lines: list) -> None:

    nice_string_count = sum(
        1
        for line in lines
        if len(re.findall(r"([a-z]{2}).*\1", line)) and re.findall(r"([a-z]).\1", line)
    )

    print(nice_string_count)


if __name__ == "__main__":
    file_name = "../input_files/day_5.txt"
    file = open(file_name, "r")
    lines = file.readlines()

    part_1(lines)
    part_2(lines)
