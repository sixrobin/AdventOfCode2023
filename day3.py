if __name__ == '__main__':
    with open('input_day3.txt') as file:
        lines = file.readlines()

        # Convert puzzle input to a 2D array.
        rows = len(lines)
        cols = len(lines[0]) - 1
        arr = [[''] * cols for i in range(rows)]
        for i in range(rows):
            line = lines[i]
            for j in range(cols):
                arr[i][j] = line[j]

        current_number = ''
        part_numbers_sum = 0
        gear_numbers = {}

        for i in range(rows):
            for j in range(cols):
                c = arr[i][j]
                line_end = j == cols - 1

                if c.isdigit():
                    current_number += c
                    if not line_end:
                        continue

                if len(current_number) > 0:
                    adjacent_symbols = ''
                    sx = max(0, i - 1)
                    ex = min(sx + 3, rows)
                    sy = max(0, j - 1 - len(current_number))
                    if line_end and c.isdigit():
                        sy += 1
                    ey = min(sy + len(current_number) + 2, cols)

                    for x in range(sx, ex):
                        for y in range(sy, ey):
                            adjacent_char = arr[x][y]
                            if not adjacent_char.isdigit() and adjacent_char != '.':
                                adjacent_symbols += adjacent_char
                                if adjacent_char == '*':
                                    dict_key = f'{x}/{y}'
                                    if dict_key in gear_numbers:
                                        gear_numbers[dict_key].append(int(current_number))
                                    else:
                                        gear_numbers[dict_key] = [int(current_number)]

                    if adjacent_symbols != '':
                        part_numbers_sum += int(current_number)

                    current_number = ''

        gear_ratios_sum = 0
        for k, v in gear_numbers.items():
            if len(v) == 2:
                gear_ratios_sum += v[0] * v[1]

        print(f'Part numbers sum: {part_numbers_sum}')
        print(f'Gears ratios sum: {gear_ratios_sum}')
