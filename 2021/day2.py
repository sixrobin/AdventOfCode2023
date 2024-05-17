if __name__ == '__main__':
    with open('input_day2.txt') as file:
        lines = file.readlines()

        horizontal = 0
        depth = 0

        for line in lines:
            move = line.split()
            if move[0] == 'forward':
                horizontal += int(move[1])
            elif move[0] == 'down':
                depth += int(move[1])
            elif move[0] == 'up':
                depth -= int(move[1])

        print(f'Part 1: {horizontal * depth}')