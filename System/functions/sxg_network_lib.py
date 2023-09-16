import sys
import os
import time
import requests
import socket


def http_req_func():
    print("-------------------------")
    print("Connecting to web servers")
    print("-------------------------")
    print("Connect to server - 0")
    print("exit - 1")
    http_reg_funt_input_command = int(input())
    if http_reg_funt_input_command == 0:
        print("Enter server url...")
        server_url_http_func_input = input()
        url_to_request = server_url_http_func_input
        response_data = http_request(url_to_request)
        print(response_data)
    elif http_reg_funt_input_command == 1:
        exit()
    else:
        print("Not Found.")
        http_req_func()

def http_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"HTTP Error: {response.status_code}"
    except requests.exceptions.RequestException:
        return "Unable to connect to the server."
    
def dns_lookup_func():
    print("-------------------------")
    print("      DNS analysis")
    print("-------------------------")
    print("Run the check - 0")
    print("exit - 1")

    dns_lookup_func_input_command = int(input())

    if dns_lookup_func_input_command == 0:
        print("Enter the domain...")
        dns_lookup_func_input_command_domain = input()
        domain_to_lookup = dns_lookup_func_input_command_domain
        result = dns_lookup(domain_to_lookup)
        print(result)
    elif dns_lookup_func_input_command == 1:
        exit()
    else:
        print("Not Found")
        dns_lookup_func()

  
def dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return f"Domain: {domain}, IP Address: {ip_address}"
    except socket.gaierror:
        return f"Domain {domain} not found."




def check_host_av_func():
    print("-------------------------")
    print("Host availability review")
    print("-------------------------")
    print("Run the check - 0")
    print("exit - 1")
    check_host_availability_command_input = int(input())
    if check_host_availability_command_input == 0:
        print("Enter host...")
        host = input()
        print("Enter port... Default 80")
        port = int(input())
        if check_host_availability(host, port):
            print(f"{host}:{port} is reachable.")
        else:
            print(f"{host}:{port} is not reachable.")

    elif check_host_availability_command_input == 1:
        exit()
    else:
        print("Not Found.")
        check_host_av_func()


def check_host_availability(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        return True
    except (socket.timeout, ConnectionError):
        return False
    

check_host_av_func()