def part1():
    with open("input.txt") as f:
        elves_calories = f.read().split("\n\n")

    elves_calories = [elve_calories.split("\n") for elve_calories in elves_calories]
    elves_calories[-1].pop()  # remove last blank string
    print(sum(list(max([tuple(map(int, x)) for x in elves_calories], key=lambda x: sum(x)))))


def part2():
    with open("input.txt") as f:
        elves_calories = f.read().split("\n\n")

    elves_calories = [elve_calories.split("\n") for elve_calories in elves_calories]
    elves_calories[-1].pop()  # remove last blank string
    elves_calories = [tuple(map(int, x)) for x in elves_calories]
    print(sum([sum(x) for x in sorted(elves_calories, key=lambda x: sum(x))[-3:]]))


if __name__ == "__main__":
    part1()
    part2()
