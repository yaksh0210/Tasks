# TASK 1

```
Create a python script that reads a list of IP addresses from a txt file and stores them in a list. Create two functions, one to check if the ip address is public or private, and second one to check if the ip address is reachable or not. Iterate through the list and if the ip is public then check it's reachability and display it in the below format. 

````
 
* > 1st ip Reachable
 
* > 2nd ip Not Reachable

### Refreneces
+ for subprocess module

> https://www.geeksforgeeks.org/python-subprocess-module/ 

+ for ipaddress module

> https://www.geeksforgeeks.org/how-to-manipulate-ip-addresses-in-python-using-ipaddress-module/

+ Ping Module

> https://pypi.org/project/ping3/

# Solution
```
1 Importing a subprocess module so that with help of subprocess module we can run shell command here specifically "ping" command that helps to check the network is reachable or not
 ```


> import subprocess 


```
2 Create one function to check the ip is reachable or not reachable where we are going to use subprocess module to run ping command on IP which we will take from the defined IP list 

In this function we will use error handling as well as stdout for making sure that if the subprocess run
ping command gets fail what next step will be there to handle 
```

```python

def is_reachable(ip):
    result = subprocess.run(['ping', '-c', '3', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0
```


``` 
3 The very next process is that we will going to create another function in which we will identify that the given ip is private or public 

we will also take help of ipaddress module 
```

```python
def is_public_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return not ip_obj.is_private
    except ValueError:
        return False
```

```
The above funtion will check the ip is private or not if it is private it will return true if not then it will return false it also handles the Valueerror using exception handling case
```

``` 
4 now we will create main method and define list in it as well as we will create on for loop for the list to check ip one by one with function calling and it will check first ip is private or public and then it will check its reachable or not reachable
```

```python

def main():
    
    ip_list = ["8.8.8.8", "192.168.49.1", "10.0.0.1" , "10.0.0.2"]

    for ip in ip_list:
        if is_public_ip(ip):
            print("ip " + ip + " is a public.")
        else:
            print("ip " + ip + " is a private.")

        if is_reachable(ip):
            print("ip" + ip + " is reachable.")
        else:
            print("ip " + ip + " is not reachable.")
```

``` 
5 At last we will call the main method as well to start the program from main line method
```

```python
if __name__ == "__main__":
    main()
```

# Task 2

``` 
Make minor change if the ip address is public then and only it should check the ip is public or not and also remove the ip address is private or public checking scenario 

```

## Soultion

```python
for ip in ip_list:
        if is_public_ip(ip):
            if is_reachable(ip):
              print( ip + "\nreachable.")
            else:
              print(ip + " is not reachable.")
        else:
            print("")
```

``` 
minor change in logic 
```


# Task 3 

```
Now make one txt file read ip address from txt file in a list and also make focus on out put like

"ip"
reachable 

"ip"
not reachable

```

## Solution

+ to read using file module the logic will be change a bit like 

```python
    with open('ip_add.txt', 'r') as file:
        ip_list = file.read().splitlines()
```

+ it will be repalced with static list to read list from file 

+ With...as... are context manager used to make sure that file is closed after successfully completion

+ open is used to open a file of given name

+ file.read() to read the file and splitlines() method to separate the content while reading the ip address


# Task 4
```
now use the Python ping module to complete the tasks in replace of subprocess 
```

## Solution

+ We will replace the subprocess module with python ping and apply changes like 


``` from ping3 import ping ``` in replace of ``` import subprocess```

+ then we make changes in reachable function where we had use the subprocess module now 

```python
def is_reachable(ip):
    return ping(ip, timeout=3) is not None
```
+ here the ping is method from module ping3 which is currently useful then old pythonping module 

+ timeout will complete ping in given timeout seconds 

+ is not none is one which means if ip gets ping then reachable and not then its not reachable
