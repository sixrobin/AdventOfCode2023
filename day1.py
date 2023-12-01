import sys

replacements = {'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'}


def first_digit_index(s):
    index = -1
    for i, c in enumerate(line):
        if c.isdigit():
            return i
    return index


def last_digit_index(s):
    index = -1
    for i, c in enumerate(line):
        if c.isdigit():
            index = i
    return index


if __name__ == '__main__':
    with open('input_day1.txt') as file:
        lines = file.readlines()
        result = 0

        for line in lines:
            firstDigitIndex = first_digit_index(line)
            lastDigitIndex = last_digit_index(line)
            firstLetterDigitIndex = sys.maxsize
            lastLetterDigitIndex = -1
            firstLetterDigitNumber = ''
            lastLetterDigitNumber = ''

            for n, d in replacements.items():
                firstIndex = line.find(n)
                if -1 < firstIndex < firstLetterDigitIndex:
                    firstLetterDigitIndex = firstIndex
                    firstLetterDigitNumber = n

                lastIndex = line.rfind(n)
                if lastIndex > -1 and lastIndex > lastLetterDigitIndex:
                    lastLetterDigitIndex = lastIndex
                    lastLetterDigitNumber = n

            # First digit is in letter format: replace it.
            if firstLetterDigitIndex < firstDigitIndex:
                line = line.replace(firstLetterDigitNumber, replacements[firstLetterDigitNumber], 1)

            # Last digit is in letter format: replace it.
            if lastLetterDigitIndex > lastDigitIndex:
                line = replacements[lastLetterDigitNumber].join(line.rsplit(lastLetterDigitNumber, 1))

            line = ''.join(filter(str.isdigit, line))

            length = len(line)
            if length == 0:
                print('Error when parsing a line: no value found!')
                continue
            if length == 1:
                line += line  # Single digit is both the first and the last.
            elif length > 2:
                line = line[0] + line[length - 1]

            result += int(line)

        print(result)
