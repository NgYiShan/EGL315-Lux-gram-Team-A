## This is a program to allow communication between MA3,Pandora and raspi.(no buttons)
## Last updated :  2 jul before 12am

#import library
from pythonosc import udp_client
import socket
import RPi.GPIO as GPIO
import time
import subprocess

#Pandora IP and UDP port(L : socket)
Pan_IP = "192.168.200.7"
Pan_port = 10000

#MA3 IP and UDP port(L : pythonosc)
MA_IP = "192.168.200.73"
MA_port = 8000

# Set up of the GPIO pins and button state
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button_pin = 27
Fbutton_pin = 26
GPIO.setup(Fbutton_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(14,0)
push_flag = 0

# PAN_r_IP = "192.168.200.5"
# PAN_r_port = 20000
# 
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind((PAN_r_IP, PAN_r_port))

##Link with Pandora(L : socket)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((Pan_IP, Pan_port))

##Function to link with MA3 and send message with feedback included(L : pythonosc)
def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
		# Send an OSC message to the receiver
		client.send_message(address,message)
		print("Message sent successfully.")
	except:
		print("Message not sent")


#send desired message to MA3(L : pythonosc)
Pan_msg = b"UDPSend(1,'{wdcustomscriptclick(8)}')!"
s.sendto(Pan_msg,(Pan_IP, Pan_port))
addr = "/gma3/cmd"
MA_msg = "Go+ Sequence 4 Cue 0.5"
send_message(MA_IP,MA_port,addr,MA_msg)
# time.sleep(5)

# #send desired message to Pandora(L : socket)
# Pan_msg = b"boo"
# s.sendto(Pan_msg,(Pan_IP, Pan_port))
# 
# #receive things from widgets
# while True:
#     data,addr = s.recvfrom(1024)
#     print("received message : %s"%data)
Pan_msg = b"UDPSend(1,'{wdcustomscriptclick(8)}')!"
s.sendto(Pan_msg,(Pan_IP, Pan_port))
MA_msg = "Go+ Sequence 4 Cue 1"
send_message(MA_IP,MA_port,addr,MA_msg)
# time.sleep(5  )

print("btn ready")
MA_msg = "Go+ Sequence 4 Cue 2"
send_message(MA_IP,MA_port,addr,MA_msg)

while True:
    if GPIO.input(Fbutton_pin) == GPIO.LOW:
        Pan_msg = b"UDPSend(1,'{wdcustomscriptclick(1)}')!"
        s.sendto(Pan_msg,(Pan_IP, Pan_port))
        MA_msg = "Go+ Sequence 4 Cue 3"
        send_message(MA_IP,MA_port,addr,MA_msg)
        time.sleep(10)
        MA_msg = "Go+ Sequence 4 Cue 3.5"
        send_message(MA_IP,MA_port,addr,MA_msg)
        GPIO.output(14,1)
        
    
    elif GPIO.input(button_pin) == GPIO.LOW:
        if push_flag == 0:
#             subprocess.run(["python","Pyros.py"])
#             subprocess.run(["python","Confetti.py"])
            GPIO.output(14,0)
            print("bye")
            ## block end
            Pan_msg = b"UDPSend(1,'{wdcustomscriptclick(2)}')!"
            s.sendto(Pan_msg,(Pan_IP, Pan_port))
            push_flag = 1
            MA_msg = "Go+ Sequence 4 Cue 4"
            send_message(MA_IP,MA_port,addr,MA_msg)
            time.sleep(2.42)
            MA_msg = "Go+ Sequence 4 Cue 5"
            send_message(MA_IP,MA_port,addr,MA_msg)
            time.sleep(47.06)
            MA_msg = "Go+ Sequence 4 Cue 5.7"
            send_message(MA_IP,MA_port,addr,MA_msg)
            time.sleep(2)
            MA_msg = "Go+ Sequence 4 Cue 6"
            send_message(MA_IP,MA_port,addr,MA_msg)
            time.sleep(8)
            MA_msg = "Go+ Sequence 4 Cue 7"
            send_message(MA_IP,MA_port,addr,MA_msg)
            time.sleep(15.51)
            MA_msg = "Go+ Sequence 4 Cue 0.5"
            send_message(MA_IP,MA_port,addr,MA_msg)
            Pan_msg = b"UDPSend(1,'{wdcustomscriptclick(8)}')!"
            s.sendto(Pan_msg,(Pan_IP, Pan_port))
            subprocess.run(["python","process.py"])
            break
        else:


            ## block end
            push_flag = 0
        time.sleep(0.5)