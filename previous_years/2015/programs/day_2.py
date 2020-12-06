def part_1(lines: list) -> None:
    sq_feet_total = 0

    for line in lines:
        l, w, h = list(map(int, line.split("x")))

        dims = [l * w, w * h, l * h]

        sq_feet_total += min(dims) + sum(dims) * 2

    print(f"Total number of sq feet needed: {sq_feet_total}")


def part_2(lines: list) -> None:
    ribbon_length = 0

    for line in lines:
        dimensions = list(map(int, line.split("x")))
        l, w, h = dimensions

        min_values = min(dimensions)
        dimensions.remove(min_values)

        ribbon_length += l * w * h + 2 * min_values + 2 * min(dimensions)

    print(f"Total length of ribbon needed: {ribbon_length}")


if __name__ == "__main__":
    file_name = "../input_files/day_2.txt"
    file = open(file_name, "r")
    lines = file.readlines()

    part_1(lines)
    part_2(lines)
