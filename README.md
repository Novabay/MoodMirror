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
- [Raspbeery Pi 4 B](https://www.reichelt.de/raspberry-pi-4-b-4x-1-5-ghz-4-gb-ram-wlan-bt-rasp-pi-4-b-4gb-p259920.html?&trstct=vrt_pdn&nbc=1) (4GB RAM)
- [Raspbeery Pi Camera Module 3](https://www.reichelt.com/raspberry-pi-kamera-12mp-76-v3-rasp-cam-3-p339256.html?CCOUNTRY=445&LANGUAGE=de&utm_source=display&utm_medium=rsp-foundation&src=raspberrypi&&r=1) 
- Raspbeery Pi power supply
- Micro-HDMI cable
- SD-Karte (32GB)
- Screen in size of the desired mirror size, we used a 28'' PC monitor for our prototype

### Software

- [OpenCV](https://opencv.org) for face detection  
- [deepFace](https://github.com/serengil/deepface) for emotion analysis 

### Features
- [x] AutoStart

### Planned/Ideas
- [ ] Interaktiv stuff

  
## Research
### Pi OS
To start the project, we decided to use the recommended standard 
operating system, since there are many options. We were able to get
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

## Development

## Setup instructions
### Hardware Setup

There is not much to do for the hardware setup of the Raspberry Pi.
Take the included heatsinks out of the package and stick them on the 
intended components.

![Heatsinks Position](/assets/Pi.jpg)

Once that's done, all you have to do is plug in the camera and you're ready to go. Lift the locking clip of the CSI module a little bit and plug in the cable (make sure that the bare pins point in the opposite direction with respect to the clip), to fix it just push the clip back a little bit. 

### Os Setup
[Raspberry Pi Image](https://www.raspberrypi.org/software/)

### Software Setup
First use these commands to ensure that the operating system and all installed packages are up to date.
  ```bash
    sudo apt-get update
    sudo apt-get upgrade
   ```
### Clone Repo
### Setup Autostart



 Required software
 Start the application
 Test programm
