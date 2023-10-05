# CAR-HACKING

# Car Hacking Project
git clone https://github.com/CIPHER0930/CAR-HACKING
cd CAR-HACKING

This project contains scripts for hacking and controlling a car.

## Scripts

* `CAR-CONTROL.sh`: This script allows you to send CAN messages and Bluetooth commands to control the car.
* `Car-can-hacking.py`: This script provides a GUI for controlling the car.

## Usage

To use the scripts, you will need to have a CAN interface connected to your computer. You can also use a Bluetooth adapter to control the car wirelessly.

To run the `CAR-CONTROL.sh` script, simply execute the following command:

Use code with caution. Learn more
./CAR-CONTROL.sh


You can then use the following commands to control the car:

cansend_car 0x100 0x01 0x01 # Lock the car doors
cansend_car 0x100 0x01 0x02 # Unlock the car doors
cansend_car 0x200 0x01 0x01 # Turn on the windshield wipers
cansend_car 0x200 0x01 0x02 # Turn off the windshield wipers

bluetooth_command "Play" # Play the next track on the stereo system
bluetooth_command "Pause" # Pause the music on the stereo system
bluetooth_command "VolumeUp" # Increase the volume on the stereo system
bluetooth_command "VolumeDown" # Decrease the volume on the stereo system


To run the `Car-can-hacking.py` script, simply execute the following command:

python Car-can-hacking.py

You can then use the GUI to control the car.

Warning
Please be careful when using these scripts. Hacking a car can be dangerous and could cause damage to the car or its occupants.
