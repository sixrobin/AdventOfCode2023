def parse_seeds(seeds_lines):
    seeds_data = [int(x) for x in seeds_lines.split(': ')[1].split()]
    seeds_range_data = []
    for i in range(0, len(seeds_data), 2):
        seeds_range_data.append((seeds_data[i], seeds_data[i] + seeds_data[i + 1]))
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
            while seeds:
                sa, sb = seeds.pop()
                for dst, src, rl in v:
                    intersect_start, intersect_end = max(sa, src), min(sb, src + rl)
                    if intersect_start < intersect_end:  # Intersection between ranges.
                        result.append((intersect_start - src + dst, intersect_end - src + dst))  # Shift using map.
                        if intersect_start > sa:
                            seeds.append((sa, intersect_start))  # Left part still need to be computed.
                        if intersect_end < sb:
                            seeds.append((intersect_end, sb))  # Right part still need to be computed.
                        break
                else:
                    result.append((sa, sb))  # No intersection with any range, no remapping for next map.

            seeds = result

        print(min(result)[0])
