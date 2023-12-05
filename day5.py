import sys


def parse_seeds(seeds_lines):
    seeds_data = [int(x) for x in seeds_lines.split(': ')[1].split()]

    return seeds_data  # Part 1.

    # Part 2. TODO: Technically works, but does take too long to compute.
    seeds_range_data = []
    for i in range(len(seeds_data) // 2):
        for x in range(seeds_data[i * 2 + 1]):
            seeds_range_data.append(seeds_data[i * 2] + x)

    return seeds_range_data


def parse_map(map_line):
    map_data = [int(x) for x in map_line.split(' ')]
    src_min, src_max = map_data[1], map_data[1] + map_data[2] - 1
    dst_min, dst_max = map_data[0], map_data[0] + map_data[2] - 1
    return [src_min, src_max, dst_min, dst_max]


if __name__ == '__main__':
    with open('input_day5.txt') as file:
        lines = file.read().splitlines()
        seeds = parse_seeds(lines[0])
        maps = {}
        last_map_key = ''
        lowest_location = sys.maxsize

        # Parse maps.
        for line in lines:
            if line == '':
                continue
            if 'map' in line:
                last_map_key = line.split(' ')[0]
                maps[last_map_key] = []
            elif last_map_key != '':
                maps[last_map_key].append(parse_map(line))

        # Process each seed through all maps.
        for s in seeds:
            result = s
            for k, v in maps.items():
                for m in v:
                    if m[0] <= result <= m[1]:
                        result = result + m[2] - m[0]
                        break

            lowest_location = min(lowest_location, result)

        print(f'Lowest location: {lowest_location}')
