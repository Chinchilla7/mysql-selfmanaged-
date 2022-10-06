This repo uses the cloud environment on GCP to set up VM instance.

The VM instance is given the name "mysqltest". 
The region chosen is anywhere in the US.
For machine configurations, everything is to left to default besides the following:
Machine type - e2-medium 
Boot disk - Ubuntu OS, version ubuntu 18.04 lts x86/64
Fireqall - allow http and https traffic

After connecting to the VM by opening SSH in new browser we run the command sudo apt-get update to download and install updates for each outdated package and dependency on your system.
Next command is "sudo apt install mysql-server mysql-client" which installs mysql.
To get into mysql we run "sudo mysql"

In order to make the mysql instance available to external computers, we have to go to firewalls in GCP and crete a new firewall rule and next to specified protocols and ports check TCP and add port 3306 which is the port for mysql.

A .env file is created to contain credentials of dummy user that can make queries in mysql. 
The credentials in the .env file can be read using the function 'dotenv_values' from the package dotenv.

A dummy data set called "iris" will be used to be entered into dummy database 'dummy'.

