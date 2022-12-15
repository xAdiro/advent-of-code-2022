class Cave:
    SAND_SOURCE = (500, 0)

    def __init__(self, rock_paths: list[list[list[int]]]):
        self.__occupied = self.__get_occupied_by_rocks(rock_paths)
        self.__MAX_Y = self.__get_max_y()

    def add_sand(self) -> bool:
        current_x, current_y = self.SAND_SOURCE
        sand_moved = True

        while sand_moved:
            sand_moved = False
            # down
            while (current_x, current_y+1) not in self.__occupied:
                if current_y + 1 >= self.__MAX_Y: break
                current_y += 1
                sand_moved = True

            if current_y + 1 >= self.__MAX_Y: break
            # left diagonally
            if (current_x-1, current_y+1) not in self.__occupied:
                current_x -= 1
                current_y += 1
                sand_moved = True

            # right diagonally
            elif(current_x+1, current_y+1) not in self.__occupied:
                current_x += 1
                current_y += 1
                sand_moved = True
        self.__occupied.add((current_x, current_y))
        return not ((current_x, current_y) == self.SAND_SOURCE)

    def __get_occupied_by_rocks(self, rock_paths: list[list[list[int]]]) -> set[tuple[int, int]]:
        occupied: set[tuple[int, int]] = set()

        for path in rock_paths:
            for point1, point2 in zip(path, path[1:]):
                x1, y1 = point1
                x2, y2 = point2

                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        occupied.add((x1, y))
                elif y1 == y2:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        occupied.add((x, y1))

        return occupied

    def __get_max_y(self) -> int:
        max_y = max(self.__occupied, key=lambda x: x[1])[1]
        return max_y + 2

    def get_occupied(self):
        return self.__occupied

