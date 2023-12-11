if __name__ == '__main__':
    with open('input_day11.txt') as file:
        lines = file.read().splitlines()
        w, h = len(lines[0]), len(lines)

        empty_rows = [i for i in range(h) if all(c == '.' for c in lines[i])]

        empty_cols = []
        for x in range(w):
            col = ''
            for y in range(h):
                if lines[y][x] != '.':
                    break
            else:
                empty_cols.append(x)

        galaxies = []
        for x in range(w):
            for y in range(h):
                if lines[y][x] == '#':
                    galaxies.append((x, y))

        path_lengths_sum = 0
        for ga in range(len(galaxies)):
            for gb in range(ga + 1, len(galaxies)):
                ga_x, ga_y = galaxies[ga]
                gb_x, gb_y = galaxies[gb]
                if ga_x > gb_x:
                    ga_x, gb_x = gb_x, ga_x
                if ga_y > gb_y:
                    ga_y, gb_y = gb_y, ga_y
                for x in range(ga_x, gb_x):
                    path_lengths_sum += 1 if x not in empty_cols else 1000000
                for y in range(ga_y, gb_y):
                    path_lengths_sum += 1 if y not in empty_rows else 1000000

        print(f'All pairs shortest path lengths sum: {path_lengths_sum}')
