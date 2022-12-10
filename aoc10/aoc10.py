def part1():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    commands = [line.split(" ") for line in lines]

    cycle = 0
    x_register = 1
    signal_strength_sum = 0

    for command in commands:
        cycles_passed = 0
        finish_command = False

        while not finish_command:
            cycle += 1
            cycles_passed += 1
            match command[0]:
                case "noop":
                    finish_command = True
                case "addx":
                    if cycles_passed == 2:
                        x_register += int(command[1])
                        finish_command = True

            if (cycle - 20) % 40 == 0:
                signal_strength_sum += cycle * x_register


def part2():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    commands = [line.split(" ") for line in lines]

    screen = list(' ' * 300)  # lazy

    cycle = 1
    x_register = 1

    for command in commands:
        cycles_passed = 0
        finish_command = False

        while not finish_command:
            position = (cycle - 1) % 40
            if abs(position - x_register) <= 1:
                screen[cycle-1] = "#"

            cycles_passed += 1
            match command[0]:
                case "noop":
                    finish_command = True
                case "addx":
                    if cycles_passed == 2:
                        x_register += int(command[1])
                        finish_command = True

            cycle += 1

    draw_screen(screen)


def draw_screen(screen: list[str]):
    print("\n".join("".join(screen[x:x+40]) for x in range(0, len(screen), 40)))


if __name__ == '__main__':
    part1()
    part2()
