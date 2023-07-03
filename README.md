# MoodMirror
DISC-Project by Andreas Neumüller and Simon Laubis

## Project description?
The goal is to give users visual feedback on their emotions 
and encourage them to reflect on themselves. The mirror 
uses a camera to capture the user's face. The detected
emotion is displayed on the mirror. The MoodMirror responds 
with appropriate advice and sentences based on the detected 
emotion to encourage the user to reflect on his emotional 
state. The project involves designing and building
a prototype with facial recognition, emotion analysis and
user interface. 

## How does it work?
Connect the mirror to the power supply. After about half 
a minute, the mirror is ready to use. Position the mirror 
so that the upper part of the body and the face are clearly
and completely visible in the center of the mirror. After 5 
seconds of continuous recognition of the face, the analyzed
emotion is displayed on the surface with an advice.

## Components 

We were asked by the carrier to place our order with
the Conrad company. We decided to order a [Raspberry 
Pi StarterKit](https://www.conrad.de/de/p/raspberry-pi-rb-set-4-4-raspberry-pi-4-b-4-gb-4-x-1-5-ghz-inkl-netzteil-inkl-noobs-os-inkl-hdmi-kabel-inkl-geh-2765999.html) which includes the Raspberry Pi,
case, heatsink, micro-HDMI cable, power cable and 
micro-SD card. [What is a Raspberry Pi?](https://de.wikipedia.org/wiki/Raspberry_Pi)

### Hardware 
- [Raspbeery Pi 4 B](https://www.reichelt.de/raspberry-pi-4-b-4x-1-5-ghz-4-gb-ram-wlan-bt-rasp-pi-4-b-4gb-p259920.html?&trstct=vrt_pdn&nbc=1) (8GB RAM)
- [Raspbeery Pi Camera Module 3](https://www.reichelt.com/raspberry-pi-kamera-12mp-76-v3-rasp-cam-3-p339256.html?CCOUNTRY=445&LANGUAGE=de&utm_source=display&utm_medium=rsp-foundation&src=raspberrypi&&r=1) 
- Raspbeery Pi power supply
- Micro-HDMI cable
- SD-Karte (32GB)
- Screen in size of the desired mirror size, we used a 28'' PC monitor for our prototype

### Software

- [OpenCV](https://opencv.org) for face detection  
- [deepFace](https://github.com/serengil/deepface) for emotion analysis 

  
## Research
### Pi OS
To start the project, we decided to use the recommended standard 
operating system (Raspberry Pi OS 32 Bit Debian Bullseye), 
since there are many options. We were able to get
off to a good start with this operating system. In the course of 
the project it turned out that the Raspberry Pi OS (64 bit) Debian
Bullseye is recommended by us. The biggest advantage is that the
installation of the OpenCV library takes only a fragment of the
time (about 5 min) that it took with the 32Bit version (min 2h)
of the operating systems.

We used the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) 
to upload the image to the memory card.The program offers a clear user
interface, the possibility to choose different operating system
images, pre-configure them and install them.
### Programm Language

When using AI models, there is no way around Python.
In addition, [Python](https://www.python.org) is one of the most popular languages 
for programming on the Raspberry Pi. The Pi OS already offers
two editors out of the box (Geany & Thonny). Furthermore,
the language offers a large number of libraries and resources
and is relative easy to learn.

For the interface we decided to use html with css and java script. 

[HTML](https://de.wikipedia.org/wiki/Hypertext_Markup_Language) 
(Hypertext Markup Language) defines the basic structure 
of a web page. It allows the creation of content, layouts and 
the organization of elements on the user interface.

[CSS](https://de.wikipedia.org/wiki/Cascading_Style_Sheets) 
(Cascading Style Sheets) allows to determine the design of, 
among other things, HTML pages. Using simple instructions, web 
page elements such as layout, color, and typography can be customized
as desired.

[JavaScript](https://de.wikipedia.org/wiki/JavaScript) is used to create interactive web pages. JavaScripts 
can be integrated into HTML files. Here more logic can happen like
reading information and updating page content as in our case.
### Face Detection
### Emotion Analysis
### Interface 

## Setup instructions
### Hardware Setup

There is not much to do for the hardware setup of the Raspberry Pi.
Take the included heatsinks out of the package and stick them on the 
intended components (Position 1-4). To ensure an even better heat conduction, we would recommend an active cooling with a fan. There are many cases for Raspberry Pi's with integrated fans.

![Heatsinks Position](/assets/Pi.jpg)

Once that's done, all you have to do is plug in the camera and you're
ready to go. Lift the locking clip of the CSI module a little bit
and plug in the cable (make sure that the bare pins point in the opposite
direction to the clip), to fix it just push the clip back a little bit. 

### Os Setup
You will need a microSD card to install the operating system. This should be at least 8GB in size. We use the delivered 32GB card in our project.Connect the card with an appropriate adapter to your PC and start the [Raspberry Pi Imager](https://www.raspberrypi.org/software/).

Under the Operating System tab, under Raspberry Pi OS (other), select the 64-bit Raspberry Pi OS Debian Bullseye version. Select your SD card. At the cogwheel you can make further settings like enable SSH, set username and password, set up Wifi and define language settings. These advanced settings can also be changed later. Now just press write and confirm. After the installation is complete, plug the card into the Raspberry Pi, connect the screen, mouse, keyboard and connect the power. If you have already specified all the settings in the Pi imager, you should now be on the desktop. 

### Software Setup
First open the terminal and use these commands to ensure that the operating system and all installed packages are up to date.
  ```bash
    sudo apt-get update
    sudo apt-get upgrade
   ```

Install Open CV:
  ```bash
  sudo apt install python3-opencv
  ```

To check if the insterlation is successful you can open python then import opencv and get the version output:
  ```bash
  python3
 ```
 ```python
  >>> import cv2
  >>> cv2.__version__
  >>> quit()
```
Install Deepface:
```bash
pip install deepface
```
To check the installation you can open python on the terminal an try to import deepface:
  ```python
  >>> from deepface import DeepFace
  ```

### Clone Repo
It is only possible to clone the repo with authorization. Please contact neumuelleran87784@th-nuernberg.de if you are interested.
  ```bash
  git clone https://git.informatik.fh-nuernberg.de/<user-name>/magicmirror.git
  ```
Enter your username and password and confirm.The repository should be now cloned to your current directory.

### Setup Autostart
To enable the automatic launch of our programs we need to create a configuration file. You need to edit this text file:
  ```
  sudo nano ~/.config/lxsession/LXDE/autostart
  ```
Paste in these lines of code:
  ```bash
  @lxpanel --profile LXDE-pi
  @pcmanfm --desktop --profile LXDE-pi
  @lxterminal -e python /home/pi/magicmirror/mm.py
  @xscreensaver -no-splash
  @chromium-browser --kiosk --allow-file-access-from-files /home/pi/magicmirror/index.html
  @sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/chromium/Default/Preferences
  @xset s off
  @xset -dpms
  @xset s noblank
  ```
To save and exit the nano editor press CTRL-X, Y and then ENTER.
Once your configuration file has been updated you are ready to test.
  ```bash
  startx
   ```
The LXDE desktop should load and start the chromium-broswer with the index.html and the mm.py script

### Turn Monitor
For our mirror we took a monitor on the upright. To rotate the screen you have to make a configuration in the boot config. **It is important not to make any mistakes when editing this file**, otherwise the Raspberry Pi may not boot.
  ```bash
  sudo nano /boot/config.txt
  ```
Add this line to the end of the file:
```txt
display_rotate=1
```
To save and exit press CTRL-X, Y and then ENTER. Now you only have to reboot and the **MoodMirror** is ready to use. 
  ```bash
  reboot
  ``
Have fun!
