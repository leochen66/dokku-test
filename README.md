# Dokku Test

## Install Dokku
```
wget -NP . https://dokku.com/install/v0.34.8/bootstrap.sh
sudo DOKKU_TAG=v0.34.8 bash bootstrap.sh
```

## Setup
1. SSH Key
```
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub | dokku ssh-keys:add admin
```
2. Domain and DNS
```
dokku domains:set-global DNS_NAME
dokku domains:set-global IP_ADDRRESS
```
3. Create an application
```
dokku apps:create APP_NAME
```
4. Add new git remote
```
git remote add dokku dokku@DNS_NAME:APP_NAME
```
5. Set to build with Dockerfile
```
dokku builder-dockerfile:set APP_NAME dockerfile-path
```

## Deployment
### Deploy with Github Action
1. Setup SSH_PRIVATE_KEY
2. Trigger Github Action

### Deploy with cli
```
git push dokku main
```


## Useful command
```
# Show app names
dokku apps:list

# Show app status
dokku ps:report APP_NAME

# Show scale status for each process
dokku ps:scale APP_NAME

# Show logs
dokku logs APP_NAME
```