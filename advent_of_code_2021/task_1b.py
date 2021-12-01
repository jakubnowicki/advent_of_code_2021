increase = 0
decrease = 0
previous_sum = []
current_sum = []
line_number = 0

with open("data/task_1.txt") as file:
    while True:
        line = file.readline()

        if not line:
            print(increase)
            break
        line_number += 1

        line = int(line)

        if len(current_sum) >= 3:
            current_sum.pop(0)

        current_sum.append(line)

        if line_number > 3:
            if sum(current_sum) > sum(previous_sum):
                increase += 1

            if sum(current_sum) < sum(current_sum):
                decrease += 1

        previous_sum = current_sum.copy()
