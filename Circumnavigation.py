from qset_lib import Rover, AngleReader
from time import sleep
import signal

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    # This line allows for the KeyboardInterrupt to worl
    signal.signal(signal.SIGINT, signal.default_int_handler)

    right_side_speed = 1
    left_side_speed = 1
    try:
        while True:
            # the below lines iterate through all the laser scan lines and prints if the distance is less than 0.5 meters
            for dist in rover.laser_distances:
                # print(dist)
                if dist < 0.5:
                    print("TOO CLOSE")
                    right_side_speed = 1
                    left_side_speed = -1
                    for x in range(0,28):
                        print(x)
                        if rover.laser_distances[x] <= 2:
                            print("test")
                            break
                        if x >= 25:
                            print("test2")
                            right_side_speed = 0
                            left_side_speed = 0

            # the below line sends a command to the rover (simulation) 
            rover.send_command(left_side_speed, right_side_speed)
            sleep(0.01)
    except KeyboardInterrupt:
        pass

    rover.send_command(0, 0)


if __name__ == "__main__":
    main()