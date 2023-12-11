if __name__ == '__main__':
    with open('input_day11.txt') as file:
        lines = file.read().splitlines()
        w, h = len(lines[0]), len(lines)

        # Double empty rows.
        empty_rows = [i for i in range(h) if all(c == '.' for c in lines[i])]
        h += len(empty_rows)
        for i in range(len(empty_rows)):
            lines.insert(i + empty_rows[i], '.' * w)

        # Double empty columns.
        empty_cols = []
        for x in range(w):
            col = ''
            for y in range(h):
                if lines[y][x] != '.':
                    break
            else:
                empty_cols.append(x)
        w += len(empty_cols)
        for i in range(len(lines)):
            for j in range(len(empty_cols)):
                insert_index = j + empty_cols[j]
                lines[i] = lines[i][:insert_index] + '.' + lines[i][insert_index:]

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
                path_lengths_sum += abs(gb_x - ga_x) + abs(gb_y - ga_y)

        print(f'All pairs shortest path lengths sum: {path_lengths_sum}')
