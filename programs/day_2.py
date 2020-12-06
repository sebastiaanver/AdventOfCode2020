def part_1(lines: list) -> None:
    valid_passwords = 0
    for line in lines:
        line = line.strip("\n")
        split_lines = line.split(" ")
        lower_bound, upper_bound = [int(x) for x in split_lines[0].split("-")]
        criteria_letter = split_lines[1][0]

        letter_count = split_lines[-1].count(criteria_letter)

        if lower_bound <= letter_count <= upper_bound:
            valid_passwords += 1
    print("Number of valid passwords:", valid_passwords)


def part_2(lines: list) -> None:
    valid_passwords = 0
    for line in lines:
        line = line.strip("\n")
        split_lines = line.split(" ")
        lower_bound, upper_bound = [int(x) for x in split_lines[0].split("-")]
        criteria_letter = split_lines[1][0]
        password = split_lines[-1]

        places_correct = sum(
            [
                password[lower_bound - 1] == criteria_letter,
                password[upper_bound - 1] == criteria_letter,
            ]
        )

        if places_correct == 1:
            valid_passwords += 1

    print("Number of valid passwords:", valid_passwords)


if __name__ == "__main__":
    file_name = "../input_files/day_2.txt"
    file = open(file_name, "r")
    lines = file.readlines()

    part_1(lines)
    part_2(lines)
