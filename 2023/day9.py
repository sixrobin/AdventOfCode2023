if __name__ == '__main__':
    with open('input_day9.txt') as file:
        lines = file.read().splitlines()
        p1_result, p2_result = 0, 0

        for line in lines:
            seqs = [[int(x) for x in line.split()]]

            while not all(x == 0 for x in seqs[-1]):
                next_seq = []
                for i in range(len(seqs[-1]) - 1):
                    next_seq.append(seqs[-1][i + 1] - seqs[-1][i])
                seqs.append(next_seq)

            for i in range(len(seqs) - 1, 0, -1):
                seqs[i - 1].append(seqs[i][-1] + seqs[i - 1][-1])
                seqs[i - 1].insert(0, seqs[i - 1][0] - seqs[i][0])

            p1_result += seqs[0][-1]
            p2_result += seqs[0][0]

        print(f'Part 1: {p1_result}')
        print(f'Part 2: {p2_result}')
