from qset_lib import Rover, AngleReader
from time import sleep
import signal

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    # This line allows for the KeyboardInterrupt to worl
    signal.signal(signal.SIGINT, signal.default_int_handler)

    #Variable declaration
    right_side_speed = 1
    left_side_speed = 1
    rover.send_command(left_side_speed, right_side_speed)


    try:
        #Main loop
        while True:
            # the below lines iterate through all the laser scan lines and prints if the distance is less than 0.5 meters
            for dist in rover.laser_distances:
                # print(dist)
                if dist < 0.5:
                    print("TOO CLOSE")
                    right_side_speed = 1
                    left_side_speed = -1
                    break
                
            # Make sure the laser distances array is populated
            if len(rover.laser_distances) > 0: 
                #Stop if the last few lasers are the only ones that register the obstacle (check the last few for consistency)
                for i in range(28, 1 , -1): #Lasers 1-28 are the ones that work
                    print(i)
                    if rover.laser_distances[i] < 5:
                        break
                    if i == 3: 
                        right_side_speed = 1
                        left_side_speed = 1

            # the below line sends a command to the rover (simulation) 
            rover.send_command(left_side_speed, right_side_speed)
            sleep(0.01)
    except KeyboardInterrupt:
        pass

    #stop the rover's movement when the program ends
    rover.send_command(0, 0)


if __name__ == "__main__":
    main()