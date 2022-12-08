from typing import List, Tuple


def part1():
    with open("input.txt") as f:
        trees = f.read().splitlines()

    visible_trees = get_suitable_trees(trees)

    visible_trees_count = sum(sum([int(tree) for tree in tree_row]) for tree_row in visible_trees)
    print(visible_trees_count)


def part2():
    with open("input.txt") as f:
        trees = f.read().splitlines()

    visible_trees = get_suitable_trees(trees)

    max_view = 0
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            if visible_trees[i][j]:
                max_view = max(max_view, calculate_view(trees, i, j))

    print(max_view)


def calculate_view(trees: List[str], i: int, j: int) -> int:
    tree_height = int(trees[i][j])

    left_trees, right_trees, up_trees, down_trees = 0, 0, 0, 0
    for left in reversed(range(0, j)):
        left_trees += 1

        other_tree_height = int(trees[i][left])
        if other_tree_height >= tree_height:
            break

    for right in range(j+1, len(trees[0])):
        right_trees += 1

        other_tree_height = int(trees[i][right])
        if other_tree_height >= tree_height:
            break

    for up in reversed(range(0, i)):
        up_trees += 1

        other_tree_height = int(trees[up][j])
        if other_tree_height >= tree_height:
            break

    for down in range(i+1, len(trees)):
        down_trees += 1

        other_tree_height = int(trees[down][j])
        if other_tree_height >= tree_height:
            break

    return left_trees * right_trees * up_trees * down_trees


def get_suitable_trees(trees: List[str]) -> List[List[bool]]:
    MAX_HEIGHT = 9

    visible_trees_vertically = [[False] * len(trees[0]) for _ in range(len(trees))]
    visible_trees_horizontally = [[False] * len(trees[0]) for _ in range(len(trees))]

    for i in range(1, len(trees) - 1):
        # ->
        tallest = trees[i][0]
        for j in range(1, len(trees[i]) - 1):
            if (current := trees[i][j]) > tallest:
                visible_trees_horizontally[i][j] = True
                tallest = current

            if current == MAX_HEIGHT:
                break

        # <-
        tallest = trees[i][-1]
        for j in reversed(range(1, len(trees[i]) - 1)):
            if visible_trees_horizontally[i][j]:
                break

            if (current := trees[i][j]) > tallest:
                visible_trees_horizontally[i][j] = True
                tallest = current

            if current == MAX_HEIGHT:
                break

    for j in range(1, len(trees[0]) - 1):
        # ↓
        tallest = trees[0][j]
        for i in range(1, len(trees) - 1):
            if (current := trees[i][j]) > tallest:
                visible_trees_vertically[i][j] = True
                tallest = current

            if current == MAX_HEIGHT:
                break

        # ↑
        tallest = trees[-1][j]
        for i in reversed(range(1, len(trees) - 1)):
            if visible_trees_vertically[i][j]:
                break

            if (current := trees[i][j]) > tallest:
                visible_trees_vertically[i][j] = True
                tallest = current

            if current == MAX_HEIGHT:
                break

    visible_trees = [[tree_h | tree_v for tree_h, tree_v in zip(rows, columns)] for rows, columns in
                     zip(visible_trees_horizontally, visible_trees_vertically)]

    visible_trees[0] = [True] * len(visible_trees[0])
    visible_trees[-1] = [True] * len(visible_trees[0])

    for i in range(len(trees[0])):
        visible_trees[i][0] = True
        visible_trees[i][-1] = True

    return visible_trees


if __name__ == "__main__":
    part1()
    part2()

