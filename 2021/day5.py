GRID_SIZE = 1000

if __name__ == '__main__':
    with open('input_day5.txt') as file:
        lines = file.readlines()

        # Parse segments.
        segments = []
        for line in lines:
            points = line.split('->')
            x = points[0].split(',')
            y = points[1].split(',')
            segments.append((int(x[0]), int(x[1]), int(y[0]), int(y[1])))

        diagram = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

        for segment in segments:
            x1, y1, x2, y2 = segment[0], segment[1], segment[2], segment[3]
            dx = 1 if x1 < x2 else -1 if x1 > x2 else 0
            dy = 1 if y1 < y2 else -1 if y1 > y2 else 0
            lx = abs(x1 - x2) + 1
            ly = abs(y1 - y2) + 1

            for i in range(max(lx, ly)):
                x = x1 + i * dx
                y = y1 + i * dy
                diagram[y][x] += 1

        overlaps = 0
        for dx in diagram:
            for d in dx:
                if d > 1:
                    overlaps += 1

        print(f'{overlaps} overlaps')
