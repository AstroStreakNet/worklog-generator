# main.py

import sys 
import write 
import parse

name = "Utkarsh Ranjan"
studentID = 102874485


def main():
    if len(sys.argv) > 1:
        week, tasks, plans, summary = parse.parse_file(sys.argv[1])
    else:
        week, tasks, plans, summary = parse.runtime_input()

    write.generate(name, studentID, week, tasks, plans, summary)


if __name__ == "__main__":
    main()

