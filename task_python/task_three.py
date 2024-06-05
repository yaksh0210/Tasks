import subprocess
import ipaddress

def is_reachable(ip):
    result = subprocess.run(['ping', '-c', '3', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

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
