import math

def network_query():
    network_address = input("Please enter a valid IPv4 network address [X.X.X.X/X]: ")
    while not is_valid_network(network_address):
        network_address = input("Please enter a valid IPv4 network address [X.X.X.X/X]: ")

def is_valid_network(address):
    network_segments = address.split('/')
    network_bytes = address[0].split('.')
    network_mask = address[1]

    for byte in network_bytes:
        if any(not char.isdigit() for char in byte):
            print("The address should only consist of numbers.")
            return False
        if not (0 <= int(byte) <= 255):
            print("The address must only have bytes between 0 and 255.")
            return False
        if len(byte) != 1 and byte[0] == 0:
            print("Bytes of the address cannot have leading zeros.")
            return False
        
    if not (0 <= network_mask <= 32):
        print("The CIDR mask value must be between 0 and 32.")
        return False
    
    return True

    

def subnet_info_query(subnet_number):
    ...

def calculate_subnet_info(next_available, users, network):
    subnet_info = {}
    
def main():
    network_query()

if __name__ == "__main__":
    main()