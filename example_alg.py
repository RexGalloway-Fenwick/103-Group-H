from qset_lib import Rover, AngleReader
from time import sleep
import signal
import numpy
import math

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    # This line allows for the KeyboardInterrupt to worl
    signal.signal(signal.SIGINT, signal.default_int_handler)
    i = 0

    desiredX = 10
    desiredY = -10
    desiredM = desiredY/desiredX
    desiredAngle = numpy.arctan(desiredX/desiredY)*180/math.pi
    print(desiredAngle)

    while rover.heading - desiredAngle > 0.5 or rover.heading - desiredAngle < -0.5:
        print(angle_reader.read_angle - desiredAngle)
        left_side_speed = 1
        right_side_speed = -1
        rover.send_command(left_side_speed, right_side_speed)

    
    left_side_speed = 4
    right_side_speed = 4
    rover.send_command(left_side_speed, right_side_speed)

    isTooClose = False
    while not isTooClose:
        for dist in rover.laser_distances:
            if dist < 0.75:
                left_side_speed = 0
                right_side_speed = 0
                rover.send_command(left_side_speed, right_side_speed)
                isTooClose = True
                break


    left_side_speed = -1
    right_side_speed = 1
    rover.send_command(left_side_speed, right_side_speed)


    rotatedEnough = False
    while not rotatedEnough:
        if all(dist > 5 for dist in rover.laser_distances[1:29]):
            left_side_speed = 0
            right_side_speed = 0
            rover.send_command(left_side_speed, right_side_speed)
            rotatedEnough = True


    left_side_speed = 3
    right_side_speed = 2
    rover.send_command(left_side_speed, right_side_speed)

    sleep(1000)

    goodSlope = False
    while not goodSlope:
        if desiredM - rover.y/rover.x < 0.5:
            left_side_speed = 0
            right_side_speed = 0
            rover.send_command(left_side_speed, right_side_speed)
            goodSlope = True





    tooClose = False
    while not tooClose:
        if any(dist < 5 for dist in rover.laser_distances):
            rotatedEnough = False
            while not rotatedEnough:
                if all(dist > 5 for dist in rover.laser_distances):
                    left_side_speed = -1
                    right_side_speed = 1
                    rover.send_command(left_side_speed, right_side_speed)







    isTooClose = False
    try:
        while not isTooClose or True:
            print(" ANGLE: " + str(angle_reader.read_angle))
            # this line prints the current location and heading of the rover
            print("X: " + str(rover.x) + " Y: " + str(rover.y) + " Heading: " + str(rover.heading))
            # the below lines iterate through all the laser scan lines and prints if the distance is less than 0.5 meters
            for dist in rover.laser_distances:
                if dist < 0.5:
                    print("TOO CLOSE")
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
    main()

