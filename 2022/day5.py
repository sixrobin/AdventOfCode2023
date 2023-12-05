if __name__ == '__main__':
    with open('input_day5.txt') as file:
        lines = file.read().splitlines()
        stacks = []

        stack_indices_line = 0
        for i in range(len(lines)):
            if lines[i].startswith(' 1'):
                stack_indices_line = i
                stacks = [[] for x in range(int(lines[i].strip()[-1]))]
                break

        for i in range(stack_indices_line - 1, -1, -1):
            line_fill = lines[i].replace(' [', '[').replace('] ', ']').replace('   ', '[.]')
            for x in range(line_fill.count('[')):
                crate = line_fill[1 + x * 3]
                if crate != '.':
                    stacks[x].append(crate)

        for i in range(stack_indices_line + 2, len(lines)):
            # TODO: Process move.
            print(lines[i])
