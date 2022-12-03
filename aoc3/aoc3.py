from typing import Tuple, List


def part1():
    with open("input.txt") as f: print(sum(ascii_code - 38 if 90 >= ascii_code >= 65 else ascii_code - 96 for ascii_code in [ord(item.pop()) for item in [set(half1).intersection(half2) for half1, half2 in [(sack[:len(sack)//2], sack[-len(sack)//2:]) for sack in f.read().splitlines()]]]))


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


if __name__ == "__main__":
    part1()
    part2()
