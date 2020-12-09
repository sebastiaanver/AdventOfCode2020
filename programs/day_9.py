
def part_1(lines: list):
    queue = []
    for line in lines:
        if len(queue) == 25:
            if sum([(int(line) - item in queue) for item in queue]) == 0:
                return int(line), queue
            queue.pop(0)
            queue.append(int(line))
        else:
            queue.append(int(line))


def part_2(lines: list) -> None:
    number, queue = part_1(lines)

    start_idx = 0
    while True and start_idx <= len(lines) - 1:
        temp_list, idx = [], start_idx
        while sum(temp_list) <= number and idx <= len(lines) - 1:
            temp_list.append(int(lines[idx]))
            idx += 1

            if sum(temp_list) == number and len(temp_list) >= 2:
                print(min(temp_list) + max(temp_list))

        start_idx += 1


if __name__ == "__main__":
    file_name = "../input_files/day_9.txt"
    file = open(file_name, "r")
    lines = file.readlines()

    # Problem 1
    part_1(lines)

    # Problem 2
    part_2(lines)
