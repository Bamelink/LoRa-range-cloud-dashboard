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