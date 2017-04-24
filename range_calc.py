# range_calc.py
# author: Eric Hayes - eshayes@princeton.edu
# April 2017

# calculate range of each point values in CSV

import stdio

numPoints = 13
numVals = 6
padding = 2

rangeVals = [None] * numPoints * numVals

# skip first 5 lines
s = stdio.readLine()
s = stdio.readLine()
s = stdio.readLine()
s = stdio.readLine()
s = stdio.readLine()

while stdio.isEmpty() == False:

    s = stdio.readLine()

    valList = s.split(' ')
    count = 5
    i = 0
    index = 0

    while count < (padding + numPoints * numVals):

        if i == 3:
            count = count + 3
            i = 0
        else:
            value = float(valList[count])

            if value != -100000:
                if rangeVals[index] is None:
                    rangeVals[index] = value
                    rangeVals[index + 1] = value
                else:
                    if value < rangeVals[index]:
                        rangeVals[index] = value
                    if value > rangeVals[index + 1]:
                        rangeVals[index + 1] = value
            count = count + 1
            i = i + 1
            index = index + 2


# output values: x min, x max, y min, y max, z min, z max repeated for
# each of the tracked objects

# write out all values
for val in rangeVals:
    stdio.write(val)
    stdio.write(' ')
stdio.writeln()
