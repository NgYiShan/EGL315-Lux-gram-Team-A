from pythonosc import udp_client
import RPi.GPIO as gpio
import time
import subprocess
# import Pyros

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
button_pin = 27
pyro_pin = 5
ledw_pin = 6
confetti_pin = 13

gpio.setup(button_pin,gpio.IN,pull_up_down =gpio.PUD_UP)
gpio.setup(pyro_pin,gpio.IN,pull_up_down =gpio.PUD_UP)
gpio.setup(ledw_pin,gpio.IN,pull_up_down =gpio.PUD_UP)
gpio.setup(confetti_pin,gpio.IN,pull_up_down =gpio.PUD_UP)

gpio.setup(14,gpio.OUT)
gpio.output(14,0)
push_flag = 0

def send_message(receiver_ip, receiver_port, address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

        # Send an OSC message to the receiver
        client.send_message(address, message)

        print("Message sent successfully.")
    except:
        print("Message not sent")

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.200.6"# wlan ip
PORT = 1314


addr = "/print"
msg = "I wan Noodles"
loop = 0
flag = 0
counter = 0
while True:
    if gpio.input(button_pin) ==gpio.LOW and loop == 0:
        if push_flag == 0:
            gpio.output(14,0)
            send_message(PI_A_ADDR, PORT, addr, msg)
            loop += 1
            flag = 1
            print(f"loop value is {loop}")
            time.sleep(7)
            push_flag = 1
            print(f"Push Flag is {push_flag}")
        gpio.output(14,1)
    elif gpio.input(button_pin) ==gpio.LOW and loop == 1:
        msg = "Michael"
        if push_flag == 1:
            print("HUATS")
            gpio.output(14,0)
            send_message(PI_A_ADDR, PORT, addr, msg)
            loop += 1
            print(f"Push Flag is {push_flag}")
            print(f"loop value is {loop}")

    if gpio.input(pyro_pin) ==gpio.LOW:
        msg = "Explosion"
        print("ello")
        subprocess.run(["python","Pyros.py"])
    if gpio.input(ledw_pin) ==gpio.LOW:
        msg = "LED wall"
        print("Lello")
        subprocess.run(["python","LEDWall.py"])
    if gpio.input(confetti_pin) ==gpio.LOW:
        msg = "Confetti"
        print("Cello")
        subprocess.run(["python","Confetti.py"])
    
    if flag == 1:
        counter += 1
    if counter == 25000000:
        print("RESETTING")
        loop = 0
        counter = 0 
        flag = 0
        push_flag = 0
        print(f"\n\n\nLoop is now {loop}\n\n\n\n")
        print(f"push_flag value is {push_flag}")
        msg = "I wan Noodles"

    
#    if counter % 1000000 == 0:
#        print(counter)
       
        
    
