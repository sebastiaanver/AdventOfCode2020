import pandas as pd


def part_1(line: str) -> None:
    up = line.count("(")
    down = line.count(")")

    print(f"Final floor is: {up - down}")


def part_2(line: str) -> None:
    current_level = 0
    move_dict = {"(": 1, ")": -1}

    for step, move in enumerate(line):
        current_level += move_dict[move]
        if current_level < 0:
            print(f"basement is reached after {step + 1} steps")
            break


if __name__ == "__main__":
    file_name = "../input_files/day_1.txt"
    file = open(file_name, "r")
    line = file.readline()

    part_1(line)
    part_2(line)
