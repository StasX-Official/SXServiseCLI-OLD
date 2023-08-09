import sys
import time
import os
import http.server
import socketserver
from datetime import datetime
from colorama import init, Fore, Back, Style

#Project developer: StasX
#The project is under development
#App version - v1.02Beta


init(autoreset=True)
ModuleNotFoundError = "Plugin not found. Install the plugin on our website https://sxcomp.42web.io/ or contact SX technical support."
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
Yes = True
No = False
file = open("logs.txt", "a")

sxserviseclilogo = Fore.GREEN + """
#######  ###  ##  #######  #######  ######   ##  ###  #######  #######  #######           #######   ##      #######
 ##       ###  ##  ##       ##       ##  ##   ##  ###    ###    ##       ##                ##  ###   ##        ###
 #######  ###  ##  #######  ##       ##  ##   ##  ###    ###    #######  ##                ##  ###   ##        ###
      ##   #####        ##  #######  #######  ##  ###    ###         ##  #######           ##       ###        ###
 ###  ##  ##  ###  ###  ##  ###      ### ###  ## ####    ###    ###  ##  ###               ##   ##  ###        ###
 ###  ##  ##  ###  ###  ##  # #      ### ###   #####     ###    ###  ##  # #               ##   ##  ###        ###
 #######  ##  ###  #######  #######  ### ###    ###    #######  #######  #######           #######  ######   #######
"""
print(sxserviseclilogo)
print("Welcome to SXSERVISE CLI!")
print("Login to your account - loginCL")
print(" ")

command0 = "exit"
command1 = "help"
command2 = "loginCL"
command3 = "support"
command4 = "localhost"

def command_help():
    print("Command list:")

    input_command()

def command_loginCL():
    print("ERROR!")
    input_command()

def command_support():
    print(" edfd")
    input_command()

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
        text_to_write = f"{formatted_time} Starting localhost...\n"
        file.write(text_to_write)
        start_local_server()
    elif localhostcommand == 1:
        print("Stopping localhost...")
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
    else:
        print(Fore.RED + "Unknown command.")
        text_to_write = f"{formatted_time} Error code: 404. Unknown command.\n"
        file.write(text_to_write)
        input_command()

input_command()
file.close()
