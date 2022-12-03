from typing import Tuple, List


def part1():
    with open("input.txt") as f:
        sacks = f.read().splitlines()

    repeated: List[str] = []

    for sack in sacks:
        half1, half2 = get_compartments(sack)
        for item in half1:
            if item in half2:
                repeated.append(item)
                break

    print(sum(get_priority(item) for item in repeated))


def part2():
    with open("input.txt") as f:
        sacks = f.read().splitlines()

    badges: List[str] = []

    for sack1, sack2, sack3 in zip(sacks[0::3], sacks[1::3], sacks[2::3]):
        badges.append(set(sack1).intersection(sack2, sack3).pop())

    print(sum(get_priority(badge) for badge in badges))


def get_priority(item: str) -> int:
    ascii_code = ord(item)

    if 90 >= ascii_code >= 65:
        return ascii_code - 38

    if 122 >= ascii_code >= 97:
        return ascii_code - 96

    raise ValueError(f"Wrong value: {item} with code {ascii_code}")


def get_compartments(rucksack: str) -> Tuple[str, str]:
    size = len(rucksack)

    return rucksack[:size//2], rucksack[-size//2:]


if __name__ == "__main__":
    part1()
    part2()
