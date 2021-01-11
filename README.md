# Deep-T-Car
Deep-T-Car stands for Deep learning, Detection and Training Car as an educational car for autonomous driving.
Using cameras and OpenCV, you can detect lanes and drive along roads, and you can also use Machine Learning technology to read through the camera and drive along the road.

### [Software required]
- OpenCV 3.X or higher
- matplotlib
- tensorflow
- keras

### [you can install the driver of Servo Motor_Steering]
> sudo pip3 install adafruit-circuitpython-servokit

### [Code decription]
### code1_lane_follower_opencv.py
This code is for driving along the lane using openCV. The color of the line being detected is red, but you can change the code from the detcar_opencv_lane_detact.py to a different color.

### code2_record_lane_video.py
It's a code for video shooting data on the road for machine learning.

### code3_get_train_data.py
This is the code that converts the recorded video into learning data.

### code4_lane_follower_deep_simul.py
### code5_lane_follower_deep.py
