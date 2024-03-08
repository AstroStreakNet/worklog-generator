# userinput

# [tasks, status, time, notes, plans]
LIMITS = [52, 15, 10, 27, 90]

DESCRIPTION = 52
STATUS = 15
TIME = 10
NOTE = 28
PLAN = 90

# break input text into multiple lines
def wrap_input(raw_text, limit):
    wrapped_text = ""

    while len(raw_text) > limit:
        space_index = raw_text.rfind(' ', 0, limit)

        if space_index == -1:  
            space_index = limit

        wrapped_text += raw_text[:space_index] + "\n"
        raw_text = raw_text[space_index + 1:]

    wrapped_text += raw_text
    return wrapped_text


# take input at runtime
def runtime_input():
    tasks = [] 
    plans = []

    # print prompt for specific input
    def take_input(prompt, limit):
        while len(prompt) < 11:
            prompt += ' '

        input_text = input(f"\033[32m{prompt}: \033[0m")
        return wrap_input(input_text, limit)

    week = input("\033[36mWeek Number: \033[0m")

    # get current week's progress information
    tasks_count = int(input("\n\033[35mNumber of Tasks: \033[0m"))
    for i in range(tasks_count):
        entry = []
        entry.append(take_input(f"Task {i+1}", LIMITS[0]))
        entry.append(take_input("Status", LIMITS[1]))
        entry.append(take_input("Time hh:mm", LIMITS[2]))
        entry.append(take_input("Note", LIMITS[3]))
        print("-")

        tasks.append(entry)

    # get next week's progress information 
    plans_count = int(input("\n\033[35mNumber of tasks for next week: \033[0m"))
    for i in range(plans_count):
        entry = []
        entry.append(take_input(f"Task {i+1}", LIMITS[4]))
        entry.append(take_input("Time", LIMITS[2]))
        print("-")

        plans.append(entry)

    summary = input("\n\033[35mSummary/Reflection:\033[0m\n")

    return week, tasks, plans, summary

# 
def parse_file(file_path):
    week = 0
    tasks = []
    plans = []
    summary = ""
    current_section = ''
    temp_entry = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if line.isdigit() and week == 0: 
                    week = int(line)
                    continue

                if line.lower().startswith("task:"):
                    if temp_entry:  # Finish the previous section before starting a new one
                        if current_section == 'task':
                            tasks.append(temp_entry)
                        elif current_section == 'plan':
                            plans.append(temp_entry)
                    temp_entry = []
                    current_section = 'task'
                    continue

                elif line.lower().startswith("plan:"):
                    if temp_entry and current_section == 'task':  # Finish the previous section if it was a task
                        tasks.append(temp_entry)
                    temp_entry = []
                    current_section = 'plan'
                    continue

                elif line.lower().startswith("summary:"):
                    if temp_entry:  # If there's an ongoing section, conclude it before starting the summary
                        if current_section == 'task':
                            tasks.append(temp_entry)
                        elif current_section == 'plan':
                            plans.append(temp_entry)
                    temp_entry = []  # Reset temp_entry but don't really use it for summary
                    current_section = 'summary'
                    continue

                if current_section == 'summary':
                    summary += line + " "  # Append the line to summary
                    continue

                if line.startswith('> ') and current_section in ['task', 'plan']:
                    if current_section == 'task':
                        limit = LIMITS[len(temp_entry) if len(temp_entry) < len(LIMITS) else -1]
                    else:  # for 'plan'
                        limit = LIMITS[4]
                    line_content = wrap_input(line[2:], limit)
                    temp_entry.append(line_content)

            # After exiting the loop, check if there's an unfinished section
            if current_section == 'task' and temp_entry:
                tasks.append(temp_entry)
            elif current_section == 'plan' and temp_entry:
                plans.append(temp_entry)

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        exit()

    return week, tasks, plans, summary

# # Example usage
# file_path = 'formataa.txt'  # Update this to your actual file path
# week, tasks, plans, summary = parse_file(file_path)

# print("Week:", week)
# print("Tasks:")
# for task in tasks:
#     for entry in task:
#         print(f"[{entry}]")
#     print("")
# print("Plans:")
# for plan in plans:
#     for entry in plan:
#         print(f"[{entry}]")
#     print("")
# print("Summary:", summary)
