import math


OPERATION = {
    "+": int.__add__,
    "-": int.__sub__,
    "*": int.__mul__,
    "/": lambda a, b: a//b
}

INVERSE_OPERATION = {
    "+": int.__sub__,
    "-": int.__add__,
    "*": lambda a, b: a//b,
    "/": int.__mul__
}


def part1():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    lines = [line.split(": ") for line in lines]
    monkeys = {name: yelling.split(" ") for name, yelling in lines}

    print(get_value(monkeys, "root"))


def part2():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    lines = [line.split(": ") for line in lines]
    monkeys = {name: yelling.split(" ") for name, yelling in lines}

    monkey1, _, monkey2 = monkeys["root"]

    # some monotoneous tendency can be seen sooo

    print(get_inverse_score(monkeys, monkey1, "humn", get_value(monkeys, monkey2)))


def get_value(monkeys: dict[str, list[str]], monkey_name: str) -> int:
    yelling = monkeys[monkey_name]
    if len(yelling) == 1:
        return int(yelling[0])
    else:
        name1, operation, name2 = yelling
        return OPERATION[operation](get_value(monkeys, name1), get_value(monkeys, name2))


def get_inverse_score(monkeys: dict[str, list[str]], root_monkey: str, searched_name: str, input_score: int) -> int:
    if root_monkey == searched_name:
        return input_score  # because humn is in sum

    yelling = monkeys[root_monkey]

    name1, operation, name2 = yelling
    if has_inside(monkeys, name1, searched_name):
        return get_inverse_score(
            monkeys,
            name1,
            searched_name,
            INVERSE_OPERATION[operation](input_score, get_value(monkeys, name2))
        )
    else:
        translated_value = get_value(monkeys, name1)
        if operation == "/":
            # never happens

            return get_inverse_score(
                monkeys,
                name2,
                searched_name,
                1//input_score*translated_value
            )
        elif operation == "-":
            return get_inverse_score(
                monkeys,
                name2,
                searched_name,
                -input_score+translated_value
            )

        return get_inverse_score(
            monkeys,
            name2,
            searched_name,
            INVERSE_OPERATION[operation](input_score, translated_value)
        )


def has_inside(monkeys: dict[str, list[str]], monkey_name: str, searched_name: str) -> bool:
    if monkey_name == searched_name:
        return True

    yelling = monkeys[monkey_name]

    if len(yelling) == 1:
        return False

    monkey1, _, monkey2 = yelling

    return has_inside(monkeys, monkey1, searched_name) or has_inside(monkeys, monkey2, searched_name)


if __name__ == '__main__':
    # part1()
    part2()
