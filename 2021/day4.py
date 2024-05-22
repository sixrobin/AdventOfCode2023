if __name__ == '__main__':
    with open('input_day4.txt') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')

        # Parse numbers.
        numbers = list(map(int, lines[0].split(',')))

        boards = []

        # Parse boards.
        current_board = []
        for i in range(2, len(lines)):
            if lines[i].strip():
                line_numbers = []
                for n in lines[i].split():
                    line_numbers.append([int(n), 0])
                current_board.append(line_numbers)
            if not lines[i].strip() or i == len(lines) - 1:
                boards.append(current_board)
                current_board = []
                continue

        winning_boards_order = []
        winning_number = -1
        current_number = -1

        for n in numbers:
            current_number = n

            # Mark number.
            for b in range(len(boards)):
                if b in winning_boards_order:
                    continue

                board = boards[b]
                for bx in range(len(board)):
                    for by in range(len(board[bx])):
                        if board[bx][by][0] == n:
                            board[bx][by][1] = 1

            # Bingo check.
            for b in range(len(boards)):
                if b in winning_boards_order:
                    continue

                board = boards[b]

                bingo_sum = 0
                for x in range(5):
                    bingo_sum = 0
                    for y in range(5):
                        state = board[x][y][1]
                        if state == 0:
                            break
                        bingo_sum += 1
                    if bingo_sum == 5:
                        break

                if bingo_sum < 5:
                    bingo_sum = 0
                    for x in range(5):
                        bingo_sum = 0
                        for y in range(5):
                            state = board[y][x][1]
                            if state == 0:
                                break
                            bingo_sum += 1
                        if bingo_sum == 5:
                            break

                if bingo_sum == 5:
                    winning_boards_order.append(b)
                    if len(winning_boards_order) == 1:
                        winning_number = current_number

            if len(winning_boards_order) == len(boards):
                break

        # Unmarked numbers sum.
        winning_board = boards[winning_boards_order[0]]
        winning_board_unmarked_numbers_sum = 0
        for x in range(5):
            for y in range(5):
                if winning_board[x][y][1] == 0:
                    winning_board_unmarked_numbers_sum += winning_board[x][y][0]

        last_board = boards[winning_boards_order[len(winning_boards_order) - 1]]
        last_board_unmarked_numbers_sum = 0
        for x in range(5):
            for y in range(5):
                if last_board[x][y][1] == 0:
                    last_board_unmarked_numbers_sum += last_board[x][y][0]

        print(f'Winning number: {winning_number}')
        print(f'Last number: {current_number}')
        print(f'Winning board unmarked numbers sum: {winning_board_unmarked_numbers_sum}')
        print(f'Last board unmarked numbers sum: {last_board_unmarked_numbers_sum}')
        print(f'Winning board score: {winning_number * winning_board_unmarked_numbers_sum}')
        print(f'Last board score: {current_number * last_board_unmarked_numbers_sum}')
