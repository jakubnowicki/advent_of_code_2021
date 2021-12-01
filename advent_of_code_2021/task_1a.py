increase = 0
decrease = 0
previous_line = 171

with open("data/task_1.txt") as file:
    while True:
        line = file.readline()

        if not line:
            print(increase)
            break

        line = int(line)

        if line > previous_line:
          increase += 1

        if line < previous_line:
          decrease += 1

        previous_line = line
 

