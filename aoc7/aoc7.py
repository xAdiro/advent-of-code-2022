from typing import List, Tuple

from directory import Directory


def part1():
    top_dir = get_filesystem(*get_commands_and_outputs())
    dirs = [top_dir]
    dirs.extend(top_dir.get_all_subdirs())

    print(sum(directory.get_size() for directory in dirs if directory.get_size() <= 100000))


def part2():
    top_dir = get_filesystem(*get_commands_and_outputs())
    dirs = [top_dir]
    dirs.extend(top_dir.get_all_subdirs())

    total_space = 70000000
    currently_taken_space = top_dir.get_size()
    needed_space = 30000000
    space_to_remove = needed_space - (total_space - currently_taken_space)
    print(min([directory for directory in dirs if directory.get_size() >= space_to_remove], key=lambda x: x.get_size()).get_size())


def get_commands_and_outputs() -> Tuple[List[str], List[List[str]]]:
    with open("input.txt") as f:
        lines = f.read().splitlines()

    commands = [line.removeprefix("$ ") for line in lines if line.startswith("$")]
    outputs = []

    single_output = []
    for line in reversed(lines):
        if not line.startswith("$"):
            single_output.append(line)
        else:
            single_output.reverse()
            outputs.append(single_output)
            single_output = []
    outputs.reverse()

    return commands, outputs


def get_filesystem(commands: List[str], outputs: List[List[str]]) -> Directory:
    top_dir = Directory("/")
    current_dir = top_dir
    for command, output in zip(commands[1:], outputs[1:]):
        match command[:2]:
            case "ls":
                execute_ls(current_dir, output)
            case "cd":
                current_dir = execute_cd(current_dir, accesed_dir_name=command[3:])

    return top_dir


def execute_ls(current_dir: Directory, ls_output: List[str]):
    for item in ls_output:
        prefix, name = item.split(" ")
        if prefix == "dir":
            current_dir.add_directory(name)
        else:
            current_dir.add_file(name, int(prefix))


def execute_cd(current_dir: Directory, accesed_dir_name: str) -> Directory:
    if accesed_dir_name == "..":
        return current_dir.parent

    return current_dir.add_directory(accesed_dir_name)


if __name__ == "__main__":
    part1()
    part2()
