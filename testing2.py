from qset_lib import Rover, AngleReader
from time import sleep
import signal

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    # This line allows for the KeyboardInterrupt to worl
    signal.signal(signal.SIGINT, signal.default_int_handler)
    i = 0

    left_side_speed = 0
    right_side_speed = 0
    isTooClose = False
    for dist in rover.laser_distances:
        print(dist)
    try:
        while not isTooClose or True:
          
            # this line prints the current location and heading of the rover
            
            # the below lines iterate through all the laser scan lines and prints if the distance is less than 0.5 meters
           
                if dist < 0.5:
                    
                    left_side_speed = 0
                    right_side_speed = 0
                    isTooClose = True
                    break
            # the below line sends a command to the rover (simulation) 
            rover.send_command(left_side_speed, right_side_speed)
            i = i + 1
            sleep(1)

    except KeyboardInterrupt:
        pass

    rover.send_command(0, 0)

if __name__ == "__main__":