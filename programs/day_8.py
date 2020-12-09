def part_1(lines: list) -> (bool, int):

    acc, line_nr = 0, 0
    visited = []

    while True:
        if line_nr in visited:
            return False, acc
        visited.append(line_nr)

        if line_nr >= len(lines):
            print(f"reached last line: {acc}")
            return True, acc

        instruction, number = lines[line_nr].split(" ")

        if instruction == "acc":
            acc += int(number)
            line_nr += 1
        elif instruction == "jmp":
            line_nr += int(number)
        elif instruction == "nop":
            line_nr += 1


def part_2(lines: list) -> None:

    for idx, line in enumerate(lines):
        instruction, number = line.split(" ")

        if instruction != "acc":
            instruction_new = "jmp" if instruction == "nop" else "nop"
            lines[idx] = f"{instruction_new} {number}"

            reached_end, acc = part_1(lines)

            if reached_end:
                return

            lines[idx] = f"{instruction} {number}"


if __name__ == "__main__":
    file_name = "../input_files/day_8.txt"
    file = open(file_name, "r")
    lines = file.readlines()

    # Problem 1
    part_1(lines)

    # Problem 2
    part_2(lines)
