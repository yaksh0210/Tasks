from ping3 import ping
import ipaddress

def is_reachable(ip):
    return ping(ip, timeout=3) is not None

def is_public_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return not ip_obj.is_private
    except ValueError:
        return False

def main():

    with open('ip_add.txt', 'r') as file:
        ip_list = file.read().splitlines()

    for ip in ip_list:
        if is_public_ip(ip):
            if is_reachable(ip):
                print(ip + "\nreachable")
            else:
                print(ip + "\nnot reachable")
          
        print("\n")
if __name__ == "__main__":
    main()
