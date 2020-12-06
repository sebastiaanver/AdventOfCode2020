def part_1(lines: list) -> None:
    total_answers = 0
    for line in lines:
        line = line.replace("\n", "")
        total_answers += len(set(line))
    print(f"Answer part 1: {total_answers}")


def part_2(lines: list) -> None:
    total_answers = 0
    for line in lines:
        line = line.split("\n")
        set_list = [set(answer) for answer in line]
        total_answers += len(set.intersection(*set_list))
    print(f"Answer part 2: {total_answers}")


if __name__ == "__main__":
    file_name = "../input_files/day_6.txt"
    file = open(file_name, "r")
    lines = "".join(file.readlines())
    lines = lines.split("\n\n")

    # Problem 1
    part_1(lines)

    # Problem 2
    part_2(lines)
