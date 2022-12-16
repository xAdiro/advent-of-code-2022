from sensors_structure import SensorsStructure


def part1():
    sensors_beacons = get_sensors_and_beacons_corrds()

    Y = 2_000_000
    # Y = 10

    sensors_strucutre = SensorsStructure(sensors_beacons, Y)
    print(sensors_strucutre.get_impossible_beacons(Y))


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


def part2():
    sensors_ranges = get_sensors_ranges(get_sensors_and_beacons_corrds())
    percents = range(0, 4_000_000, 40_000)

    # maybe it will be at the end XD
    for x in reversed(range(0, 4_000_000+1)):
        if x in percents: print("done", x)
        for y in reversed(range(0, 4000000+1)):
            if not is_visible(x, y, sensors_ranges):
                print(x*4000000+y)
                return


def get_sensors_ranges(sensors_and_beacons_corrds: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[tuple[int, int, int]]:
    sensors_and_ranges: list[tuple[int, int, int]] = []

    for sensor, beacon in sensors_and_beacons_corrds:
        sensor_x, sensor_y = sensor
        beacons_x, beacon_y = beacon

        sensor_range = abs(sensor_x - beacons_x) + abs(sensor_y - beacon_y)
        # add only potential sensors
        sensors_and_ranges.append((sensor_x, sensor_y, sensor_range))

    return sensors_and_ranges


def is_visible(x: int, y: int, sensors_and_ranges: list[tuple[int, int, int]]) -> bool:
    for sensor_x, sensor_y, sensor_range in sensors_and_ranges:
        distance = abs(x-sensor_x) + abs(y-sensor_y)
        if distance <= sensor_range: return True
    return False


if __name__ == '__main__':
    # part1()
    part2()
