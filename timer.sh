#!/bin/bash
proxy=$1
while true
do
killall mitmdump
killall mitmproxy
killall mitmweb
cd ~/HttpProxy
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5080 --mode upstream:http://$proxy & \
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5090 --mode upstream:http://$proxy & \
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5010 --mode upstream:http://$proxy & \
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5020 --mode upstream:http://$proxy & \
sleep 600
done

