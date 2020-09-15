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
