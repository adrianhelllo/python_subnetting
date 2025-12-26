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

def subnet_info_query(taken, parent_cidr):
    subnets = int(input("Enter the amount of subnets: "))
    while subnets < 1:
        int(input("Enter the amount of subnets: "))

    info_table = {}
    for i in range(subnets):
        s_name = input(f"Enter the name of subnet {i + 1}: ")
        
        s_hosts = int(input(f"Enter the amount of hosts on subnet {s_name}: "))
        while 2 ** (get_cidr(parent_cidr, s_hosts) - 24) > 2 ** (32 - parent_cidr) - taken:
            print("Parent network can not be configured for this many hosts.")
            s_hosts = int(input(f"Enter the amount of hosts on subnet {s_name}: "))

        taken += get_cidr(parent_cidr, s_hosts)

        info_table[s_name] = s_hosts

    return info_table

def get_cidr(parent_mask, hosts):
    required_bits = math.ceil(math.log2(hosts + 2))
    cidr_value = parent_mask + required_bits
    return cidr_value

def mask_calculations(hosts, parent_mask):
    mask_bits = get_cidr(parent_mask, hosts)
    cidr_mask = '/' + str(mask_bits)
    
    binary_rep = (mask_bits * '1') + ((32 - mask_bits) * '0')
    binary_mask = [binary_rep[i:i+8] for i in range(0, len(binary_rep), 8)]

    decimal_mask = [int(binary_mask[i], 2) for i in range(len(binary_mask))]
    return (cidr_mask, binary_mask, decimal_mask)

def calculate_subnet_info(hosts, mask):
    subnet_info = {}
    mask_info = mask_calculations(hosts, mask)
    subnet_info["cidr"] = mask_info[0]
    subnet_info["b_mask"] = mask_info[1]
    subnet_info["d_mask"] = mask_info[2]

    return subnet_info
    
def main():
    net_segments = network_query().split('/')
    net_bytes = net_segments[0]
    net_cidr_prefix = int(net_segments[1])

    taken = 0
    subnet_table = subnet_info_query(taken, net_cidr_prefix)
    
    print(subnet_table)
    
    for subnet, hosts in subnet_table.items():
        info = calculate_subnet_info(hosts, net_cidr_prefix)
        print(f"------- Subnet {subnet} ------".center(30))
        print(f"The CIDR mask prefix: {info['cidr']}")
        print(f"The binary mask: ", end="")

        for byte in info["b_mask"]:
            print(byte, end=" ")
        print()

        print(f"The decimal mask: ", end="")

        for byte in info["d_mask"]:
            print(byte, end=" ")
        print()


if __name__ == "__main__":
    main()