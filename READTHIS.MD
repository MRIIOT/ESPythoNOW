
## install docker

```
curl -fsSL https://get.docker.com -o ~/get-docker.sh
sudo sh ~/get-docker.sh
sudo usermod -aG docker "$USER"
newgrp docker
sudo systemctl enable --now docker
```

## prep secrets

```
echo "your github user" > ~/secret.ghuser
echo "your github pat" > ~/secret.ghpat
echo "your dockerhub password" > ~/secret.dhpass
```

## clone repo

```
cd ~
git clone https://$(cat ~/secret.ghuser):$(cat ~/secret.ghpat)@github.com/MRIIOT/ESPythoNOW.git
```

## build image

```
export BUILD_VERSION=0.0.031
docker build -f ~/ESPythoNOW/Dockerfile --tag=ladder99/espythonow:latest --tag=ladder99/espythonow:$BUILD_VERSION ~/ESPythoNOW
cat ~/secret.dhpass| docker login --username ladder99 --password-stdin
docker push ladder99/espythonow --all-tags
docker logout
```

## standup

```
docker compose \
  -f ~/ESPythoNOW/docker-compose.yml \
  --env-file ~/ESPythoNOW/.env \
  up -d --force-recreate
```

## running bare metal

```angular
sudo apt install git python3-venv net-tools

git clone https://github.com/ChuckMash/ESPythoNOW.git
cd ESPythoNOW
python3 -m venv venv
source venv/bin/activate
pip install scapy
sudo bash prep.sh wlo2 8

# create sniff.py

cp venv/bin/python3 venv/bin/python_netraw
sudo chown $USER venv/bin/python_netraw
chmod -x,u+x venv/bin/python_netraw
sudo setcap cap_net_raw=eip venv/bin/python_netraw
python_netraw sniff.py
```