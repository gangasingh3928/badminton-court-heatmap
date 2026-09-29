from ultralytics import YOLO
model=YOLO("yolov8n.pt")
results=model.predict(source="videos/rally.mp4",show=True,conf=0.5)
print("Detection complete")

