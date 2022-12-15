from cave import Cave
from cave2 import Cave as Cave2


def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    rock_paths = [[[int(coord) for coord in xy.split(',')] for xy in line.split(" -> ")] for line in lines]

    cave = Cave(rock_paths)
    sand_added = 0
    while cave.add_sand():
        sand_added += 1

    print(sand_added)


def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    rock_paths = [[[int(coord) for coord in xy.split(',')] for xy in line.split(" -> ")] for line in lines]

    cave = Cave2(rock_paths)

    sand_added = 1
    while cave.add_sand():
        sand_added += 1
    print(sand_added)


if __name__ == '__main__':
    # part1()
    part2()
