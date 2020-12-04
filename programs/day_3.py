import numpy as np


def part_1(lines: list, right: int) -> None:
    x = 0
    tree_counter = 0
    for line in lines:
        line = line.strip('\n')*100

        if line[x] == "#":
            tree_counter += 1
        x += right

    print("Number of trees encountered on the path: ", tree_counter)


def part_2(lines: list, slopes: list) -> None:
    trees = []

    for right, down in slopes:
        x = 0
        tree_counter = 0
        lines_t = [line_t for idx, line_t in enumerate(lines) if idx % down == 0]
        for line in lines_t:
            line = line.strip('\n') * 100

            if line[x] == "#":
                tree_counter += 1

            x += right
        trees.append(tree_counter)

    print("Product of trees found on the paths: ", np.prod(trees))


if __name__ == '__main__':
    file_name = "../input_files/day_3.txt"
    file = open(file_name, "r")
    lines = file.readlines()

    # Problem 1
    right, down = 3, 1
    part_1(lines, right)

    # Problem 2
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    part_2(lines, slopes)
