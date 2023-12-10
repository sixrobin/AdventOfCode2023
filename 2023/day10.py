valid_incoming_directions = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE'}
cardinal_to_direction = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}


def rotate(dx, dy):
    if dx == -1:
        return 0, 1
    elif dx == 1:
        return 0, -1
    elif dy == -1:
        return -1, 0
    else:
        return 1, 0


def try_move(px, py, dx, dy):
    nx, ny = px + dx, py + dy
    if nx < 0 or nx >= w or ny < 0 or ny >= h:
        return px, py, dx, dy

    n = lines[ny][nx]
    if n == 'S':
        return nx, ny, 0, 0
    elif n == '.':
        return px, py, 0, 0

    valid_dir = valid_incoming_directions[n]

    if dx == 1 and 'W' in valid_dir:
        ndx, ndy = cardinal_to_direction[valid_dir.replace('W', '')]
        return nx, ny, ndx, ndy
    elif dx == -1 and 'E' in valid_dir:
        ndx, ndy = cardinal_to_direction[valid_dir.replace('E', '')]
        return nx, ny, ndx, ndy
    elif dy == 1 and 'N' in valid_dir:
        ndx, ndy = cardinal_to_direction[valid_dir.replace('N', '')]
        return nx, ny, ndx, ndy
    elif dy == -1 and 'S' in valid_dir:
        ndx, ndy = cardinal_to_direction[valid_dir.replace('S', '')]
        return nx, ny, ndx, ndy

    return px, py, dx, dy


def point_left_to_seg(ax, ay, bx, by, px, py):
    factor = (by - ay) * (px - ax) - (py - ay) * (bx - ax)
    if factor > 0:
        return 1
    elif factor < 0:
        return -1
    else:
        return 0


def winding_number(polygon, pt):
    wn = 0
    ptx, pty = pt[0], pt[1]

    for i in range(len(polygon) - 1):
        if polygon[i][0] <= ptx:
            if polygon[i + 1][0] > ptx:
                if point_left_to_seg(polygon[i][0], polygon[i][1], polygon[i + 1][0], polygon[i + 1][1], ptx, pty) > 0:
                    wn += 1
        else:
            if polygon[i + 1][0] <= ptx:
                if point_left_to_seg(polygon[i][0], polygon[i][1], polygon[i + 1][0], polygon[i + 1][1], ptx, pty) < 0:
                    wn -= 1

    return wn


if __name__ == '__main__':
    with open('input_day10.txt') as file:
        lines = file.read().splitlines()
        w, h = len(lines[0]), len(lines)

        # Find loop start coordinates.
        sx, sy = -1, -1
        for y in range(h):
            for x in range(w):
                if lines[y][x] == 'S':
                    sx, sy = x, y
                    break
            if sx != -1 and sy != -1:
                break

    pos_x, pos_y = sx, sy
    dir_x, dir_y = 0, -1
    path = []

    while True:
        new_x, new_y, new_dx, new_dy = try_move(pos_x, pos_y, dir_x, dir_y)
        if new_x == pos_x and new_y == pos_y:
            new_dx, new_dy = rotate(dir_x, dir_y)
        else:
            path.append((pos_x, pos_y))
            pos_x, pos_y = new_x, new_y
            if lines[pos_y][pos_x] == 'S':
                break

        dir_x, dir_y = new_dx, new_dy

    pts_inside_loop = 0
    for y in range(h):
        for x in range(w):
            if (x, y) not in path and winding_number(path, (x, y)) != 0:
                pts_inside_loop += 1

    furthest_point_index = len(path) // 2
    print(f'Path traced with {len(path)} points (farthest index: {furthest_point_index}).')
    print(f'{pts_inside_loop} points are nested inside the path.')
