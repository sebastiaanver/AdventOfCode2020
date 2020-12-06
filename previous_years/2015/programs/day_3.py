"""
Currently keeping track of the number of times a house is visited, but we don't really care about
this, so keeping tracks of the number of addresses in a set would be better than storing this info
in a dictionary.
"""


def part_1(line: list) -> None:
    visit_dict = {}

    x, y = 0, 0
    visit_dict[f"{x}-{y}"] = 1

    for move in line:
        if move == ">":
            x += 1
        elif move == "v":
            y -= 1
        elif move == "<":
            x -= 1
        elif move == "^":
            y += 1

        if f"{x}-{y}" in visit_dict:
            visit_dict[f"{x}-{y}"] += 1
        else:
            visit_dict[f"{x}-{y}"] = 1

    print(len(visit_dict))


def part_2(line: list) -> None:
    visit_dict = {}

    x_santa, y_santa = 0, 0
    x_santa_bot, y_santa_bot = 0, 0
    visit_dict[f"{x_santa}-{y_santa}"] = 2

    for idx, move in enumerate(line):
        print(idx, move, idx % 2, idx % 1)
        if idx % 2 == 0:  # Santa
            if move == ">":
                x_santa += 1
            elif move == "v":
                y_santa -= 1
            elif move == "<":
                x_santa -= 1
            elif move == "^":
                y_santa += 1

            if f"{x_santa}-{y_santa}" in visit_dict:
                visit_dict[f"{x_santa}-{y_santa}"] += 1
            else:
                visit_dict[f"{x_santa}-{y_santa}"] = 1
        else:  # Santa-bot
            if move == ">":
                x_santa_bot += 1
            elif move == "v":
                y_santa_bot -= 1
            elif move == "<":
                x_santa_bot -= 1
            elif move == "^":
                y_santa_bot += 1

            if f"{x_santa_bot}-{y_santa_bot}" in visit_dict:
                visit_dict[f"{x_santa_bot}-{y_santa_bot}"] += 1
            else:
                visit_dict[f"{x_santa_bot}-{y_santa_bot}"] = 1

    print(len(visit_dict))


if __name__ == "__main__":
    file_name = "../input_files/day_3.txt"
    file = open(file_name, "r")
    lines = file.readline()

    part_1(lines)
    part_2(lines)
