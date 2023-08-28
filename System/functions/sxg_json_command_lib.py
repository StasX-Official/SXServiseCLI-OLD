import json
import datetime
from colorama import init, Fore, Back, Style

ModuleNotFoundError = "Plugin not found. Install the plugin on our website https://sxcomp.42web.io/ or contact SX technical support."
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
Yes = True
No = False
file = open("logs.txt", "a")

def command_create_json():
    filename = input("Enter the filename for JSON: ")
    
    data = {}
    print("Enter data for JSON:")
    for key in ["name", "age", "city"]:
        data[key] = input(f"{key.capitalize()}: ")

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(Fore.GREEN + "JSON file created successfully." + Style.RESET_ALL)

def command_read_json():
    filename = input("Enter the filename for JSON: ")
    
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
            print("Data in JSON file:")
            print(data)
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)

def command_check_json_validity():
    filename = input("Enter the filename for JSON: ")
    
    try:
        with open(filename, "r") as json_file:
            json.load(json_file)
            print(Fore.GREEN + "JSON file is valid." + Style.RESET_ALL)
    except json.JSONDecodeError:
        print(Fore.RED + "JSON file is not valid." + Style.RESET_ALL)

def command_sort_json_data():
    filename = input("Enter the filename for JSON: ")
    
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
            sorted_data = {k: v for k, v in sorted(data.items())}
            print("Sorted JSON data:")
            print(sorted_data)
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)

def command_json_menu():
    print("-----------------")
    print("----json-menu----")
    print("-----------------")
    print("Create json - 0")
    print("Read json - 1")
    print("Check JSON validity - 2")
    print("Sort JSON data - 3")
    print("Exit - 4")

    jsonmenucommand = int(input())
    formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if jsonmenucommand == 0:
        text_to_write = f"{formatted_time} The create_json command is running\n"
        file.write(text_to_write)
        command_create_json()
    elif jsonmenucommand == 1:
        text_to_write = f"{formatted_time} The read_json command is running\n"
        file.write(text_to_write)
        command_read_json()
    elif jsonmenucommand == 2:
        text_to_write = f"{formatted_time} The check_json_validity command is running\n"
        file.write(text_to_write)
        command_check_json_validity()
    elif jsonmenucommand == 3:
        text_to_write = f"{formatted_time} The sort_json_data command is running\n"
        file.write(text_to_write)
        command_sort_json_data()
    elif jsonmenucommand == 4:
        text_to_write = f"{formatted_time} The exit command is running\n"
        file.write(text_to_write)
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        command_json_menu()