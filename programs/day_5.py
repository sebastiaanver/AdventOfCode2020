def part_1(lines: list) -> None:
    max_id = 0
    for line in lines:
        line = line.strip("\n")
        row_sequence = line[:7]
        col_sequence = line[7:]
        # row_nr = calculate_row(row_sequence)
        row_nr = calculate_row_binary(row_sequence)
        col_nr = col_dict[col_sequence]

        seat_id = row_nr * 8 + col_nr

        max_id = seat_id if seat_id > max_id else max_id

    print(f"Maximum id on the plane: {max_id}")


def part_2(lines: list) -> None:
    plane_dict = {}

    for line in lines:
        line = line.strip("\n")
        row_sequence = line[:7]
        col_sequence = line[7:]
        row_nr = calculate_row(row_sequence)
        col_nr = col_dict[col_sequence]

        if row_nr in plane_dict:
            plane_dict[row_nr]["count"] += 1
            plane_dict[row_nr]["col_nrs"].append(col_nr)
        else:
            plane_dict[row_nr] = {"count": 1, "col_nrs": [col_nr]}
    for row_nr, value in plane_dict.items():
        if value["count"] == 7:
            col_nr = set({0, 1, 2, 3, 4, 5, 6, 7}.difference(set(value["col_nrs"])))
            print(row_nr * 8 + col_nr.pop())


def calculate_row(sequence: str, lower_bound: int = 0, upper_bound: int = 127) -> int:
    """Recursive (less efficient) way"""
    if len(sequence) == 1:
        return lower_bound if sequence[0] == "F" else upper_bound

    if sequence[0] == "F":
        return calculate_row(
            sequence[1:],
            lower_bound=lower_bound,
            upper_bound=int((lower_bound + upper_bound) // 2),
        )
    else:
        return calculate_row(
            sequence[1:],
            lower_bound=int(round((lower_bound + upper_bound) / 2)),
            upper_bound=upper_bound,
        )


def calculate_row_binary(sequence: str) -> int:
    """String can be seen as binary."""
    sequence = sequence.replace("B", "1").replace("F", "0")
    return int(sequence, 2)


col_dict = {
    "LLL": 0,
    "LLR": 1,
    "LRL": 2,
    "LRR": 3,
    "RLL": 4,
    "RLR": 5,
    "RRL": 6,
    "RRR": 7,
}


if __name__ == "__main__":
    file_name = "../input_files/day_5.txt"
    file = open(file_name, "r")
    lines = file.readlines()

    # Problem 1
    part_1(lines)

    # Problem 2
    part_2(lines)
