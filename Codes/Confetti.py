# Huats 2023 oscstarterkit
import socket
import RPi.GPIO as GPIO
import time

# FOR INFO: IP address and port of the receiving Raspberry Pi
Pan_IP = "192.168.200.7"
Pan_port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((Pan_IP, Pan_port))

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up the button pin
button_pin2 = 15
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

push_flag = 0

while True:
    if GPIO.input(button_pin2) == GPIO.LOW:
        if push_flag == 0:
            Pan_msg = b"UDPSend(1,'{wdcustomscriptclick(4)}')!"
            s.sendto(Pan_msg,(Pan_IP, Pan_port))
            print("Fired")
            ## block end
            push_flag = 1
        else:
            ## write in this block what happens upon 2nd press
#             send_message(PI_A_ADDR, PORT, addr, deinit_msg)
            print("Reserved")
            ## block end
            push_flag = 0
        time.sleep(2)