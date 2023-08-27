import sys
import time
import os
import json
import tqdm
import qrcode
import string
import random
import platform
import subprocess
import http.server
import socketserver
from tqdm import tqdm
from datetime import datetime
from colorama import init, Fore, Back, Style

#Project developer: StasX
#The project is under development
#App version - v4.10Beta
#Copying the code is prohibited by SX copyright.


init(autoreset=True)
ModuleNotFoundError = "Plugin not found. Install the plugin on our website https://sxcomp.42web.io/ or contact SX technical support."
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
Yes = True
No = False
file = open("logs.txt", "a")

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

def command_help():
    print("Command list:")
    print("help - Display this list of commands")
    print("loginCL - Login to your account")
    print("support - Contact technical support")
    print("localhost - Manage local server")
    print("json - Manage JSON files")
    print("qr - Manage QR codes")
    print("exit - Exit the program")

    input_command()

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def command_generate_password():
    password_length = int(input("Enter the length of the password: "))
    password = generate_random_password(password_length)
    print("Generated password:", password)
    input_command()

def ping_host(host):
    try:
        subprocess.run(["ping", "-c", "4", host])
        host_to_ping = input("Enter the host to ping: ")
        ping_host(host_to_ping)
    except Exception as e:
        print("Error:", e)

def command_loginCL():
    print("Not available in beta...")
    input_command()

def command_support():
    print("If you need assistance or have any questions, please contact our technical support.")
    print("Site - http://sxcomp.42web.io/")
    input_command()


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
        input_command()
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        command_json_menu()
    

def start_local_server(port=8000, directory="localhostData"):
    handler = http.server.SimpleHTTPRequestHandler
    handler.directory = directory
    with socketserver.TCPServer(("", port), handler) as httpd:
        message = f"Server started at port {port} - http://localhost:8000/"
        print(Fore.RED + "Press Control + C to stop localhost")
        print(message)

        message = f"Serving directory: {directory}"
        print(message)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            text_to_write = f"{formatted_time} Localhost server stopped.\n"
            file.write(text_to_write)
            print("Server stopped.")


def command_localhost():
    print("")
    print("Start localhost - 0")
    print("Stop localhost - 1")
    print("exit - 2") # taskkill /PID 8000
    print("")
    localhostcommand = int(input(Fore.BLUE + "sxservise >>> "))
    if localhostcommand == 0:
        print("Starting localhost...")
        for i in tqdm(range(100)):
            time.sleep(0.01)
        text_to_write = f"{formatted_time} Starting localhost...\n"
        file.write(text_to_write)
        start_local_server()
    elif localhostcommand == 1:
        print("Stopping localhost...")
        for i in tqdm(range(100)):
            time.sleep(0.005)
        text_to_write = f"{formatted_time} The stop_localhost command is running\n"
        file.write(text_to_write)
        stop_local_server()
    elif localhostcommand == 2:
        input_command()
    elif localhostcommand == command0:
        text_to_write = f"{formatted_time} The exit command is running\n"
        file.write(text_to_write)
        input_command()
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        command_localhost()

def stop_local_server():
    print("Stopping the server.")
    text_to_write = f"{formatted_time} Stopping the localhost server.\n"
    file.write(text_to_write)
    raise KeyboardInterrupt

def create_qrcode():
    print("Your text for the QR code:")
    qrcodetextdata = input()
    qrcodesizedataY = int(input("QR code cell size (default is 10): "))
    qrcodesizedataX = int(input("Border width (default is 4): "))
    
    print("Creating your QR code...")
    for i in tqdm(range(100)):
        time.sleep(0.1)
    
    data = qrcodetextdata
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=qrcodesizedataY,
        border=qrcodesizedataX,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = "qrcode.png"
    img.save(img_path)
    
    print("QR code created successfully!")
    os.startfile(img_path)
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

def command_additional_info():
    additional_info = additional_information()
    print("Information stored:", additional_info)
    input_command()

def command_qrcode_menu():
    print("--QrCode---")
    print("Create - 0")
    print("Edit Existing - 1")
    print("Decode - 2")
    print("Wi-Fi QR Code - 3")
    print("Exit   - 4")
    print("-----------")
    command_qrcode = int(input(Fore.BLUE + ">>> "))
    
    if command_qrcode == 0:
        create_qrcode()
    elif command_qrcode == 1:
        edit_qrcode()
    elif command_qrcode == 2:
        decode_qrcode()
    elif command_qrcode == 3:
        create_wifi_qrcode()
    elif command_qrcode == 4:
        text_to_write = f"{formatted_time} The exit command is running\n"
        file.write(text_to_write)
        input_command()
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        command_qrcode_menu()

    
def edit_qrcode():
    filename = input("Enter the filename of the QR code to edit: ")
    
    try:
        with open(filename, "r") as qr_file:
            qrcodetextdata = qr_file.readline().strip()
        print("Editing QR code:", qrcodetextdata)
        
        new_text = input("Enter new text for the QR code: ")
        
        with open(filename, "w") as qr_file:
            qr_file.write(new_text)
        print("QR code updated successfully!")
        
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)

def decode_qrcode():
    print("Decode QR code:")
    qrcode_image = input("Enter the filename of the QR code image: ")
    
    try:
        img = qrcode.make(qrcode_image)
        qr_data = img.data.decode("utf-8")
        print("Decoded data:", qr_data)
    except FileNotFoundError:
        print(Fore.RED + "File not found." + Style.RESET_ALL)
    except UnicodeDecodeError:
        print(Fore.RED + "Error decoding QR code." + Style.RESET_ALL)

def create_wifi_qrcode():
    ssid = input("Enter Wi-Fi SSID: ")
    password = input("Enter Wi-Fi Password: ")
    
    wifi_qr_data = f"WIFI:S:{ssid};T:WPA;P:{password};;"
    qrcodesizedataY = int(input("QR code cell size (default is 10): "))
    qrcodesizedataX = int(input("Border width (default is 4): "))
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=qrcodesizedataY,
        border=qrcodesizedataX,
    )
    qr.add_data(wifi_qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = "wifi_qrcode.png"
    img.save(img_path)
    
    print("Wi-Fi QR code created successfully!")
    os.startfile(img_path)
    input_command()

def install_package(package_name):
    # Логіка для встановлення пакету за назвою
    print(f"Installing package {package_name}...")

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
    elif command == command9:
        text_to_write = f"{formatted_time} The passworld command is running\n"
        file.write(text_to_write)
        command_generate_password()
    elif command.startswith("sxg install"):
        text_to_write = f"{formatted_time} The sxg install command is running\n"
        file.write(text_to_write)
        package_name = command[len("sxg install "):]
        install_package(package_name)
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_time}" + command + "Unknown command.\n"
        file.write(text_to_write)
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        input_command()

input_command()
file.close()
