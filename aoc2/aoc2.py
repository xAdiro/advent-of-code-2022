# A,X - rock
# B,Y - paper
# C,Z - scissors

VALUES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

BEATS = {
    "X": "C",
    "Y": "A",
    "Z": "B",
    "A": "Z",
    "B": "X",
    "C": "Y"
}

LOSES = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

DRAWS = {
    "X": "A",
    "Y": "B",
    "Z": "C",
    "A": "X",
    "B": "Y",
    "C": "Z"
}


def part1():
    with open("input.txt") as f:
        moves = f.read().splitlines()

    score = 0

    for move in moves:
        their_move = move[0]
        my_move = move[2]

        score += VALUES[my_move]

        if DRAWS[my_move] == their_move:
            score += 3
        elif BEATS[my_move] == their_move:
            score += 6

    print(score)


def part2():
    with open("input.txt") as f:
        moves = f.read().splitlines()

    score = 0

    for move in moves:
        their_move = move[0]
        result = move[2]
        my_move = ""

        match result:
            case "X":
                my_move = BEATS[their_move]
            case "Y":
                my_move = DRAWS[their_move]
                score += 3
            case "Z":
                my_move = LOSES[their_move]
                score += 6

        score += VALUES[my_move]

    print(score)


if __name__ == "__main__":
    part1()
    part2()
