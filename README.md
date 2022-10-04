This repo uses the cloud environment on GCP to set up VM instance.

The VM instance is given the name "mysqltest"


After connecting to the VM by opening SSH in new browser we run the command sudo apt-get update to set things up
Next command is "sudo apt install mysql-server mysql-client" which installs mysql
To get into mysql we run "sudo mysql"

In order to make the mysql instance available to external computers, we have to go to firewalls in GCP and crete a new firewall rule and next to specified protocols and ports check TCP and add port 3306 which is the port for mysql.

A .env file is created to contain credentials of dummy user that can make queries in mysql. 
A dummy data set will be used to be entered into dummy database 'dummy'
