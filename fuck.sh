#!/bin/bash
yum install git
yum install psmisc
yum update -y nss curl libcurl
git clone https://e.coding.net/wwpp3399/httpproxy/HttpProxy.git
yum install python3
cd HttpProxy
pip3 install -r requirements.txt
deactivate
pip3 install mitmproxy
pip3 install PyMySql
pip3 install PyDes
rm -r ~/.mitmproxy/
mkdir ~/.mitmproxy/
systemctl stop firewalld.service 
cp -r cas/ ~/.mitmproxy
bash timer.sh v