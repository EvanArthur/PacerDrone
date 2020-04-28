from djitellopy import Tello
import math
import time

def flyCurve(tello, r, speed):
    yaw = int(speed*180/(r*math.pi))
    print("yaw is: ", yaw)

    tello.send_rc_control(0, speed, 0, yaw)


def main():
    # CONNECT TO TELLO
    me = Tello()
    me.connect()
    me.for_back_velocity = 0
    me.left_right_velocity = 0
    me.up_down_velocity = 0
    me.yaw_velocity = 0
    me.speed = 0

    print(me.get_battery())

    me.streamoff()
    me.streamon()
    ########################

    me.takeoff()
    flyCurve(me, 160, 50)
    time.sleep(5)
    me.land()

if __name__ == "__main__":
    main()
    