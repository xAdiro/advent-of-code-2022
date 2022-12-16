class SensorsStructure:
    def __init__(self, sensors_and_beacons_coords: list[tuple[tuple[int, int], tuple[int, int]]], y: int):
        self.__y = y
        self.__sensors_and_beacons_coords = sensors_and_beacons_coords

    def get_impossible_beacons(self, y: int) -> int:
        x_intervals = []

        for sensor_x, sensor_y, sensor_range in self.__get_useful_sensors_and_ranges(self.__sensors_and_beacons_coords):
            x_range = sensor_range - abs(sensor_y-y)
            x_intervals.append((sensor_x - x_range, sensor_x + x_range))

        x_intervals = self.__minimal_ranges(x_intervals)

        result = 0
        for interval in x_intervals:
            result += interval[1] - interval[0]

        return result - self.get_existing_beacons_on_line(x_intervals) + 1

    def get_existing_beacons_on_line(self, x_intervals: list[tuple[int, int]]) -> int:
        result = 0
        beacons = {beacon for _, beacon in self.__sensors_and_beacons_coords}

        for beacon in beacons:
            beacon_x, beacon_y = beacon

            for interval in x_intervals:
                if beacon_y == self.__y and interval[0] <= beacon_x <= interval[1]:
                    result += 1
                    break

        return result

    def __minimal_ranges(self, intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))  # most left x if tie then bigger
        reduced_intervals = []

        parent = intervals[0]

        for interval in intervals:
            # print(reduced_intervals)
            # parent:   ..<----->..s
            # interval: ....<->....
            if parent[0] <= interval[0] and interval[1] <= parent[1]:
                continue
            # parent   ..<----->......
            # interval .....<----->...
            elif interval[0] <= parent[1] <= interval[1]:
                parent = (parent[0], interval[1])
                continue

            # parent   ..<---->..
            # interval ...........<--->
            reduced_intervals.append(parent)
            parent = interval

        reduced_intervals.append(parent)

        return reduced_intervals

    def __get_useful_sensors_and_ranges(self, sensors_and_beacons_coords: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[[tuple[int, int, int]]]:
        sensors_and_ranges: list[tuple[int, int, int]] = []

        for sensor, beacon in sensors_and_beacons_coords:
            sensor_x, sensor_y = sensor
            beacons_x, beacon_y = beacon

            sensor_range = abs(sensor_x - beacons_x) + abs(sensor_y - beacon_y)
            # add only potential sensors
            if abs(self.__y - sensor_y) <= sensor_range:
                sensors_and_ranges.append((sensor_x, sensor_y, sensor_range))

        return sensors_and_ranges
