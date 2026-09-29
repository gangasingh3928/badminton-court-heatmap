import cv2
video = cv2.VideoCapture("videos/rally.mp4")
if not video.isOpened():
    print("Error: Could not open video file")
    exit()
while True:
    success,frame=video.read()
    if not success:
        break

    cv2.imshow("badminton",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()




