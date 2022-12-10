from head import Head
from tail import Tail


def part1():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    moves = [(str(direction), int(steps)) for direction, steps in [line.split(" ") for line in lines]]

    visited = set()
    head = Head()
    tail = Tail()

    for direction, steps in moves:
        for _ in range(steps):
            head.move(direction)
            tail.catch_up(head)

            visited.add(tail.get_position())

    print(len(visited))


def part2():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    moves = [(str(direction), int(steps)) for direction, steps in [line.split(" ") for line in lines]]

    visited = set()
    head = Head()
    tails = [Tail() for _ in range(9)]

    for direction, steps in moves:
        for _ in range(steps):
            head.move(direction)
            tails[0].catch_up(head)

            for tail1, tail2 in zip(tails[:-1], tails[1:]):
                tail2.catch_up(tail1)

            visited.add(tails[-1].get_position())

    print(len(visited))


if __name__ == '__main__':
    part1()
    part2()
