from qset_lib import Rover, AngleReader
from time import sleep
import signal

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    # Main program loop
    while True :
        for dist in rover.laser_distances:
            print(rover.laser__distances[dist])

if __name__ == "__main__":
    main()