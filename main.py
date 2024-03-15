from qset_lib import Rover, AngleReader
from time import sleep
import signal

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()


    left_side_speed = 0
    right_side_speed = 0
    while True:

        if rover.laser_distances[18] > 0.5 and rover.laser_distances[19] > 0.5 and rover.laser_distances[20] > 0.5:
            while rover.laser_distances[18] > 0.5 and rover.laser_distances[19] > 0.5 and rover.laser_distances[20] > 0.5:
                left_side_speed = 1
                right_side_speed = -1
                rover.send_command(left_side_speed, right_side_speed)
                print("Too close to left side")


        if rover.laser_distances[14] < 0.5 and rover.laser_distances[15] < 0.5 and rover.laser_distances[16] < 0.5 and rover.laser_distances[10] < 2:
            while rover.laser_distances[14] < 0.5 and rover.laser_distances[15] < 0.5 and rover.laser_distances[16] < 0.5:
                left_side_speed = -1
                right_side_speed = 1
                rover.send_command(left_side_speed, right_side_speed)
                print("Too close to left side")

