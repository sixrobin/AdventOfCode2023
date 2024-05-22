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

        winning_board_index = -1
        current_number = -1

        for n in numbers:
            current_number = n

            # Mark number.
            for b in range(len(boards)):
                board = boards[b]
                for bx in range(len(board)):
                    for by in range(len(board[bx])):
                        if board[bx][by][0] == n:
                            board[bx][by][1] = 1

            # Bingo check.
            for b in range(len(boards)):
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
                    winning_board_index = b
                    break

            if winning_board_index > -1:
                break

        # Unmarked numbers sum.
        winning_board = boards[winning_board_index]
        unmarked_numbers_sum = 0
        for x in range(5):
            for y in range(5):
                if winning_board[x][y][1] == 0:
                    unmarked_numbers_sum += winning_board[x][y][0]

        print(f'Winning board index: {winning_board_index}')
        print(f'Winning number: {current_number}')
        print(f'Unmarked numbers sum: {unmarked_numbers_sum}')
        print(f'Winning board score: {current_number * unmarked_numbers_sum}')
