import matplotlib.pyplot as plt
import numpy as np

# x is meters
# y is radius at that point

radius1 = 27.082
radius2 = 40.022
angle1 = 53
angle2 = 74

def arc(radius, angle):
    distance = (2*np.pi*radius) * (angle/360)
    return distance

def f(x):
    if x <= segment1:
        return radius1
    elif segment1 < x <= (segment1 + segment2):
        return radius2
    elif (segment1 + segment2) < x <= ((2*segment1 + segment2)):
        return radius1
    elif (2*segment1 + segment2) < x <= ((2*segment1 + segment2) + straight):
        return 0
    elif ((2*segment1 + segment2) + straight) < x <= ((3*segment1 + segment2) + straight):
        return radius1
    elif ((3*segment1 + segment2) + straight) < x <= ((3*segment1 + 2*segment2) + straight):
        return radius2
    elif ((3*segment1 + 2*segment2) + straight) < x <= ((4*segment1 + 2*segment2) + straight):
        return radius1
    elif ((4*segment1 + 2*segment2) + straight) < x <= 400:
        return 0


segment1 = arc(27.082, 53)
segment2 = arc(40.022, 74)
straight = 97.265

t = np.arange(0, 400)

plt.plot(t, list(map(f, t)), 'b-')

plt.show()