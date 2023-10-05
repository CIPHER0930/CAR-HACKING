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


##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


The script can control the steering wheel by sending CAN messages to the car's steering wheel control unit. The CAN message will specify the desired steering angle. The steering wheel control unit will then use this information to control the steering wheel.

To connect the script to the car's Bluetooth system, you can use the bluetooth_command() function to send a Bluetooth command to the car. The Bluetooth command will depend on the specific car model. For example, some cars may use the Bluetooth command AT+STEERING=<angle> to control the steering wheel angle.

Once the script is connected to the car's Bluetooth system, you can use the control_steering() function to send CAN messages to control the steering wheel. For example, to turn the wheel 10 degrees to the left, you would call the following function:

control_steering -10
To turn the wheel 10 degrees to the right, you would call the following function:

control_steering 10
It is important to note that controlling the steering wheel using Bluetooth is a safety-critical task. It is important to test the script thoroughly before using it in a real-world scenario. You should also be aware of the limitations of the script. For example, the script may not be able to control the steering wheel accurately at high speeds.

Here is an example of how to use the script to control the steering wheel using Bluetooth:

# Connect to the car's Bluetooth system
bluetooth_command "AT+STEERING=<angle>" "<device_name>"

# Control the steering wheel
control_steering -10

# Disconnect from the car's Bluetooth system
bluetooth_command "Disconnect" "<device_name>" 
########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

You can then use the GUI to control the car.

Warning
Please be careful when using these scripts. Hacking a car can be dangerous and could cause damage to the car or its occupants.
