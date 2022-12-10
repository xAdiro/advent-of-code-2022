from __future__ import annotations
from typing import Tuple

from head import Head


class Tail:
    def __init__(self) -> None:
        self.__x = 0
        self.__y = 0

    def catch_up(self, head: Head | Tail) -> None:
        distance_x, distance_y = self.__get_distance(head)

        # . . . . .
        # . T T T .
        # . T H T .
        # . T T T .
        # . . . . .
        if abs(distance_x) <= 1 and abs(distance_y) <= 1: return

        # . . . . .
        # . . . . .
        # T . H . T
        # . . . . .
        # . . . . .
        if abs(distance_x) >= 2 and abs(distance_y) == 0:
            self.__x += (1 if distance_x > 0 else -1)
            return

        # . . T . .
        # . . . . .
        # . . H . .
        # . . . . .
        # . . T . .
        if abs(distance_y) >= 2 and abs(distance_x) == 0:
            self.__y += (1 if distance_y > 0 else -1)
            return

        # . T . T .
        # T . . . T
        # . . H . .
        # T . . . T
        # . T . T .
        self.__x += (1 if distance_x > 0 else -1)
        self.__y += (1 if distance_y > 0 else -1)

    def get_position(self) -> Tuple[int, int]:
        return self.__x, self.__y

    def __get_distance(self, head: Head | Tail) -> Tuple[int, int]:
        head_x, head_y = head.get_position()

        return head_x - self.__x, head_y - self.__y
