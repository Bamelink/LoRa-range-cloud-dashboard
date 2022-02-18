# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Docker_%28container_engine%29_logo.svg/610px-Docker_%28container_engine%29_logo.svg.png" alt="drawing" width="120"/> Installation 

First of all make sure your repositories are up to date
```bash
sudo apt update
sudo apt upgrade -y
```
See https://docs.docker.com/engine/install/debian/ for manual installation. I would recommend the install script:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
If you are curious what the script does you can execute it by
```bash
DRY_RUN=1 sh ./get-docker.sh
```

# <img src="https://img.icons8.com/fluency/48/000000/launched-rocket.png" alt="drawing" width="40"/> Launching the Stack
## Docker-Compose
To launch this stack, you first need to install docker-compose:
If you are curious what the script does you can execute it by
```bash
sudo apt-get update && sudo apt-get install docker-compose -y
```

## Clone the Repository
Navigate into the folder where you want to store the files of the repository and clone it by running:
```bash
git clone git@gitlab.gwdg.de:esg/studentische-arbeiten/tp-lorawan/serverside.git
```
Note that you ssh-key has to be deposited inside gitlab.

## Launching
Navigate into the cloned repository and launch the docker-compose stack:
```bash
cd serverside
docker-compose up -d
```
This downloads and/or creates all images, creates the volumes to persistently store all data and then launches the containers.

## Login
For the following, change my ip address 192.168.178.63 with the one of your specific server running this stack!

Grafana can be reached by http://192.168.178.63:3000, the default login is "admin" "admin". After the first login you will be forced to create a new password. This will then be stored until you delete your volume. Furthermore the database should already be configured. When going to the "Explore" Tab in Grafana, you should be able to see automaticly generated test data.

To further test this stack, you can open NodeRed on http://192.168.178.63:1880.
There should be a Flow named "Testing". The upper one just takes Data and inserts this into the Database as a Test.\
 To get access to the Database, you have to insert the username and password by editing the node. You can finde these in the Dockerfile under database. If nothing changed, the default username is "grafana" and password is "kRXb4cJBU8WTgDGvTXDp". If everything wored, this data should be also visible in Grafana.\
The lower one is to fully test the stack which also includes MQTT

The python script can be used to test this, but you will need to have python installed on your system executing this script and also install the MQTT and numpy package by running
```bash
pip install paho-mqtt
pip install numpy
```
Inside the script, scroll down to the line "client.connect("192.168.178.63", 1883)" and again change the IP-adress to the one running the stack.\
After that, the script should execute just fine and insert a bunch of data into the database.