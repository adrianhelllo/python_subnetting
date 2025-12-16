NETWORK = "192.168.10.0/24"

def subnet_info_query(subnet_number):
    subnet_info = {} # Name -> Users
    occupied_subnets = [] # Keep track of distinct subnet names
    for i in range(subnet_number):
        subnet_name = input(f"Enter the name of the {i+1}. subnet: ")
        while subnet_name in occupied_subnets:
            print("New subnet name must be distinct from previous subnets. Please try again.")
            subnet_name = input(f"Enter the name of the {i+1}. subnet: ")

        occupied_subnets[i] = subnet_name
        subnet_info[subnet_name] = int(input(f"Enter the number of users on subnet {subnet_name}: "))

    return subnet_info

def main():
    network = NETWORK[:-3]
    print(network)
    subnets = int(input("Enter the number of subnets: "))
    subnet_info = subnet_info_query(subnets)

if __name__ == "__main__":
    main()