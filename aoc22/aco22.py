def part1():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    input_separator = None
    for i, line in enumerate(lines):
        if line == "": input_separator = i

    board_str = lines[:input_separator]
    max_row_len = len(max(board_str, key=len))
    board_str = [f"{line: <{max_row_len}}" for line in board_str]

    steps_str = "".join(lines[input_separator + 1:])
    steps_str = steps_str.replace("L", " L ").replace("R", " R ").split(" ")

    # print("\n".join(board_str))
    # print("\n".join(steps_str))

    start = [None, 0]
    for x, field in enumerate(board_str[start[1]]):
        if field == ".": start[0] = x
    print(start)
    direction = 0

    for step in steps_str:
        if step == "L":
            direction -= 1
            direction %= 4
            continue
        elif step == "R":
            direction += 1
            direction %= 4
            continue

        for _ in range(int(step)):
            start = next_pos(board_str, start, direction)

    col, row = start
    col += 1
    row += 1
    print(f"{row = }, {col = }, {direction = }")
    print(1_000*row + 4*col + direction)


# 0 1 2 3 > v < ^
def next_pos(board_str: list[str], start: tuple[int, int], direction: int) -> tuple[int, int]:
    x, y = start
    while True:
        match direction:
            case 0:
                x += 1
            case 2:
                x -= 1
            case 1:
                y += 1
            case 3:
                y -= 1
        if y < 0 or y >= len(board_str):
            y %= len(board_str)
        elif x < 0 or x >= len(board_str[y]): x %= len(board_str[y])

        if board_str[y][x] == ".":
            return x, y
        elif board_str[y][x] == "#":
            return start


if __name__ == '__main__':
    part1()
