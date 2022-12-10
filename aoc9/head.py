from typing import Tuple


class Head:
    def __init__(self) -> None:
        self.__x = 0
        self.__y = 0

    def get_position(self) -> Tuple[int, int]:
        return self.__x, self.__y

    def move(self, direction: str) -> None:
        match direction:
            case 'R':
                self.__x += 1
            case 'L':
                self.__x -= 1
            case 'U':
                self.__y += 1
            case 'D':
                self.__y -= 1
