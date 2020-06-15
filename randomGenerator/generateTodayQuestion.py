import sys
from random import randrange


def query(lines, number):
    rtn = []
    selected = set()
    for _ in range(number):
        select = 0
        while True:
            select = randrange(len(lines))
            if select not in selected:
                break

        if '](' in lines[select]:
            rtn += [lines[select]]
        else:
            for i in range(select, -1, -1):
                if '](' in lines[i]:
                    break
            rtn += [lines[i]]
            rtn += [lines[select]]
    return rtn


# def main(easy, medium, hard, super):
def main():
    data = None
    with open("randomGenerator/PROBLEMS.md") as file:  # Use file to refer to the file object
        current = 'garbage'
        sums = {
            'easy': [],
            'medium': [],
            'hard': [],
            'super': [],
            'garbage': []
        }
        for line in file:
            if line == '\n':
                continue
            elif '## Easy' in line:
                current = 'easy'
            elif '## Medium' in line:
                current = 'medium'
            elif '## Hard' in line:
                current = 'hard'
            elif '## Super' in line:
                current = 'super'
            else:
                sums[current].append(line)
        data = (
            query(sums['easy'], 1) +
            query(sums['medium'], 1) +
            query(sums['hard'], 1) +
            query(sums['super'], 1)
        )

    with open('Today.md', 'w') as file:  # Use file to refer to the file object
        for line in data:
            file.write(line)


if __name__ == "__main__":
    # if len(sys.argv) != 5:
    #     exit()

    # main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    main()
