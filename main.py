import ipaddress
import math

def network_query():
    network_address = input("Please enter a valid IPv4 CIDR address [x.x.x.x/x]: ")
    while not is_valid_network(network_address):
        network_address = input("Please enter a valid IPv4 CIDR network [x.x.x.x/x]: ")

    return network_address

def return_int(lst): # Helper
    return int("".join(lst))

def is_valid_network(cidr):
    try:
        netw_add = ipaddress.IPv4Network(cidr)
    except ValueError:
        print("Correct usage: x.x.x.x/x")
        return False
    return True

def subnet_info_query():
    subnets = int(input("Enter the amount of subnets: "))
    while subnets < 1:
        int(input("Enter the amount of subnets: "))

    info_table = {}
    for i in range(subnets):
        s_name = input(f"Enter the name of subnet {i + 1}: ")
        s_hosts = int(input("Enter the amount of hosts on subnet {s_name}: "))
        info_table[s_name] = s_hosts
    return info_table


def calculate_subnet_info(next_available, users, network):
    subnet_info = {}
    
def main():
    net = network_query()
    subnet_table = subnet_info_query()

    

if __name__ == "__main__":
    main()