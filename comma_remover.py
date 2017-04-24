# comma_remover.py
# author: Eric Hayes - eshayes@princeton.edu
# March 2017

# remove comments from csv file, replace missing values with -100000

import stdio

while stdio.isEmpty() == False:
    s = stdio.readLine()
    output = ""

    for i in range (0, len(s)):

        if i < len(s) - 1:
            if s[i] == ',' and s[i+1] == ',':
                # insert -100000 at index s[i]
                output = "".join((output, " -100000"))
            else:
                output = "".join((output, s[i]))

        elif i == len(s) - 1 and s[i] == ',':
            # insert -100000 at index s[i]
            output = "".join((output, " -100000"))

    # replace comma with empty string
    output = output.replace(',', ' ')

    stdio.writeln(output)
