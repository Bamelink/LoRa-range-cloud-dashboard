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
This downloads all images, creates the volumes to persistently store all data and then launches the containers.