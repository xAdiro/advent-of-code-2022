from typing import List, Tuple


def part1():
    # move <amount> from <stack1> to <stack2>
    moves = get_moves()
    stacks = get_stacks()

    for move in moves:
        amount = move[0]
        stack1 = move[1]-1
        stack2 = move[2]-1
        for _ in range(amount):
            stacks[stack2].append(stacks[stack1].pop())

    print("".join([stack[-1] for stack in stacks]))


def part2():
    # move <amount> from <stack1> to <stack2>
    moves = get_moves()
    stacks = get_stacks()

    for move in moves:
        amount = move[0]
        stack1 = move[1] - 1
        stack2 = move[2] - 1

        stacks[stack2].extend(stacks[stack1][-amount:])
        del stacks[stack1][-amount:]

    print("".join([stack[-1] for stack in stacks]))


def get_stacks() -> List[List[str]]:
    with open('input.txt') as f:
        lines = f.read().replace("", "").replace("", "").replace(" ", " ").splitlines()[:8]

    stacks: List[List[str]] = []
    for i in range(1, 35, 4):

        stack: List[str] = []
        for h in range(len(lines)):
            value = lines[h][i]
            if value != " ":
                stack.append(value)
        stack.reverse()
        stacks.append(stack)

    return stacks


def get_moves() -> List[Tuple[int]]:
    with open('input.txt') as f:
        lines = [tuple(map(int, line.split())) for line in f.read().replace("move ", "").replace("from ", "").replace(" to ", " ").splitlines()[10:]]

    return lines


if __name__ == "__main__":
    part1()
    part2()
