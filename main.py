import ipaddress
import math

BYTE_SIZE = 8
MASK_BITS = 32
MASK_BYTES = MASK_BITS // BYTE_SIZE

def network_query():
    network_address = input("Please enter a valid IPv4 CIDR address [x.x.x.x/x]: ")
    while not is_valid_network(network_address):
        network_address = input("Please enter a valid IPv4 CIDR network [x.x.x.x/x]: ")
    return network_address

def is_valid_network(addr):
    if '/' not in addr:
        print("Network address must contain a CIDR prefix")
        return False
    
    try:
        netw_add = ipaddress.IPv4Network(addr)
    except ValueError:
        print("Correct usage: x.x.x.x/x")
        return False
    return True

def subnet_info_query(parent_cidr):
    subnets = int(input("Enter the number of subnets: "))
    while subnets < 1:
        int(input("Enter the number of subnets: "))

    taken = 0
    info_table = {}

    for i in range(subnets):
        s_name = input(f"Enter the name of the {i+1}. subnet: ")
        s_hosts = int(input(f"Enter the number of hosts on subnet {s_name}: "))
        subnet_capacity = 2 ** subnet_bits(s_hosts)
        available = 2 ** (MASK_BITS - parent_cidr) - taken
        
        while subnet_capacity > available:
            print(subnet_capacity, available)
            print("Parent network can not be configured for a subnet with this number of hosts.")
            
            s_hosts = int(input(f"Enter the amount of hosts on subnet {s_name}: "))
            subnet_capacity = 2 ** subnet_bits(s_hosts) # Subnet block size
            available = 2 ** (MASK_BITS - parent_cidr) - taken

        taken += subnet_capacity

        info_table[s_name] = s_hosts

    return info_table

def subnet_bits(hosts):
    return math.ceil(math.log2(hosts + 2))

def subnet_cidr(hosts):
    cidr_value = MASK_BITS - subnet_bits(hosts)
    return cidr_value

def mask_calculations(hosts):
    subn_mask_bits = subnet_cidr(hosts)
    cidr_mask = '/' + str(subn_mask_bits)
    
    binary_rep = (subn_mask_bits * '1') + ((MASK_BITS - subn_mask_bits) * '0')
    binary_mask = [binary_rep[i:i+BYTE_SIZE] for i in range(0, len(binary_rep), BYTE_SIZE)]

    decimal_mask = [str(int(binary_mask[i], 2)) for i in range(len(binary_mask))]

    return (cidr_mask, binary_mask, decimal_mask)

def read_host_bits(parent_b, cidr):
    parent_b_bin = [bin(byte)[2:] for byte in parent_b]
    bit_string = ""

    mixed_octet = cidr // BYTE_SIZE
    first_host_bit = cidr % BYTE_SIZE
    
    bit_string += parent_b_bin[mixed_octet][first_host_bit:]
    bit_string += parent_b_bin[mixed_octet+1:] # Add full host bytes

    return bit_string

def utility_address_calculations(parent_b, taken, hosts, bits):
    netw_add_bytes = []
    
    for i in range(len(parent_b), -1, -1):
        if ...:
            ...

    

def calculate_subnet_info(hosts, mask):
    subnet_info = {}
    mask_info = mask_calculations(hosts)
    subnet_info["cidr"] = mask_info[0]
    subnet_info["b_mask"] = mask_info[1]
    subnet_info["d_mask"] = mask_info[2]

    ...

    return subnet_info
    
def main():
    net_segments = network_query().split('/')
    net_bytes = net_segments[0]
    net_cidr_prefix = int(net_segments[1])

    subnet_table = subnet_info_query(net_cidr_prefix) # !!!! To-do: sort by host number
    
    print(subnet_table)
    
    for subnet, hosts in subnet_table.items():
        info = calculate_subnet_info(hosts, net_cidr_prefix)
        print(f"+-----# Subnet {subnet} #----+".center(30))
        print(f"CIDR mask prefix: {info['cidr']}")
        print(f"Binary mask: {' '.join(info['b_mask'])}")
        print(f"Decimal mask: {'.'.join(info['d_mask'])}")

if __name__ == "__main__":
    main()