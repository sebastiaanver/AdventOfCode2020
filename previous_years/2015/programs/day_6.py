import numpy as np
import re


def part_1(lines: list) -> None:
    m = np.zeros(shape=(1000, 1000))

    for line in lines:
        numbers = re.findall("([0-9]*,[0-9]*)", line)
        x_start, y_start, x_end, y_end = [
            *numbers[0].split(","),
            *numbers[1].split(","),
        ]
        x_start = int(x_start)
        y_start = int(y_start)
        x_end = int(x_end) + 1
        y_end = int(y_end) + 1

        if "toggle" in line:
            sub_m = m[x_start:x_end, y_start:y_end].copy()
            where_0 = np.where(sub_m == 0)
            where_1 = np.where(sub_m == 1)
            sub_m[where_0] = 1
            sub_m[where_1] = 0

            m[x_start:x_end, y_start:y_end] = sub_m

        elif "turn on" in line:
            m[x_start:x_end, y_start:y_end] = 1

        elif "turn off" in line:
            m[x_start:x_end, y_start:y_end] = 0

    print(len(m[np.where(m == 1)]))


def part_2(lines: list) -> None:
    m = np.zeros(shape=(1000, 1000))

    for line in lines:
        numbers = re.findall("([0-9]*,[0-9]*)", line)
        x_start, y_start, x_end, y_end = [
            *numbers[0].split(","),
            *numbers[1].split(","),
        ]
        x_start = int(x_start)
        y_start = int(y_start)
        x_end = int(x_end) + 1
        y_end = int(y_end) + 1

        if "toggle" in line:
            m[x_start:x_end, y_start:y_end] += 2

        elif "turn on" in line:
            m[x_start:x_end, y_start:y_end] += 1

        elif "turn off" in line:
            sub_m = m[x_start:x_end, y_start:y_end].copy()
            where_not_0 = np.where(sub_m != 0)
            sub_m[where_not_0] -= 1
            m[x_start:x_end, y_start:y_end] = sub_m

    print(int(np.sum(m)))


if __name__ == "__main__":
    file_name = "../input_files/day_6.txt"
    file = open(file_name, "r")
    lines = file.readlines()

    part_1(lines)
    part_2(lines)
