if __name__ == '__main__':
    with open('input_day2.txt') as file:
        lines = file.readlines()

        horizontal = 0
        depth = 0
        aim = 0

        for line in lines:
            move = line.split()
            number = int(move[1])
            if move[0] == 'forward':
                horizontal += number
                depth += aim * number
            elif move[0] == 'down':
                aim += number
            elif move[0] == 'up':
                aim -= number

        print(horizontal * depth)
