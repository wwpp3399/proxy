#!/bin/bash
while true
do
killall mitmdump
killall mitmproxy
killall mitmweb
cd ~/HttpProxy
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5080 & \
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5090 & \
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5010 & \
mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5020 & \
sleep 600
done

