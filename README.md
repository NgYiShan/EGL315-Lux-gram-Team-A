# EGL315-Lux-gram-Team-A

# Set up guide to create a pepper's ghost

## Hardware

To know what items are required for this setup, please read the BOM listed below.

1. 1x Projector Epson EB-PU2010B
2. 1x Network Switch Cisco SG1100D-08HP
3. 1x Audio Mixer Yamaha QL1
4. 1x MA3 2 Port Node
5. 1x Media Server
6. 3x Laptop Hp Zbook G5 15
7. 2x Spot MH Ayrton Mistral
8. 1x SaCN to DMX converter Luminex Luminode 4
9. 1x Audio Amplifier Kramer 914
10. 2x Passive speakers Mackie CR4
11. 1x Active Subwoofer Adam Sub10 
12. 1x Hinged acrylic 80cm x 110cm  
13. 3x White polyfoam 270cm x 120cm x 0.5cm
14. 2x Ayrton MagicBlade
15. 1x Ayrton MiniPanel

## Required Softwares and Licenses

1. Christie's Pandoras Box
2. Pandora Server Management
3. Pro tools
4. Dante Virtual Soundcard
5. Dante Controller
6. grandMA3 v1.9.3.3
7. Dongle for pandora licensing
8. Dongle for Pro Tools licensing

## Set up

### **Pepper's ghost set up**
![Alt text](imgs/setup_front2.jpg)

Using a sturdy and heavy enough frame, mount the projector to the underside of the frame, then angle the projector 10° towards the floor.

Then, at 100cm away, prop up the white polyfoam, and tilt it backwards to an angle of 68°.

Above the frame, place and open the acrylic, then secure it while angling it at 75°.

### **Video system set up**

![Alt text](imgs/pandora.jpg)

Connect 1 laptop to your media server via a LAN cable, then a HDMI cable to your projector set up previously.

Ensure the ip addresses for your laptop and media server are in the same subnet.

Connect the licensing dongle for Pandora to your laptop, then launch pandoras box on and server management.

On your media server, launch pandoras box, then enter fullscreen.

You can now start sending in content through your laptop to your media server.

### **Lighting system set up**

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


### **Audio System set up**
You can use any audio playback engine you are comfortable with but in this setup we used ProTools

1. Patching your outputs. 
- In our case we used OMNI 6-8. Assigning a mix to each.(OMNI6&7 being the tops and OMNI8 being our sub-woofer)
![Alt text](imgs/speakeroutputpatch.jpeg)

1_1. Start by patching an amplifier in your QL1, then connecting two passive speakers into the amplifier.


![Alt text](imgs/audio/amp.jpg)


1_2. Then, patch a subwoofer in your QL1.

2. Removing redundant frequencies
- for the top speakers:

2_1. Using eq, reduce the gain on the low frequencies at around 40Hz to -ve infinity


![Alt text](imgs/speakereq.jpeg)

- for the sub-woofer:

2_2. Using eq, reduce the gain on the frequencies > 500 and <20 to -ve infinity.


![Alt text](imgs/subwoofereq.jpeg)


3. Connect to Dante
- Ensure the ip addresses for your laptop and QL1 are in the same subnet.

3_1. Connect 1 laptop to your Yamaha QL1 via a LAN cable.

3_2. Go to 'I/O DEVICE' then 'SETUP', select 'DAISY CHAIN' and 'THIS CONSOLE'.
![Alt text](imgs/dantesetup.jpeg)

3_3. Go to 'SETUP' then 'DANTE SETUP', then select 'DANTE INPUT PATCH'. select the input accordingly.
![Alt text](imgs/danteinputpatch.jpeg)

4. angling of tops(to make sure there's no phasing)
- angle at 30 degrees towards the auidence
![Alt text](imgs/setup_side.jpg)

### **Audio Software set up**
Connect the licensing dongle for Pro Tools to your laptop, then launch Pro Tools, Dante Virtual Soundcard and Dante controller.

1. Connect dante to QL1.
1_1. open the application and Press 'Start'.


![Alt text](imgs/audio/DVSstart.jpg)

1_2. Select the dante channels such that they match with the patching you did on the QL1.


![Alt text](imgs/audio/danteController.png)

2.Importing your audio tracks into ProTools.
2_1. Select the 'File' Dropdown menu and then select 'Import' --> 'Audio'.


![Alt text](imgs/audio/protools_import_audio.jpg)

2_2. After importing the tracks window should look like this.


![Alt text](imgs/Audio/audioSoftSetup1.jpg)

3. Setting up Dante output to QL.
3_1. Go to the 'Setup' Dropdown menu and select I/O.


![Alt text](imgs/audio/IOdropdownmenu.png)

3_2. Add Stereo Dante Outputs according to how many tracks you need.


![Alt text](imgs/audio/IOsetup.png) 

4. Stereo busing
4_1. go to setup on QL1 and make your output mix/matrixes stereo.


![Alt text](imgs/bussetup.jpeg)
