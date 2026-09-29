from ultralytics import YOLO
print("program started")

model = YOLO("yolov8n.pt")

results = model.track(source="videos/rally.mp4", show=True, conf=0.5)

print("Video finished")
for result in results:
    if result.boxes is not None:

        for box,track_id in zip(result.boxes, result.boxes.id):
            if int(box.cls[0])==0:
                print("Player id:",int(track_id))
print("donee!")