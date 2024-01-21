import sys

X = int(sys.stdin.readline())
possible_sticks = [1, 2, 4, 8, 16, 32, 64]
choosen_sticks = [0]
split_length = 64

while True:
    if X in possible_sticks:
        sys.stdout.write(str(1))
        break
    else:
        split_length = split_length // 2
        add_sticks = split_length + sum(choosen_sticks)
        if add_sticks <= X:
            choosen_sticks.append(split_length)
        if sum(choosen_sticks) == X:
            sys.stdout.write(str(len(choosen_sticks) - 1))
            break