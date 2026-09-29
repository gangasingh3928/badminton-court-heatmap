from ultralytics import YOLO
import csv

model = YOLO("yolov8n.pt")

file=open("player_positions.csv","w",newline="")
writer=csv.writer(file)

writer.writerow(["frame","x","y"])

results=model.track(source="videos/rally.mp4", show=True, conf=0.5,)
frame=0

for result in results:
    if result.boxes is not None:
        for box,track_id in zip(result.boxes, result.boxes.id):

            if int(track_id)==1:

                x1,y1,x2,y2=box.xyxy[0]
                x=int((x1+x2)/2)
                y=int((y1+y2)/2)

                writer.writerow([frame,x,y])
    frame += 1

file.close()
print("saved")