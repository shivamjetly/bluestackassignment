import os
import re

with open("C:/Users/sjetly/Downloads/Assignment2/start_assignment.log", encoding='utf8') as d:
    f = d.read()
    try:
        # Finding string "beginning of assignment"
        find = re.findall("beginning of assignment", f)
        print(find[0])
    except():
        print("Match not found")

    try:
        # Finding first occurrence of "required_pattern_"
        find = re.findall("required_pattern_\d\d", f)[0]
        print(find)
    except():
        print("Match not found")

directory = "C:/Users/sjetly/Downloads/Assignment2/Logs/"
for root, dirs, files in os.walk(directory):
    for basename in files:
        if re.search('required_pattern_\d\d', basename):
            basename = os.path.splitext(basename)[0]
            print(basename)

for fil in os.listdir(directory):
    with open(directory + fil, encoding='utf8') as f:
        fin = f.read()

        try:
            print(re.findall('assignment_completed.*\n.*\n', fin))
        except():
            print('Match not found')
