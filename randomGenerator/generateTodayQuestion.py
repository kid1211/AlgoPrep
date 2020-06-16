import sys
from random import randrange
import subprocess

EASY_MED_HARD_SUPER = (1, 1, 1, 1)
executable = [
    'git status',
    'main',
    'git add .',
    'git commit -a -m \"Generated Question\"',
    'git push',
    'open https://github.com/kid1211/AlgoPrep#readme'
]


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
    with open("PROBLEMS.md") as file:  # Use file to refer to the file object
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

        easy, med, hard, super = EASY_MED_HARD_SUPER
        data = (
            query(sums['easy'], easy) +
            query(sums['medium'], med) +
            query(sums['hard'], hard) +
            query(sums['super'], super)
        )

    with open('README.md', 'w') as file:  # Use file to refer to the file object
        file.write('# Today\'s Problem\n\n')
        for line in data:
            file.write(line)


if __name__ == "__main__":
    # main()
    for line in executable:
        process = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE)
        process.wait()
        if (process.returncode != 0):
            sys.exit()
        if 'git status' in line:
            status = process.stdout.read()
            print(status)
            if status != b'':
                sys.exit()
        elif 'main' in line:
            main()
