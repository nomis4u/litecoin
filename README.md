# Litecoin 0.18.1 in Docker
Respoiroty contains Dockerfile to run Litecoin in Docker and as stateful in Kubernetes with a sample Jenkinsfile

## Requirements
- Docker - Jenkins server to have docker binary running
- kubectl - jenkins server to have kubectl binary installed
- kubeconfig - Kubeconfig which has permission to apply the statefulset in the appropriate location


## Dockerfile
Using `sha256sum` we are checking the checksum of the downloaded release and fails the build process if it returns an error.

## litecoin-statefulset.yaml
Assumptions
- There is already a namesapce `litecoin`
- Standard stoarge class is available

## Jenkinsfile
Sample Jenkinsfile for deploying the application to kubernetes.

# Anchore - Image Scan
Scans docker image for any vulnerability.

## docker-compose.yaml
The file is downloaded from https://engine.anchore.io/docs/quickstart/docker-compose.yaml
```
# curl -O https://engine.anchore.io/docs/quickstart/docker-compose.yaml
# docker-compose up -d
```
Above command will bring up all the necessary docker containers required to scan the docker image

## Add Docker Image for analysis
```
# docker-compose exec api anchore-cli image add nomdoc/litecoin:0.18.1
```

## Check for Vulneribility
```
# docker-compose exec api anchore-cli image vul nomdoc/litecoin:0.18.1
# docker-compose exec api anchore-cli evaluate check nomdoc/litecoin:0.18.1



