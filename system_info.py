#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import getpass
import socket
import platform
import time
import datetime

name = socket.getfqdn(socket.gethostname())
CaoZuo = platform.system()
Cpu = platform.machine()
Banben = platform.version()
Banben2 = platform.dist()

if CaoZuo == 'Windows':
    print ("Ope System:"),CaoZuo,("Sys Version:"),Banben,("Cpu Platform:"),Cpu
elif CaoZuo == 'Linux':
    print  ("Ope System:"),CaoZuo,("Sys Version:"),platform.dist(),("Cpu Platform:"),Cpu
else :
    print "Not identified"

print ("Comr Name:"),socket.getfqdn(socket.gethostname())
print ("Sys time:"),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print ("IP  Addr:"),socket.gethostbyname(name)
print ("Sys  User："),getpass.getuser()
print ("Boot Time:"),datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print ("Mem  Total："),psutil.virtual_memory().total/1024/1024,"MB"
print ("Mem  Free:"),psutil.virtual_memory().free/1024/1024,"MB"
print ("Mem  Usage:"),(psutil.virtual_memory().total-psutil.virtual_memory().free)/1024/1024,"MB"
print ("Swap Total:"),psutil.swap_memory().total/1024/1024,"MB"
print ("Swap Free:"),psutil.swap_memory().free/1024/1024,"MB"
print ("Swap Usage:"),(psutil.swap_memory().total-psutil.swap_memory().free)/1024/1024,"MB"
print ("Cpu  Number:"),psutil.cpu_count()
print ("Cpu  Ilde:"),(100-psutil.cpu_percent()),"%"
print ("Cpu  Sys:"),psutil.cpu_percent(),"%"
print ("Net  BY-Sent:"),psutil.net_io_counters().bytes_sent/1024/1024,"MB"
print ("Net  BY-Recv:"),psutil.net_io_counters().bytes_recv/1024/1024,"MB"
print ("Net  Pa-Sent:"),psutil.net_io_counters().packets_sent,"packets"
print ("Net  Pa-Recv:"),psutil.net_io_counters().packets_recv,"packets"
print ("Io   Read_count:"),psutil.disk_io_counters().read_count
print ("Io   Write_count:"),psutil.disk_io_counters().write_count
print ("Io   Read_bytes:"),psutil.disk_io_counters().read_bytes/1024/1024,"MB"
print ("Io   Write_bytes:"),psutil.disk_io_counters().write_bytes/1024/1024,"MB"
def IsOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print "Port is up:",ip,":",port
        return True
    except:
        print 'Port is down:',ip,":",port
        return False
#if __name__=='__main__':
IsOpen('127.0.0.1',80)
IsOpen('127.0.0.1',3306)
