def part1():
    with open("input.txt") as f:
        elves_calories = f.read().split("\n\n")

    elves_calories = [elve_calories.split("\n") for elve_calories in elves_calories]
    elves_calories[-1].pop()  # remove last blank string
    print(sum(list(max([tuple(map(int, x)) for x in elves_calories], key=lambda x: sum(x)))))


if __name__ == "__main__":
    part1()
