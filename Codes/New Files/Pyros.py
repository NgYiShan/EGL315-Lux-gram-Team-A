# Huats 2023 oscstarterkit
import socket
import RPi.GPIO as GPIO
import time
from pythonosc import udp_client
# FOR INFO: IP address and port of the receiving Raspberry Pi
Pan_IP = "192.168.200.7"
Pan_port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((Pan_IP, Pan_port))

MA_IP = "192.168.200.73"
MA_port = 8000
addr = "/gma3/cmd"
def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
		# Send an OSC message to the receiver
		client.send_message(address,message)
		print("Message sent successfully.")
	except:
		print("Message not sent")
# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up the button pin
button_pin2 = 5
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

push_flag = 0
finished = 0
while finished == 0:
    if GPIO.input(button_pin2) == GPIO.LOW:
        if push_flag == 0:
            Pan_msg = b"UDPSend(1,'{wdcustomscriptclick(3)}')!"
            s.sendto(Pan_msg,(Pan_IP, Pan_port))
            MA_msg = "Go+ Sequence 15 Cue 1"
            send_message(MA_IP,MA_port,addr,MA_msg)
            time.sleep(3)
            MA_msg = "Off Sequence 15"
            send_message(MA_IP,MA_port,addr,MA_msg)
            print("Fired")
            ## block end
            push_flag = 1
            finished = 1
        else:
            ## write in this block what happens upon 2nd press
#             send_message(PI_A_ADDR, PORT, addr, deinit_msg)
            print("Reserved")
            ## block end
            push_flag = 0
        time.sleep(0.5)
        