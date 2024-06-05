import subprocess

def is_reachable(ip):
    result = subprocess.run(['ping', '-c', '3', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def main():
    ip_list = ["8.8.8.8","192.168.49.1","10.0.0.1","10.0.0.2"]
    for ip in ip_list:
        if is_reachable(ip):
            print("ip " +ip+ " is reachable.")
        else:
            print( "ip " +ip+ " is not reachable.")

if __name__ == "__main__":
    main()
