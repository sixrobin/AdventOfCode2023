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
    return map_data[0], map_data[1], map_data[2]


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

        # Make each map process all seeds.
        for k, v in maps.items():
            result = []
            for s in seeds:
                for dst, src, rl in v:
                    if src <= s < src + rl:
                        result.append(s - src + dst)
                        break
                else:
                    result.append(s)

            seeds = result

        print(min(seeds))
