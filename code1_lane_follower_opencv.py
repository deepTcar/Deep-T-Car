import cv2
from adafruit_servokit import ServoKit
from deeptcar_opencv_lane_detect import DTCOpencvLaneDetect
from deeptcar_car_motor_l9110 import DTCMotorL9110

cv_detector = DTCOpencvLaneDetect()
motor = DTCMotorL9110()
servo = ServoKit(channels=16)

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

cap = cv2.VideoCapture(0)
cap.set(3, int(SCREEN_WIDTH))
cap.set(4, int(SCREEN_HEIGHT))

# Car Speed, default 15
motor.motor_all_start(15)

while True:
	ret, img_org = cap.read()
	if ret:
		lanes, img_lane = cv_detector.get_lane(img_org)
		angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
		if img_angle is None:
			pass
		else:
			print(angle)
			servo.servo[0].angle = angle
			cv2.imshow("img_angle", img_angle)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			motor.motor_all_start(10)
			#motor.motor_all_stop()
			break
	else:
		print("cap error")
sleep(1000)
motor.motor_all_stop()
cap.release()
cv2.destroyAllWindows()
