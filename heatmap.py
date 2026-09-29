import csv
import matplotlib.pyplot as plt
x_values = []
y_values = []
with open('player_positions.csv', 'r') as file:
    data=csv.DictReader(file)
    for row in data:
        x_values.append(int(row['x']))
        y_values.append(int(row['y']))

plt.hist2d(x_values,y_values,bins=50)

plt.title("Heatmap of Player Positions")
plt.xlabel("X Position")
plt.ylabel("Y Position")

plt.colorbar(label='Number of Visits')
plt.savefig("heatmap.png")
plt.show()