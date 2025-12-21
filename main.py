import ipaddress
import math

def network_query():
    network_address = input("Please enter a valid IPv4 CIDR address [x.x.x.x/x]: ")
    while not is_valid_network(network_address):
        network_address = input("Please enter a valid IPv4 CIDR network [x.x.x.x/x]: ")

    return network_address

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
        s_hosts = int(input(f"Enter the amount of hosts on subnet {s_name}: "))
        info_table[s_name] = s_hosts

    return info_table

def mask_calculations(hosts, mask):
    required_bits = math.ceil(math.log2(hosts + 2))
    mask_bits = mask + required_bits
    cidr_mask = '/' + str(mask_bits)
    
    binary_rep = (mask_bits * '1') + ((32 - mask_bits) * 0)
    binary_mask = [binary_rep[i:i+8] for i in range(len(binary_rep))]

    decimal_mask = [int(binary_mask[i]) for i in range(len(binary_mask))]
    return (cidr_mask, binary_mask, decimal_mask)

def calculate_subnet_info(hosts, mask):
    subnet_info = {}
    mask_info = mask_calculations(hosts, mask)
    subnet_info["cidr"] = mask_info[0]
    subnet_info["b_mask"] = mask_info[1]
    subnet_info["d_mask"] = mask_info[2]

def calculate_subnet_info(next_available, users, network):
    subnet_info = {}
    
def main():
    net = network_query()
    subnet_table = subnet_info_query()
    print(subnet_table)



if __name__ == "__main__":
    main()