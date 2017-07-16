#!/usr/bin/python

import os

os.system("yum install httpd -y")
#os.system("wget -O /var/www/html/index.html http://server0.example.com/candidate/station.html")
os.system("touch /var/www/html/index.html")
file=open("/var/www/html/index.html","w")
data1='This is Prodevans'
file.write(data1)
file.close()
data='<VirtualHost *:80> \nServerAdmin server0.example.com\nDocumentRoot "/var/www/html"\nServerName 192.168.1.218\n</VirtualHost>\n<Directory /var/www/html>\nrequire all granted\n</Directory>'
file=open("/etc/httpd/conf.d/one.conf","w")
file.write(data)
file.close()
os.system("systemctl restart httpd")
os.system("systemctl enable httpd")
os.system("firewall-cmd --permanent --add-service=http")
os.system("firewall-cmd --reload")
