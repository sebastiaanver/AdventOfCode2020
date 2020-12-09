def part_1(sequence: list) -> (int, list):
    queue = []
    for number in sequence:
        number = int(number)
        if len(queue) == 25:
            if sum([(number - item in queue) for item in queue]) == 0:
                return number, queue
            queue.pop(0)
            queue.append(number)
        else:
            queue.append(number)


def part_2(sequence: list) -> None:
    number, queue = part_1(sequence)

    start_idx = 0
    while True and start_idx <= len(sequence) - 1:
        temp_list, idx = [], start_idx
        while sum(temp_list) <= number and idx <= len(sequence) - 1:
            temp_list.append(int(sequence[idx]))
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
