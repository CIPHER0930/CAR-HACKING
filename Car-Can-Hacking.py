import tkinter as tk
import threading
import time

# Set the CAN interface
CAN_INTERFACE="can0"

# Get the current CAN bus ID
CAN_ID=$(caninfo -i $CAN_INTERFACE)

# Function to send a CAN message to control the car
def cansend_car(message):
    cansend -i $CAN_INTERFACE $CAN_ID "$message"

# Function to send a Bluetooth command to control the car
def bluetooth_command(command, device_name=None):
    if device_name is None:
        # Discover Bluetooth devices
        devices = bluetoothctl scan on | grep -oP '(?<=Device )([0-9a-fA-F:]+)'

        # If no devices were found, exit
        if len(devices) == 0:
            print("No Bluetooth devices found")
            exit(3)

        # Select the first device in the list
        device_name = devices[0]

    bluetoothctl connect "$device_name"
    bluetoothctl send "$command"
    bluetoothctl disconnect "$device_name"

# Example CAN messages to control the car
# Lock the car doors
# cansend_car 0x100 0x01 0x01

# Unlock the car doors
# cansend_car 0x100 0x01 0x02

# Turn on the windshield wipers
# cansend_car 0x200 0x01 0x01

# Turn off the windshield wipers
# cansend_car 0x200 0x01 0x02

# Example Bluetooth commands to control the car
# Play the next track on the stereo system
# bluetooth_command "Play"

# Pause the music on the stereo system
# bluetooth_command "Pause"

# Increase the volume on the stereo system
# bluetooth_command "VolumeUp"

# Decrease the volume on the stereo system
# bluetooth_command "VolumeDown"

class CarGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Car Control GUI")

        # Steering wheel
        self.steering_wheel = tk.Canvas(self.root, width=200, height=200)
        self.steering_wheel.create_oval(10, 10, 190, 190, fill="black")
        self.steering_wheel.create_line(100, 100, 100, 50, width=5, arrow=tk.LAST)
        self.steering_wheel.bind("<Motion>", self.on_steering_wheel_move)
        self.steering_wheel.pack()

        # Other GUI interfaces
        # ...

        self.root.mainloop()

    def on_steering_wheel_move(self, event):
        # Calculate the steering angle
        steering_angle = (event.x - 100) / 50

        # Send the CAN message to control the steering wheel
        cansend_car(0x300 0x01 steering_angle)

        # Update the steering wheel position
        self.steering_wheel.create_line(100, 100, 100, 100 - steering_angle, width=5, arrow=tk.LAST)

def main():
    # Create the GUI
    car_gui = CarGUI()

if __name__ == "__main__":
    main()
