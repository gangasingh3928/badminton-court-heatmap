from ultralytics import YOLO
model = YOLO("yolov8n.pt")
result=model.track(source="videos/rally.mp4", show=True, conf=0.5,)
for result in result:
    if result.boxes is not None:
        for box in result.boxes:
            if int(box.cls[0])==0:
                x1,y1,x2,y2=box.xyxy[0]
                x=int((x1+x2)/2)
                y=int((y1+y2)/2)
                print("position of player:",x,y)

print("donee!")                
