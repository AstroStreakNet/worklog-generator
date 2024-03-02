# main.py

import write 

name = "Utkarsh Ranjan"
studentID = 102874485


def wrap_input(prompt, limit):
    while len(prompt) < 11:
        prompt += ' '

    input_text = input(f"\033[32m{prompt}: \033[0m")
    wrapped_text = ""

    while len(input_text) > limit:
        space_index = input_text.rfind(' ', 0, limit)
        
        if space_index == -1:  
            space_index = limit

        wrapped_text += input_text[:space_index] + "\n"
        input_text = input_text[space_index + 1:]

    wrapped_text += input_text
    return wrapped_text

def main():
    current_tasks = [] 
    next_tasks = []

    week = input("\033[36mWeek Number: \033[0m")

    t_this_week = int(input("\n\033[35mNumber of Tasks: \033[0m"))
    for i in range(t_this_week):
        entry = []
        entry.append(wrap_input(f"Task {i+1}", 52))
        entry.append(wrap_input("Status", 15))
        entry.append(wrap_input("Time hh:mm", 10))
        entry.append(wrap_input("Note", 28))
        print("-")

        current_tasks.append(entry)


    t_next_week = int(input("\n\033[35mNumber of tasks for next week: \033[0m"))
    for i in range(t_next_week):
        entry = []
        entry.append(wrap_input(f"Task {i+1}", 90))
        entry.append(wrap_input("Time", 25))
        print("-")

        next_tasks.append(entry)

    summary = input("\033[35mSummary/Reflection:\033[0m\n")

    write.generate(name, studentID, week, current_tasks, next_tasks, summary)

if __name__ == "__main__":
    main()

