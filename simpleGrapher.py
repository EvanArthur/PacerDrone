import matplotlib.pyplot as plt
import csv
import ast
import numpy as np

x=[]
y=[]
z=[]

with open('curveDataELI.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    next(plots)
    next(plots)
    for row in plots:
        print(row[0])
        row = ast.literal_eval(row[0])
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

t = np.arange(0, 341)

# plt.plot(t,x, marker='o')
# plt.plot(t,y, marker='x')
plt.plot(t,z, marker='.')

plt.title('Radius from Computer Vision')

plt.xlabel('Meters')
plt.ylabel('Radius')

plt.show()
