
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
export BUILD_VERSION=0.0.008
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