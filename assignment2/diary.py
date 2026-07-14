import csv
import os
import traceback


# Task 1: Diary Program
try:
    # Open the file for appending using a with statement
    with open("diary.txt", "a") as diary_file:
        # First prompt
        user_input = input("What happened today? ")

        # Loop until "done for now" is entered
        while user_input != "done for now":
            # Write the line to the file with a newline
            diary_file.write(user_input + "\n")

            # Prompt for the next line
            user_input = input("What else? ")

        # Write "done for now" to the file
        diary_file.write("done for now\n")
        print("Diary entry saved. Goodbye!")

except Exception as e:
    # Get traceback information
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')

    # Print exception details
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")

## task 2: Read employees.csv and store in a dictionary


def read_employees(): 
    employees = {}
    rows = []
    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            first = True
            for row in reader:
                if first:
                    employees["fields"] = row
                    first=False
                else:
                    rows.append(row)
            employees["rows"] = rows
        return employees
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print("employees: ", employees)




##Task 3: Find the Column Index
# ---------------------------------------------------------------------------
def column_index(name):
    return employees["fields"].index(name)


employee_id_column = column_index("employee_id")


# ---------------------------------------------------------------------------
# Task 4: Find the Employee First Name
# ---------------------------------------------------------------------------
def first_name(row_number):
    idx = column_index("first_name")
    return employees["rows"][row_number][idx]


# ---------------------------------------------------------------------------
# Task 5: Find the Employee - a Function in a Function
# ---------------------------------------------------------------------------
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# ---------------------------------------------------------------------------
# Task 6: Find the Employee with a Lambda
# ---------------------------------------------------------------------------
def employee_find_2(employee_id):
    matches = list(
        filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"])
    )
    return matches


# ---------------------------------------------------------------------------
# Task 7: Sort the Rows by last_name Using a Lambda
# ---------------------------------------------------------------------------
def sort_by_last_name():
    idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[idx])
    return employees["rows"]


sort_by_last_name()
print(employees)


# ---------------------------------------------------------------------------
# Task 8: Create a dict for an Employee
# ---------------------------------------------------------------------------
def employee_dict(row):
    result = dict(zip(employees["fields"], row))
    result.pop("employee_id", None)
    return result


print(employee_dict(employees["rows"][0]))


# ---------------------------------------------------------------------------
# Task 9: A dict of dicts, for All Employees
# ---------------------------------------------------------------------------
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)
    return result


print(all_employees_dict())


# ---------------------------------------------------------------------------
# Task 10: Use the os Module
# ---------------------------------------------------------------------------
def get_this_value():
    return os.getenv("THISVALUE")


# ---------------------------------------------------------------------------
# Task 11: Creating Your Own Module
# ---------------------------------------------------------------------------
def set_that_secret(new_secret):
    assignment2.custom_module.set_secret(new_secret)


set_that_secret("open sesame")
print(assignment2.custom_module.secret)


# ---------------------------------------------------------------------------
# Task 12: Read minutes1.csv and minutes2.csv
# ---------------------------------------------------------------------------
def _read_minutes_csv(path):
    data = {}
    rows = []
    try:
        with open(path, newline="") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(tuple(row))
        data["rows"] = rows
    except Exception as e:
        print(f"Error reading {path}: {e}")
        exit(1)
    return data


def read_minutes():
    m1 = _read_minutes_csv("../csv/minutes1.csv")
    m2 = _read_minutes_csv("../csv/minutes2.csv")
    return m1, m2


minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)


# ---------------------------------------------------------------------------
# Task 13: Create minutes_set
# ---------------------------------------------------------------------------
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1 | set2


minutes_set = create_minutes_set()


# ---------------------------------------------------------------------------
# Task 14: Convert to datetime
# ---------------------------------------------------------------------------
def create_minutes_list():
    as_list = list(minutes_set)
    converted = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), as_list) # type: ignore
    )
    return converted


minutes_list = create_minutes_list()
print(minutes_list)


# ---------------------------------------------------------------------------
# Task 15: Write Out Sorted List
# ---------------------------------------------------------------------------
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted = list(
        map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list)
    )
    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)
    return converted


write_sorted_list()
