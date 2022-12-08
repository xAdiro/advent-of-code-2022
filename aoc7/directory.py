from __future__ import annotations
from typing import Set, List

from file import File


class Directory:
    def __init__(self, name: str, parent: Directory = None) -> None:
        self.name = name
        self.subdirs: Set[Directory] = set()
        self.files: Set[File] = set()
        self.parent = parent

    def add_file(self, file_name: str, file_size: int) -> None:
        self.files.add(File(file_name, file_size))

    def add_directory(self, directory_name: str) -> Directory:
        new_directory = Directory(directory_name, parent=self)
        self.subdirs.add(new_directory)
        return new_directory

    def get_size(self) -> int:
        total_size = 0

        for file in self.files:
            total_size += file.size

        for directory in self.subdirs:
            total_size += directory.get_size()

        return total_size

    def get_all_subdirs(self) -> List[Directory]:
        subdirs: List[Directory] = []

        subdirs.extend(self.subdirs)

        for subdir in self.subdirs:
            subdirs.extend(subdir.get_all_subdirs())

        return subdirs

