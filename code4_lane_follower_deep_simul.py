import cv2
import time
from deeptcar_deep_lane_detect import DTCDeepLaneDetect
from deeptcar_opencv_lane_detect import DTCOpencvLaneDetect

video_file = "./data/car_video.avi"

deep_detector = DTCDeepLaneDetect("./models/lane_navigation_final.h5")
cv_detector = DTCOpencvLaneDetect()
cap = cv2.VideoCapture(video_file)

prev_time = 0
curr_time  = 0

# skip first second of video.
for i in range(3):
    _, frame = cap.read()

try:
    i = 0
    while cap.isOpened():
        _, img_org = cap.read()
        
        lanes, img_lane = cv_detector.get_lane(img_org)
        angle_lane, img_lane = cv_detector.get_steering_angle(img_lane, lanes)
        
        prev_time = time.time()
        angle_deep, img_deep = deep_detector.follow_lane(img_org)
        curr_time = time.time()

        diff = angle_lane - angle_deep
        print(angle_deep, angle_lane, curr_time-prev_time)
        cv2.imshow("Deep Learning", img_deep)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
