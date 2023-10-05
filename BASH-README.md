# CAR-HACKING


Bash script for controlling a car using CAN bus and Bluetooth

This script provides a set of functions to control a car using CAN bus and Bluetooth. The functions can be used to lock and unlock the doors, turn on and off the windshield wipers, play and pause music on the stereo system, control the volume, and control the steering wheel.

To use the script:

Install the cansend and bluetoothctl packages:
sudo apt install cansend bluetoothctl
Set the CAN interface and get the current CAN bus ID:
CAN_INTERFACE="can0"
CAN_ID=$(caninfo -i $CAN_INTERFACE)
Call the desired function with the desired CAN message or Bluetooth command. For example, to lock the car doors, you would call the cansend_car() function with the following arguments:
cansend_car 0x100 0x01 0x01
To play the next track on the stereo system, you would call the bluetooth_command() function with the following arguments:

bluetooth_command "Play"
You can also specify the Bluetooth device name as the second argument to the bluetooth_command() function. If no Bluetooth device name is specified, the script will discover Bluetooth devices and select the first one.

Example usage:

# Lock the car doors
cansend_car 0x100 0x01 0x01

# Unlock the car doors
cansend_car 0x100 0x01 0x02

# Turn on the windshield wipers
cansend_car 0x200 0x01 0x01

# Turn off the windshield wipers
cansend_car 0x200 0x01 0x02

# Play the next track on the stereo system
bluetooth_command "Play"

# Pause the music on the stereo system
bluetooth_command "Pause"

# Increase the volume on the stereo system
bluetooth_command "VolumeUp"

# Decrease the volume on the stereo system
bluetooth_command "VolumeDown"

# Turn the wheel 10 degrees to the left
control_steering -10

# Turn the wheel 10 degrees to the right
control_steering 10
Safety guidelines

Make sure that the script is properly tested and validated before using it in a real-world setting.
Be aware of the limitations of CAN bus and Bluetooth communication. These technologies can be susceptible to interference and other problems.
Use caution when controlling the car's steering wheel. A small mistake can lead to serious consequences.
Be aware of your surroundings and always be prepared to take over manual control of the car if necessary.
