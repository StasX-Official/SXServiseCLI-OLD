import sys
import time
import os
import json
import tqdm
import qrcode
import string
import random
import ctypes
import platform
import subprocess
import http.server
import socketserver
from tqdm import tqdm
from datetime import datetime
from colorama import init, Fore, Back, Style

from System.functions.sxg_qrcode_command_v2300 import command_qrcode_menu

from System.functions.sxg_localhost_command_v3400 import command_localhost

from System.sxg_error_func import error



app_id="SXSERVISECLIGLOBALFREE"
app_com="githab.sxservise.sxcomp.42web.io"
app_ver="4.14"


#Project developer: StasX
#The project is under development
#App version - v2.15Beta 
#Copying the code is prohibited by SX copyright.

#ATTENTION! Support for the old version of SXServiseCLI has ended on April 8, 2024. We sincerely thank you for using our application during this time.
#If you are still using the old version, we recommend updating your program to the new version of SXServiseCLI 2024. The new version offers more features, improved performance, and ensures security.
#To update to the new version, visit the application page on GitHub -> https://github.com/StasX-Official/SXServiseCLI. If you have any questions or issues with the update, please contact our support at sxservise@outlook.com.
#Once again, thank you for using SXServiseCLI. We are always ready to assist you in your user experience!
#Sincerely,
#StasX


init(autoreset=True)
ModuleNotFoundError = "Plugin not found. Install the plugin on our website https://sxcomp.42web.io/ or contact SX technical support."
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
Yes = True
No = False
icon_path = os.path.abspath("logo.ico")
appid = "sxcomp.sxservisecli.sxg.v4200Beta"
file = open("logs.txt", "a")

my_app_id = "sxservisecli.sxcomp.sxg"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

def starting():
    print("Cheking files...")
    for i in tqdm(range(100)):
        time.sleep(0.01)

sxserviseclilogo = Fore.GREEN + """
 #######  ###  ##  #######  #######  ######   ##  ###  #######  #######  #######           #######   ##      #######
 ##       ###  ##  ##       ##       ##  ##   ##  ###    ###    ##       ##                ##  ###   ##        ###
 #######  ###  ##  #######  ##       ##  ##   ##  ###    ###    #######  ##                ##  ###   ##        ###
      ##   #####        ##  #######  #######  ##  ###    ###         ##  #######           ##       ###        ###
 ###  ##  ##  ###  ###  ##  ###      ### ###  ## ####    ###    ###  ##  ###               ##   ##  ###        ###
 ###  ##  ##  ###  ###  ##  # #      ### ###   #####     ###    ###  ##  # #               ##   ##  ###        ###
 #######  ##  ###  #######  #######  ### ###    ###    #######  #######  #######           #######  ######   #######
"""

starting()
print(sxserviseclilogo)
print("Welcome to SXSERVISE CLI!")
print("Login to your account - loginCL")
print(" ")

command0 = "exit"
command1 = "help"
command2 = "loginCL"
command3 = "support"
command4 = "localhost"
command5 = "json"
command6 = "qr"
command7 = "qrcode"
command8 = "ping"
command9 = "passworld"
command10 = "sxg install"
command11 = "http"
command12 = "https"
command13 = "dns"
command14 = "host"
command15 = "arduino"


def command_help():
    print("Command list:")
    print("help - Display this list of commands")
    print("loginCL - Login to your account BETA")
    print("support - Contact technical support")
    print("localhost - Manage local server")
    print("json - Manage JSON files")
    print("qr - Manage QR codes")
    print("exit - Exit the program")
    print("http - Connecting to web servers")
    print("dns - DNS analysis")
    print("host - Checking the availability of hosts")

    input_command()

def command_support():
    print("If you need assistance or have any questions, please contact our technical support.")
    print("Site - http://sxcomp.42web.io/")

def ping_host(host):
    try:
        subprocess.run(["ping", "-c", "4", host])
        host_to_ping = input("Enter the host to ping: ")
        ping_host(host_to_ping)
    except Exception as e:
        print("Error:", e)
        error("Error code: 4010. Error ping function", 1)

