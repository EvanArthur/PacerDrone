import matplotlib.pyplot as plt
import csv
import ast
import numpy as np

x=[]
y=[]
z=[]

with open('curveData.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    next(plots)
    next(plots)
    for row in plots:
        # print(row[0])
        row = ast.literal_eval(row[0])
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

t = np.arange(0, 335*2)
# t = np.arange(0, 335)
# z = z[175:]+z[:175]
z = z + z
t = t*0.5899705015
# print(z)
# plt.plot(t,x, marker='o')
# plt.plot(t,y, marker='x')
plt.plot(t,z, marker='.')

plt.title('Radius from Computer Vision')

plt.xlabel('Distance from Track Start (meters)')
plt.ylabel('Detected Curve Radius (meters)')

plt.savefig("ReportPhotos/cv_radii.png")
plt.show()
