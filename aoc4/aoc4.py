def part1():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    elf_pairs = [line.split(",") for line in lines]
    for i in range(len(elf_pairs)):
        for j in range(2):
            elf_pairs[i][j] = [int(edge) for edge in elf_pairs[i][j].split("-")]

    fully_contained = 0

    for elf_pair in elf_pairs:
        range1 = elf_pair[0]
        range2 = elf_pair[1]

        if (range2[0] <= range1[0] and range1[1] <= range2[1]) or (range1[0] <= range2[0] and range2[1] <= range1[1]):
            fully_contained += 1

    print(fully_contained)


def part2():
    with open('input.txt') as f:
        lines = f.read().splitlines()
    elf_pairs = [line.split(",") for line in lines]
    for i in range(len(elf_pairs)):
        for j in range(2):
            elf_pairs[i][j] = [int(edge) for edge in elf_pairs[i][j].split("-")]

    fully_contained = 0

    for elf_pair in elf_pairs:
        range1 = elf_pair[0]
        range2 = elf_pair[1]

        if range2[0] <= range1[0] <= range2[1] or range2[0] <= range1[1] <= range2[1]\
                or range1[0] <= range2[0] <= range1[1] or range1[0] <= range2[1] <= range1[1]:
            fully_contained += 1

    print(fully_contained)


if __name__ == "__main__":
    part1()
    part2()