def command_loginCL():
    print("Sorry, but you are using an old version and this feature is not available.")
    input_command()

def select_ip():
    print("Select IP Address:")
    print("1. Localhost (127.0.0.1)")
    print("2. Custom IP")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        return "127.0.0.1"
    elif choice == "2":
        custom_ip = input("Enter custom IP: ")
        return custom_ip
    else:
        return "Unknown IP"

def additional_information():
    print("Additional Information:")
    print("Enter any additional information you want to store:")
    info = input()
    return info

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
        error("Error code: 404. File not found", 1)

def command_check_json_validity():
    filename = input("Enter the filename for JSON: ")
    
    try:
        with open(filename, "r") as json_file:
            json.load(json_file)
            print(Fore.GREEN + "JSON file is valid." + Style.RESET_ALL)
    except json.JSONDecodeError:
        print(Fore.RED + "JSON file is not valid." + Style.RESET_ALL)
        error("Error code: 4041. JSON file is not valid.", 1)

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
        error("Error code: 404. File not found", 1)

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

def command_additional_info():
    additional_info = additional_information()
    print("Information stored:", additional_info)
    input_command()

def install_package(package_name):
    print("This beta function")
    input_command()

def input_command():
    command = input(Fore.BLUE + ">>> ")
    if command == command1:
        text_to_write = f"{formatted_time} The help command is running\n"
        file.write(text_to_write)
        command_help()
    elif command == command2:
        text_to_write = f"{formatted_time} The login command is running\n"
        file.write(text_to_write)
        command_loginCL()
    elif command == command0:
        text_to_write = f"{formatted_time} The exit command is running\n"
        file.write(text_to_write)
        file.close()
        exit()
    elif command == command3:
        text_to_write = f"{formatted_time} The support command is running\n"
        file.write(text_to_write)
        command_support()
    elif command == command4:
        text_to_write = f"{formatted_time} The localhost command is running\n"
        file.write(text_to_write)
        command_localhost()
    elif command == command5:
        text_to_write = f"{formatted_time} The json command is running\n"
        file.write(text_to_write)
        command_json_menu()
    elif command == command6:
        text_to_write = f"{formatted_time} The qrcode command is running\n"
        file.write(text_to_write)
        command_qrcode_menu()
    elif command == command7:
        text_to_write = f"{formatted_time} The qrcode command is running\n"
        file.write(text_to_write)
        command_qrcode_menu()
    elif command == command8:
        text_to_write = f"{formatted_time} The ping command is running\n"
        file.write(text_to_write)
        host_to_ping = input("Enter the host to ping: ")
        ping_host(host_to_ping)
    elif command.startswith("sxg install"):
        text_to_write = f"{formatted_time} The sxg install command is running\n"
        file.write(text_to_write)
        package_name = command[len("sxg install "):]
        install_package(package_name)
    elif command == command11:
        text_to_write = f"{formatted_time} The http command is running\n"
        file.write(text_to_write)
        from System.functions.sxg_network_lib import http_req_func
    elif command == command12:
        text_to_write = f"{formatted_time} The https command is running\n"
        file.write(text_to_write)
        from System.functions.sxg_network_lib import http_req_func
    elif command == command13:
        text_to_write = f"{formatted_time} The dns command is running\n"
        file.write(text_to_write)
        from System.functions.sxg_network_lib import dns_lookup_func
    elif command == command14:
        text_to_write = f"{formatted_time} The host command is running\n"
        file.write(text_to_write)
        from System.functions.sxg_network_lib import check_host_av_func
    elif command == command15:
        text_to_write = f"{formatted_time} The arduino command is running\n"
        file.write(text_to_write)
        from System.functions.arduino.sxg_arduino_lib import sxg_arduino_Win32
    else:
        print(Fore.RED + "Unknown command.")
        error("Error code: 404. Unknown command", 1)
        text_to_write = f"{formatted_time}" + command + "Unknown command.\n"
        file.write(text_to_write)
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        input_command()
input_command()
file.close()
