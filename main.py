from qset_lib import Rover, AngleReader
from time import sleep
import signal

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()


    left_side_speed = 1
    right_side_speed =

    while True:
        print








    """
    while True:

        if rover.laser_distances[28] > 0.5 and rover.laser_distances[29] > 0.5 and rover.laser_distances[30] > 0.5:
            while rover.laser_distances[28] > 0.5 and rover.laser_distances[29] > 0.5 and rover.laser_distances[30] > 0.5:
                left_side_speed = 1
                right_side_speed = -1
                rover.send_command(left_side_speed, right_side_speed)
                print("Too close to left side")


        if rover.laser_distances[24] < 0.5 and rover.laser_distances[25] < 0.5 and rover.laser_distances[26] < 0.5 and rover.laser_distances[15] < 2:
            while rover.laser_distances[24] < 0.5 and rover.laser_distances[25] < 0.5 and rover.laser_distances[26] < 0.5 and rover.laser_distances[15] < 2:
                left_side_speed = -1
                right_side_speed = 1
                rover.send_command(left_side_speed, right_side_speed)
                print("Too close to left side")


    """