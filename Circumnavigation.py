from qset_lib import Rover, AngleReader
from time import sleep
import signal

right_side_speed = 0
left_side_speed = 0

def circumnavigate():
    right_side_speed = 1
    left_side_speed = -1

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    # This line allows for the KeyboardInterrupt to worl
    signal.signal(signal.SIGINT, signal.default_int_handler)

    while True:
        # the below lines iterate through all the laser scan lines and prints if the distance is less than 0.5 meters
        for dist in rover.laser_distances:
            # print(dist)
            if dist < 0.5:
                #circumnavigate()
                right_side_speed = 1
                left_side_speed = -1
                print("TOO CLOSE")
        # the below line sends a command to the rover (simulation) 
        rover.send_command(left_side_speed, right_side_speed)
        i = i + 1
        sleep(0.01)

if __name__ == "__main__":
    main()