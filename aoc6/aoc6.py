def part1():
    with open("input.txt") as f:
        message = f.read()

    for i in range(len(message)):
        signal = set(message[i:i+4])
        if len(signal) == 4:
            print(i+4)
            return


def part2():
    with open("input.txt") as f:
        message = f.read()

    for i in range(len(message)):
        signal = set(message[i:i+14])
        if len(signal) == 14:
            print(i+14)
            return


if __name__ == "__main__":
    part1()
    part2()
