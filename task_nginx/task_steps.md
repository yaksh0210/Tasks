# TASK STEPS


### Step 1 - install nginx

+ first updates the system

> sudo apt-get update

+ Then install nginx using 

> sudo apt install nginx

### Step 2 - start nginx service

+ Start nginx using

> sudo systemctl start nginx

+ check serivce is running or not using 

> systemctl status nginx.service


### Step 3 - create html and css file that you want to display on server nginx 


* create a directory to store html and css files

```shell
sudo mkdir /var/www/yaksh
cd /var/www/yaksh
```
+ create an html file inside it 

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML AND CSS</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>HELLO THERE</h1>
    <hr>
    <marquee>Einfochips</marquee>
    
</body>
</html>

```

+ now also create on css file

```css

*{
    color: aqua;
}

h1{
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

```

### Step 4 - Create your server on nginx 

+ to create server you need to create a file on given path 

> sudo nano /etc/nginx/sites-available/yaksh

- here "yaksh" is my file name for server


+ copy following code in the file :

```shell
server {
    listen 80;
    listen [::]:80;

    server_name yhtmcssproject.com www.yhtmcssproject.com;

    root /var/www/yaksh;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

```

+ here i have given the custom domain name to run it on localserver with that name 


### Step - 5 link nginx server to my domain 



```shell

sudo ln -s /etc/nginx/sites-available/yaksh /etc/nginx/sites-enabled/

```
+ after linking we will test the server is ok and running successfully or not using

> sudo nginx -t

+ once all process done we will restart our webserver using

>sudo systemctl restart nginx

### Step 5 - custom domain

go to hosts file

> sudo nano /etc/hosts

replace the localhost as below
``` 127.0.0.1	      localhost ```
with

``` 127.0.0.1 yhtmlcssproject.com www.yhtmlcssproject.com ```


### Step - 6 now check the domain is running on nginx or not using 

```shell 
Curl -I http://www.yhtmcssproject.com 
```