from sensors_structure import SensorsStructure
from sensors_structure2 import SensorsStructure2


def part1():
    sensors_beacons = get_sensors_and_beacons_corrds()

    Y = 2_000_000
    # Y = 10

    sensors_strucutre = SensorsStructure(sensors_beacons, Y)
    print(sensors_strucutre.get_impossible_beacons(Y))


def part2():
    sensors_beacons = get_sensors_and_beacons_corrds()
    searched_y = None

    for y in range(4_000_000+1):
        sensors_structure = SensorsStructure2(sensors_beacons, y)
        if sensors_structure.get_impossible_beacons(y) <= 4_000_000:
            searched_y = y
            break

    searched_x = None
    sensors_structure = SensorsStructure2(sensors_beacons, searched_y).get_useful_sensors_and_ranges(sensors_beacons)

    get_sensors_and_beacons_corrds()
    for x in range(4_000_000+1):
        if not is_visible(x, searched_y, sensors_structure):
            searched_x = x
            break

    print(searched_x * 4000000 + searched_y)


def get_sensors_and_beacons_corrds() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    with open('input.txt') as f:
        lines = f.read().splitlines()
    coord_strings = [
        line.removeprefix("Sensor at x=")
        .replace(": closest beacon is at", "")
        .replace("x=", "")
        .replace("y=", "")
        .replace(", ", " ")
        .split(" ")
        for line in lines]

    sensors_beacons = [
        (
            (int(sensor_beacon[0]), int(sensor_beacon[1])),
            (int(sensor_beacon[2]), int(sensor_beacon[3]))
        )
        for sensor_beacon in coord_strings]

    return sensors_beacons


def is_visible(x: int, y: int, sensors_and_ranges: list[tuple[int, int, int]]) -> bool:
    for sensor_x, sensor_y, sensor_range in sensors_and_ranges:
        distance = abs(x-sensor_x) + abs(y-sensor_y)
        if distance <= sensor_range: return True
    return False


if __name__ == '__main__':
    part1()
    part2()
