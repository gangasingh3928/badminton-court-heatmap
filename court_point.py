import cv2
video = cv2.VideoCapture("videos/rally.mp4")
success,frame=video.read()

points=[]

def click_point(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        print("point:",x,y)

        cv2.circle(frame,(x,y),5,(0,225,0),-1)
        cv2.imshow("court",frame)

if success:
    cv2.imshow("court",frame)
    cv2.setMouseCallback("court",click_point)

    print("click the 4 corners")
    print("press esc to exit")

    while len(points)<4:
        cv2.waitKey(50)
    
    cv2.destroyAllWindows()
    
    print("points:",points)
    
else:
    print("Error: Could not read video frame")
    
video.release()