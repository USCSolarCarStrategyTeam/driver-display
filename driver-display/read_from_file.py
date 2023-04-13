
file = open('test_input.txt', 'r')
line = file.readline()

while line:
    print(line)
    line = file.readline()
file.close()
