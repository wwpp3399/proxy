#!/bin/bash
type=$1
echo "参数是${type}"
if [[ $type == "" ]]; then
	echo "执行远程代理"
	proxy=$(curl http://47.116.12.2/getip?num=1&type=1&pro=&city=0&yys=0&port=1&time=3&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=1&regions=&username=chukou01&spec=1)
	
	killall mitmdump
	killall mitmproxy
	killall mitmweb
	cd ~/HttpProxy
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5080 --mode upstream:https://$proxy/ & \
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5090 --mode upstream:https://$proxy/ & \
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5010 --mode upstream:https://$proxy/ & \
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5020 --mode upstream:https://$proxy/ & \
	
elif [[ $type == 'v' ]]; then
	#statements
	echo "执行无代理模式"
	
	killall mitmdump
	killall mitmproxy
	killall mitmweb
	cd ~/HttpProxy
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5080  & \
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5090  & \
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5010  & \
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5020  & \
	
else
	echo "执行指定代理模式"
	
	killall mitmdump
	killall mitmproxy
	killall mitmweb
	cd ~/HttpProxy
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5080 --mode upstream:https://$1/ & \
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5090 --mode upstream:https://$1/ & \
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5010 --mode upstream:https://$1/ & \
	mitmdump -s main.py -s tls_passthrough.py --set client_certs=cer/soul.pem --set block_global=false -p5020 --mode upstream:https://$1/ & \
	
fi
	#statements
