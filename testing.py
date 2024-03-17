from qset_lib import Rover, AngleReader
from time import sleep
import signal

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    while True :
        i = 0
        for dist in rover.laser_distances:
            print(dist[i])
            i += 1

if __name__ == "__main__":
    main()