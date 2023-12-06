import re

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

        # Fill stacks.
        for i in range(stack_indices_line - 1, -1, -1):
            line_fill = lines[i].replace(' [', '[')
            line_fill = line_fill.replace('] ', ']')
            line_fill = line_fill.replace('   ', '[.]')
            line_fill = re.sub(' ', '', line_fill)
            for x in range(line_fill.count('[')):
                crate = line_fill[1 + x * 3]
                if crate != '.':
                    stacks[x].append(crate)

        # Process move instructions.
        for i in range(stack_indices_line + 2, len(lines)):
            m = [int(i) for i in lines[i].split() if i.isdigit()]
            buffer = []
            for x in range(m[0]):
                crate = stacks[m[1] - 1].pop()
                buffer.append(crate)
            while buffer:
                stacks[m[2] - 1].append(buffer.pop())

        result = ''
        for s in stacks:
            result += s[-1]
        print(f'Result: {result}')
