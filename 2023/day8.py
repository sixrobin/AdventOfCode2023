def direction_to_index(d):
    if d == 'L':
        return 0
    return 1


if __name__ == '__main__':
    with open('input_day8.txt') as file:
        lines = file.read().splitlines()

        directions = lines[0]

        network = {}
        for il in range(2, len(lines)):
            pos, dirs = lines[il].split('=')[0].strip(), lines[il].split('=')[1].strip()
            dirs = dirs[1:len(dirs) - 1].split(',')
            network[pos] = (dirs[0], dirs[1].strip())

        end_reached = False
        steps = 0
        current_pos = 'AAA'
        while not end_reached:
            direction = directions[steps % len(directions)]
            current_pos = network[current_pos][direction_to_index(direction)]
            steps += 1

            if current_pos == 'ZZZ':
                print(f'{steps} steps')
                end_reached = True
