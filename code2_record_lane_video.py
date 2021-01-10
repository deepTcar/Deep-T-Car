import cv2
from adafruit_servokit import ServoKit
from deeptcar_opencv_lane_detect import DTCOpencvLaneDetect
from deeptcar_car_motor_l9110 import DTCMotorL9110

servo = ServoKit(channels=16)
cv_detector = DTCOpencvLaneDetect()
motor = DTCMotorL9110()

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

cap = cv2.VideoCapture(0)
cap.set(3, SCREEN_WIDTH)
cap.set(4, SCREEN_HEIGHT)

# Below code works normally for Pi camera V2.1
# But for ELP webcam, it doesn't work.
#fourcc =  cv2.VideoWriter_fourcc(*'XVID')
fourcc =  cv2.VideoWriter_fourcc('M','J','P','G')

video_orig = cv2.VideoWriter('./data/car_video.avi', fourcc, 20.0, (SCREEN_WIDTH, SCREEN_HEIGHT))
#video_lane = cv2.VideoWriter('./data/car_video_lane.avi', fourcc, 20.0, (SCREEN_WIDTH, SCREEN_HEIGHT))
      
for i in range(3):
	_, frame = cap.read()
     
motor.motor_all_start(15)

while True:
	ret, img_org = cap.read()
	if ret:
		cv2.imshow('lane', img_org)
		video_orig.write(img_org)
		lanes, img_lane = cv_detector.get_lane(img_org)
		
		angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
		if img_lane is None:
			pass
		else:
			#video_lane.write(img_lane)
			
			print(angle)
			servo.servo[0].angle = angle
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		print("cap error")
		
motor.motor_all_stop()
cap.release()
video_orig.release()
#video_lane.release()
cv2.destroyAllWindows()
