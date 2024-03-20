from qset_lib import Rover, AngleReader
from time import sleep
import signal

rover = Rover() # this line starts the connection to the rover and gives access to the rover data
angle_reader = AngleReader()

def perpCheck():
    # Make sure the laser distances array is populated
    if len(rover.laser_distances) > 0: 
        #Stop if the last few lasers are the only ones that register the obstacle (check the last few for consistency)
        for i in range(28, 1 , -1): #Lasers 1-28 are the ones that work
            if rover.laser_distances[i] < 1:
                break
            if i == 3: 
                rover.send_command(0, 0)
                return True
            
def distCheck(distance):
    for dist in rover.laser_distances: 
        if dist < distance:
            print("TOO CLOSE")
            return 1
        
def circumnavigate():
    #start circumnavigating by getting parallel to the obstacle
    while True:        
            if perpCheck():
                break
            rover.send_command(-1, 1) #Turn left
            sleep(0.01)
    while True:
        rover.send_command(2, 2)
        if distCheck(0.5):
            circumnavigate()
    return

def main():
    # This line allows for the KeyboardInterrupt to worl
    signal.signal(signal.SIGINT, signal.default_int_handler)

    #Variable declaration
    rover.send_command(1, 1)

    try:
        while True:
            # the below lines iterate through all the laser scan lines and prints if the distance is less than 0.5 meters
            if distCheck(0.5):
                break

            rover.send_command(2,2)
            sleep(0.01)

        circumnavigate()

    except KeyboardInterrupt:
        pass

    #stop the rover's movement when the program ends
    rover.send_command(0, 0)


if __name__ == "__main__":
    main()