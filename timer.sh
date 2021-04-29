#!/bin/bash
proxy=$1
while true
do
killall mitmdump
killall mitmproxy
killall mitmweb
cd ~/HttpProxy
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5080 upstream:https://$proxy & \
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5090 upstream:https://$proxy & \
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5010 upstream:https://$proxy & \
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5020 upstream:https://$proxy & \
sleep 600
done

