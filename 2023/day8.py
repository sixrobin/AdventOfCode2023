def greatest_common_divider(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    return (a * b) // greatest_common_divider(a, b)


if __name__ == '__main__':
    with open('input_day8.txt') as file:
        lines = file.read().splitlines()
        directions = lines[0]
        paths = []

        network = {}
        for il in range(2, len(lines)):
            pos, dirs = lines[il].split('=')[0].strip(), lines[il].split('=')[1].strip()
            left, right = dirs[1:-1].split(',')
            network[pos] = (left, right.strip())
            if pos[2] == 'A':
                paths.append((pos, 0))

        # Compute each path required steps to get to an end.
        for i in range(len(paths)):
            p, s = paths[i]
            while True:
                d = directions[s % len(directions)]
                p = network[p][0 if d == 'L' else 1]
                s += 1
                paths[i] = (p, s)
                if p[2] == 'Z':
                    break

        # Compute the least common multiple of all paths required steps to get the result.
        full_cycle_steps = least_common_multiple(paths[0][1], paths[1][1])
        for i in range(2, len(paths)):
            full_cycle_steps = least_common_multiple(full_cycle_steps, paths[i][1])

        print(full_cycle_steps)
