import pandas as pd


def part_1(data: set) -> None:
    for values in data:
        if 2020 - values in data:
            print(values * (2020 - values))
            return


def part_2(data: set) -> None:
    for values in data:
        for val in data:
            if 2020 - (values + val) in data:
                print((2020 - (values + val)) * values * val)
                return


if __name__ == "__main__":
    data = pd.read_csv("../input_files/day_1.txt", header=None)[0].values
    data = set(data)
    print(type(data))

    part_1(data)
    part_2(data)
