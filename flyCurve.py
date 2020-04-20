from djitellopy import Tello
import math
import time

def flyCurve(tello, r, speed):
    # try:
    #     print("Trying curve now")
    #     y = int(-1*math.sqrt(r/2) + r*math.sin(67.5*math.pi/180))
    #     print("y coord: ", y)
    #     x1 = int(math.sqrt(r/2) + r*math.cos(67.5*math.pi/180))
    #     print("X1 coord: ", x1)
    #     x2 = int(math.sqrt(r*2) + r*math.cos(67.5*math.pi/180))
    #     print("X2 coord: ", x2)

    #     tello.go_xyz_speed(x1, y, 0, speed)
    #     tello.go_xyz_speed(x2, y, 0, speed)
    # except Exception:
    #     print(Exception)
    #     tello.land()

    tello.send_rc_control(0, 25, 0, -50)
    time.sleep(5)

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
    flyCurve(me, 100, 20)
    me.flip_back()
    # time.sleep(5)
    me.land()

if __name__ == "__main__":
    main()
    