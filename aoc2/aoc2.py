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
    "Z": "B"
}

DRAWS = {
    "X": "A",
    "Y": "B",
    "Z": "C"
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


if __name__ == "__main__":
    part1()
