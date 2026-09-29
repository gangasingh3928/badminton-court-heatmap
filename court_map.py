import csv
import cv2
import numpy as np
import matplotlib.pyplot as plt

source_point=np.float32([[85,254],[564,215],[839,274],[429,469]])

court_width=610
court_heiight=1340
destination_point=np.float32([[0,0],[court_width,0],[court_width,court_heiight],[0,court_heiight]])

matrix=cv2.getPerspectiveTransform(source_point,destination_point)

x_values=[]
y_values=[]

with open("player_positions.csv","r") as file:

    data=csv.DictReader(file)

    for row in data:
        x_values.append(float(row["x"]))
        y_values.append(float(row["y"]))

camera_points=np.float32(list(zip(x_values,y_values))).reshape(-1,1,2)

court_points=cv2.perspectiveTransform(camera_points,matrix)
print("Camera X range:", x_values and min(x_values), "to", x_values and max(x_values))
print("Camera Y range:", y_values and min(y_values), "to", y_values and max(y_values))
court_x=court_points[:,0,0]
court_y=court_points[:,0,1]
print("Number of points:", len(court_x))
print("X range:", court_x.min(), "to", court_x.max())
print("Y range:", court_y.min(), "to", court_y.max())
print("First 10 points:", list(zip(court_x, court_y))[:10])

plt.figure(figsize=(7,12))

plt.hist2d(court_x,court_y,bins=30)

plt.colorbar(label="Number of points")

plt.scatter(court_x,court_y,s=40,color="red",zorder=10)

plt.plot([0,court_width],[court_heiight/2,court_heiight/2])

plt.plot([0,court_width],[472,472])

plt.plot([0,court_width],[868,868])

plt.plot([46,46],[0,court_heiight])

plt.plot([564,564],[0,court_heiight])

plt.title("Badminton Court Heatmap")

plt.xlabel("court width")
plt.ylabel("court length")

plt.xlim(0,court_width)
plt.ylim(court_heiight,0)

plt.savefig("badminton_heatmap.png")

plt.show()

print("badminton created")