# EGL315-Lux-gram-Team-A

# grandMA3 Lighting Console

## grandMA3 setup

![Alt text](imgs/LightinUp%20Setup.jpg)


Launch grandMA3 on your laptop

Connect 1 laptop to a ma3 two-port node via a LAN cable, then connect the two-port node to a SaCN to DMX converter via a LAN cable.


![Alt text](<imgs/MA3 Network.jpg>)


Ensure the ip addresses for your laptop and ma3 Two-port Node are in the same subnet.\
Under DMX  protocols enable output and set local and sACN universes


![Alt text](<imgs/MA3 sACN.jpg>)


Connect your two Spot Moving heads to the DMX converter via DMX cables.

you can now start creating cues in your lighting system.


![Alt text](imgs/LightingFixtures.jpg)
![Alt text](imgs/LightingCue.jpg)


OSC connection:\
Select Gear > In and Out > OSC > Enable Input (should light up yellow)
Set, receive, receive command & echo input switch to “Yes”


![Alt text](imgs/MA3OSC.PNG)


Interface set to laptop IP address
Set prefix to “gma3”
Set Page to “Page1”
Destination IP set to 2 port node IP address


![Alt text](imgs/ChooseSystemMonitor.PNG)


On the main page, click on the blank space > Add window > All > type system monitor and select it


![Alt text](imgs/SystemMonitor.PNG)


Cross check system monitor with Raspi
