# main.py

import write 

name = ""
studentID = 1234

def main():
    current_entries = []
    next_entries = []

    week = input("\033[36mWeek Number: \033[0m")

    t_this_week = int(input("\n\033[35mNumber of Tasks: \033[0m"))
    for i in range(t_this_week):
        entry = {
                "task"  : input(f"\033[32mTask {i+1} \033[0m: "),
                "status": input("\033[32mStatus \033[0m: "),
                "time"  : input("\033[32mTime   \033[0m: "),
                "note"  : input("\033[32mNote   \033[0m: ")
                }
        print("-")

        current_entries.append(entry)


    t_next_week = int(input("\n\033[35mNumber of tasks for next week: \033[0m"))
    for i in range(t_next_week):
        entry = {
                "task"  : input(f"\033[31mTask {i+1} \033[0m: "),
                "time"  : input("\033[31mTime   \033[0m: "),
                }
        print("-")

        next_entries.append(entry)

    summary = input("\033[35mSummary/Reflection:\033[0m\n")

    write.generate(name, studentID, week, current_entries, next_entries, summary)

if __name__ == "__main__":
    main()

