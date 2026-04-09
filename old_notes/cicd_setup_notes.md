To diable ssl verify
```
git config --global http.sslVerify false
``` 

jenkins installation:
https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-16-04

To get which distribution of linux:
echo $(lsb_release -cs)

Runner Setup 
https://about.gitlab.com/2016/04/19/how-to-set-up-gitlab-runner-on-digitalocean/

Gitlab-runner installation on ubuntu : 
https://packages.gitlab.com/runner/gitlab-ci-multi-runner/install#manual

curl -L https://packages.gitlab.com/runner/gitlab-ci-multi-runner/gpgkey | sudo apt-key add -
sudo apt-get update
sudo apt-get install debian-archive-keyring
sudo apt-get install -y apt-transport-https

Create a file named /etc/apt/sources.list.d/runner_gitlab-ci-multi-runner.list that contains the repository configuration below.

Make sure to replace ubuntu and trusty in the config below with your Linux distribution and version:

deb https://packages.gitlab.com/runner/gitlab-ci-multi-runner/ubuntu/ trusty main
deb-src https://packages.gitlab.com/runner/gitlab-ci-multi-runner/ubuntu/ trusty main

[replace trusty to  xenial]

sudo apt-get update
sudo apt-get install gitlab-runner

Then  do gitlab-ci-multi-runner registration:

sudo gitlab-ci-multi-runner register
URL: https://code.siemens.com/
token: follow below steps:
	Login to ad00 account
	login to code.siemens.com 
	Settings > CI/CD > Runner Settings > Expand >Specific runner (pick registration token)
description: azure
tag: azure-build
run untagged build: [by default false] press enter
lock runner: [by default false] press enter
executor:  docker
docker image: hello-world

gitlab-ci-multi-runner commands: 

sudo gitlab-ci-multi-runner status
sudo gitlab-ci-multi-runner verify
sudo gitlab-ci-multi-runner list

unregister gitlab-ci-multi-runner:
sudo gitlab-runner unregister --url https://github.com/ --token XXXXXXXXXXXXXXXXXXXXXXX

Below steps are not required:

openssl req -nodes -newkey rsa:4096 -keyout registry-auth.key -out registry-auth.csr -subj "/CN=gitlab-issuer"
openssl x509 -in registry-auth.csr -out registry-auth.crt -req -signkey registry-auth.key -days 3650


Template: 
.gitlab-ci.yml file:

image: localhost:5000/azure-java:1.5
stages:
  - build
  - test
  - deploy
build:
    stage: build
    script: echo "build sucessfully"
    tags:
    - azure-build
test:
    stage: test
    script: echo "Tested sucessfully"
    tags:
    - azure-build
deploy:
    stage: deploy
    script: echo "deployed successfully"
    tags:
    - azure-build
    
 ______________________________________________________
 
 docker installation  steps:
	https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04
	
docker proxy configuration which i made:

/etc/systemd/system/docker.service.d$ cat http-proxy.conf

[Service]
Environment="HTTP_PROXY=http://proxy-url:8080/" "NO_PROXY=ip"

/etc/systemd/system/docker.service.d$ cat https-proxy.conf
[Service]
Environment="HTTPS_PROXY=http://proxy-url:8080"

/etc/docker$ cat daemon.json
{
  "insecure-registries" : ["localhost:5000"]
}


systemctl daemon-reload
service docker restart

to restart docker:
sudo /etc/default/docker restart
systemctl daemon-reload
sudo service docker restart


Docker file: 
Docker file content:
FROM centos

# buildtime variable
ARG proxy_ip
ARG no_proxy_ip

# set proxy
ENV no_proxy ${no_proxy_ip}
ENV http_proxy ${proxy_ip}:8080
ENV https_proxy ${proxy_ip}:8080
ENV host_url http://132.186.64.237/mindsphere
ENV JAVA_TOOL_OPTIONS -Dhttp.proxyHost=${proxy_ip} -Dhttp.proxyPort=8080 -Dhttps.proxyHost=${proxy_ip} -Dhttps.proxyPort=8080

# install java
RUN yum update -y
RUN yum install -y \
       git \
       java-1.8.0-openjdk-devel \
    && yum clean all

# set env variables
ENV JAVA_HOME /etc/alternatives/jre/

#certificates
COPY siemens.crt .
COPY Siemens_Issuing_CA_Intranet_Server_2016.crt .

RUN keytool -importcert -keystore $JAVA_HOME/lib/security/cacerts -storepass changeit -file certname.crt -alias "alias name" -noprompt
RUN keytool -importcert -keystore $JAVA_HOME/lib/security/cacerts -storepass changeit -file crtfilename.crt -alias "alias" -noprompt

# Adding AZ-CLI
RUN yum check-update; yum install -y gcc libffi-devel python-devel openssl-devel
RUN curl "https://bootstrap.pypa.io/get-pip.py" | python
RUN pip install --pre azure-cli

# Terraform
COPY terraform /usr/local/bin/

## SSH Key
RUN mkdir /root/.ssh
COPY id_rsa.pub  /root/.ssh
COPY id_rsa  /root/.ssh
COPY known_hosts /root/.ssh

If you need a fresh start and com­pletely unin­stall docker, just run the fol­low­ing commands:

sudo apt-get purge docker-engine
sudo apt-get autoremove --purge docker-engine
rm -rf /var/lib/docker # This deletes all images, containers, and volumes


config.toml for Runner:
[[runners]]
  name = "azure"
  url = "code repo url"
  token = "gitlab tocken"
  executor = "docker"
  [runners.docker]
    tls_verify = false
    image = "hello-world"
    privileged = false
    disable_cache = false
    volumes = ["/cache"]
    shm_size = 0
  [runners.cache]

[[runners]]
  name = "azure"
  url = "code repo url"
  token = "gitlab tocken"
  executor = "docker"
  [runners.docker]
    tls_verify = false
    image = "hello-world"
    privileged = false
    disable_cache = false
    volumes = ["/cache"]
    shm_size = 0
  [runners.cache]
  
  
  --------------------------------------------------------------------------------
               
Java 8 installation:
http://tipsonubuntu.com/2016/07/31/install-oracle-java-8-9-ubuntu-16-04-linux-mint-18/

Jenkins installation on ubuntu steps: 
https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-16-04

wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins

Running & launching jenkins
sudo /usr/bin/java -Djava.awt.headless=true -jar /usr/share/jenkins/jenkins.war --webroot=/var/cache/jenkins/war --httpPort=80 & 

encrypted password stored in: sudo cat /var/lib/jenkins/secrets/initialAdminPassword 


azure cli installation:
https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest

git on ubantu:  https://www.vultr.com/docs/setting-up-git-on-ubuntu-14-04

terraform installation : 
wget https://releases.hashicorp.com/terraform/0.11.1/terraform_0.11.1_linux_amd64.zip
unzip terraform_0.11.1_linux_amd64.zip
sudo mv terraform /usr/local/bin/
terraform --version
-- sudo apt-get install zip unzip -- to install zip unzip 

KeePass : for password creation

Azure VM creation:
az ad sp create-for-rbac --name  <name-for-your-service-principal> 



to install openjdk8  without interactive mode:
sudo apt-get install openjdk-8-jdk

##Install certificates : https://github.com/escline/InstallCert

check and clean space
docker system df 
docker system prune -f
docker system prune --volumes -f

To delete all docker images forcefully.
docker rmi -f $(docker images -q)


services:
- name: mongo:v1.0
  alias: mongo
 variables:
    MONGO_HOST: mongo

