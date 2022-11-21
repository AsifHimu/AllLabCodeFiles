fhand = open("./input.txt")
tsk = {}
for line in fhand:
    element = line.split(',')
    tsk[element[0]] = {}
    tsk[element[0]]['Activity'] = 