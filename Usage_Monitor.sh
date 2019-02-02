#!/bin/sh

while true
do

 top -n 1 | grep python3 > Usage_Monitor.txt
 python3 Usage_Monitor.py
 sleep 1800

done
