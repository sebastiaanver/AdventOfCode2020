import hashlib


def part_1_and_2(line: list, match: str) -> None:
    i = 0
    while True:
        hash_val = hashlib.md5((line + str(i)).encode()).hexdigest()
        if hash_val.startswith(match):
            print(f"Answer for {len(match)} zeros: {i}")
            break
        i += 1


if __name__ == "__main__":
    file_name = "../input_files/day_4.txt"
    file = open(file_name, "r")
    lines = file.readline()

    part_1_and_2(lines, "00000")
    part_1_and_2(lines, "000000")
