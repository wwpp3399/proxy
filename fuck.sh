#!/bin/bash
git clone https://e.coding.net/wwpp3399/httpproxy/HttpProxy.git
yum install python3
pip3 install virtualenv
cd HttpProxy
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
deactivate
pip3 install mitmproxy
pip3 install PyMySql
pip3 install PyDes
mitmdump -s main.py -p5070 --set client_certs=soul.pem  --set block_global=false