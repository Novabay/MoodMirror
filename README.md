# MoodMirror
DISC-Project by Andreas Neumüller and Simon Laubis

## Project description?
The goal is to give users visual feedback on their emotions 
and encourage them to reflect on themselves. The mirror 
uses a camera to capture the user's face. After five seconds, 
the detected emotion is displayed on the mirror. It responds 
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
micro-SD card.

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
### Programm Language
### Face Detection
### Emotion Analysis
### Interface 

## Development

## Setup instructions
### Hardware Setup
### Os Setup
First use these commands to ensure that the operating system and all installed packages are up to date.
  ```bash
    sudo apt-get update
    sudo apt-get upgrade
   ```

 
### Library installation
### Clone Repo
### Setup Autostart



 Required software
 Start the application
 Test programm
