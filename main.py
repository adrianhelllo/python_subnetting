import math

def network_query():
    network_address = input("Please enter a valid IPv4 network address [x.x.x.x/x]: ")
    while not is_valid_network(network_address):
        network_address = input("Please enter a valid IPv4 network address [x.x.x.x/x]: ")

def return_int(lst): # Helper
    return int("".join(lst))

def is_valid_network(address):
    pattern = "x.x.x.x/x"
    address_bytes = []
    current_byte = []
    mask = 0

    print(address)

    #Form handling
    if not all(char.isdigit() or char in "./" for char in address):
        print("Correct usage: x.x.x.x/x")
        return False
    
    i = 0
    while address[i] != '/':
        while address[i] != '.':
            current_byte.append(address[i])
            i += 1
        i += 1 # Skip over dot
        address_bytes.append(current_byte)
        current_byte = [] # Reset

    if len(address_bytes) != 4:
        print("Correct usage: x.x.x.x/x")
        return False
    if not all(char.isdigit() for char in address[i+1:]): # i+1: step over '/'
        return False
        print("Correct usage: x.x.x.x/x")

    mask = return_int(address[i+1:]) # Convert remaining characters to mask
    
    #Byte handling
    for byte in address_bytes:
        if len(byte) != 0 and byte[0] == 0:
            print("Bytes must not have leading zeros.")
            return False
        if 0 <= return_int(byte) <= 255:
            print("Each byte must be between 0 and 255.")
            return False
        if not (0 <= mask <= 32):
            print("The mask must be between 0 and 32.")
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