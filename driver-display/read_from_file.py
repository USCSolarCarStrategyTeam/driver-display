# generating random inputs
import random

file = open('test_input.txt', 'w')
for i in range(1000):
    type = random.randint(0, 5)

    value = random.randint(0, 99)

    file.writelines(str(type) + ' ' + str(value) + '\n')

file = open('test_input.txt', 'r')
line = file.readline()

while line:
    print(line.strip())
    line = file.readline()
file.close()
