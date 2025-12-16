import math
NETWORK = "192.168.10.0/24"

def subnet_info_query(subnet_number):
    subnets = {} # Name -> Users
    occupied_subnets = [] # Keep track of distinct subnet names
    
    for i in range(subnet_number):
        subnet_name = input(f"Enter the name of the {i+1}. subnet: ")
        while subnet_name in occupied_subnets:
            print("New subnet name must be distinct from previous subnets. Please try again.")
            subnet_name = input(f"Enter the name of the {i+1}. subnet: ")

        occupied_subnets.append(subnet_name)
        subnets[subnet_name] = int(input(f"Enter the number of users on subnet {subnet_name}: "))

    return subnets

def calculate_subnet_info(next_available, users, network):
    subnet_info = {}
    required_bits = int(math.log2(users + 2)) # on b bits you can represent 2^b - 2 different addresses (network, BC)
    mask_bits = int(NETWORK[-3:]) + required_bits
    subnet_info["Network Address"] = network + f".{next_available}/" + mask_bits
    mask = int(mask_bits * '1' + (32 - mask_bits) * '0')


def main():
    network = NETWORK[:-3]
    network_bytes = network.split(".")
    subnet_number = int(input("Enter the number of subnets: "))
    subnets = dict(sorted(subnet_info_query(subnet_number).items(), key=lambda item: item[1], reverse=True))

    next_available = 0

    for subnet, users in subnets.items():
        print(f"-- Subnet {subnet}: --")
        subnet_info = calculate_subnet_info(next_available, users, NETWORK)

if __name__ == "__main__":
    main()