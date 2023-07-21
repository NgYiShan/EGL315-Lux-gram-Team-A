# EGL315-Lux-gram-Team-A

# QL1 audio mixing

## QL1 setup

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