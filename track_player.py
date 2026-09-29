from ultralytics import YOLO
import cv2
import csv
model = YOLO("yolov8n.pt")

video_path="videos/rally.mp4"

cap=cv2.VideoCapture(video_path)

with open("player_positions.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["x","y"])

    target_id=None

    while True:
        success,frame=cap.read()

        if not success:
            break

        results=model.track(frame, persist=True,conf=0.5,classes=[0])
        boxes=results[0].boxes

        if boxes is not None and len(boxes)>0:

            if boxes.id is not None:
                ids=boxes.id.cpu().numpy()
                coordinates=boxes.xyxy.cpu().numpy()

                if target_id is None:
                    target_id=int(ids[0])

                for player_id,box in zip(ids,coordinates):
                    if int(player_id) == target_id:

                        x1,y1,x2,y2=box
                        x=int((x1+x2)/2)
                        y=int(y2)
                        writer.writerow([x,y])

                        cv2.circle(frame,(x,y),8,(0,0,255),-1)
                        cv2.rectangle(frame,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),2)
                        cv2.putText(frame,"player",(int(x1),int(y1)-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
                        break

        cv2.imshow("Tracking",frame)
        if cv2.waitKey(1)==27:
            break

cap.release()
cv2.destroyAllWindows()

print("player tracking completed!")
print("player positions is created")
