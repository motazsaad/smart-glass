# Peace Ear Smart Glasses, a graduation project by Nadia Zoheer Khatib 

# [PeaceEar SmartGlasses](https://github.com/NadiaKhatib/smart-glass)
PeaseEar is Linux-based system software designed to run on wearable devices with attachment to a pair of glasses that provides a real-time transcription of the words being spoken so that it allows Deaf people to ability to engage in a naturally flowing conversation.

## Pre-requisites / device setup
To use and develop PeaceEar, we will need to setup a proper base environment with the required hardware. You will need:

• A Raspberry Pi with the latest Raspbian installed on a minimum 4GB SD card. All Pi models work.

• A small, monochrome OLED display. (Currently only supports 'SSD1306 128x64' OLED displays.)

• A microphone module out of a broken headset, soldered onto a small USB soundcard board.


## Installation
Let's get down to installing PeaceEar. To make things easier, PeaceEar has its own simple first-time setup and configuration. You will need your Pi to be connected to a working internet connection. **The first-time setup removes a lot of pre-installed software from the standard Raspbian image, so it's best to install PeaceEar on a clean image to prevent any loss of data**


#### Step One: Cloning PeaceEar from the official GitHub.
The first thing we need to do is to clone PeaceEar from the GitHub repository. This can be done simply by entering the following command into the terminal:
> git clone https://github.com/NadiaKhatib/smart-glass.git


#### Step Two: Entering the PeaceEar src directory.
Now that we've cloned the repository, lets enter our newly-created local directory.
> cd smart-glass

We need to go deeper to access the main source file, 'OledSpy.py', which is located in the src directory.
> cd src


#### Step Three: Starting the first-time setup.
When we start 'OledSpy.py' with 'sudo' rights, the terminal will be cleared and first-time setup's dialog will be displayed. The setup begins about 20 seconds after the dialog is shown, and takes a *very long time* to complete. Once setup is complete, the Pi will reboot and PeaceEar should start to capture sound and displaying on the connected OLED display.

You can start the setup by entering:
> sudo python3 OledSpy.py

**MAKE SURE ITS RUN WITH 'sudo python3' AND NOT WITH 'python'!**


# Abstract 
Individuals who are Deaf or hard of hearing can experience trouble completing basic daily tasks such as interacting with others. Although some solutions are used to deal with this, they have a lot of flaws. Where lip reading can be used, but only to understand about 30% of the spoken words, although there are sign language interpreters, they are few, and this deficiency is expected to worsen as these individuals enter public situations more often. These problems are partly responsible for the high unemployment rate and the existence of problems such as depression and anxiety in the deaf community.In this project, we design smart glasses that are assistive technology for people with hearing disabilities to help us understand what is going around them and the possibility of coexistence and interaction with the other worlds. The glasses are able to provide accurate real-time speech transcription and properly format it onto its display. When worn, they are attached to a regular pair of glasses, where are compatible with any eyeglass prescription the wearer may have. Overall, the device is highly effective and is able to achieve its purpose. where The program detects when a person is speaking by analyzing the energy levels (the sound intensity) of the stream of audio coming from the microphone.and then the program is analyzing the audio from the microphone, it is changed based on the current level of ambient noise. This allows the program to adapt to the situation the wearer of the glasses is in. We use the prototyping methodology to develop this project because the product requirements are not clearly understood, unstable, and change rapidly. This project will have a major impact on people with hearing disabilities, as it will help them to communicate effectively with friends and members of society, contribute to raising their awareness and improving their educational and cultural level, and also works to increase their productivity and participation in all fields, and helps encourage community members to speak with people with hearing disabilities and participate in with them.


# Demo 
https://youtu.be/88c4ylL4k0c 

