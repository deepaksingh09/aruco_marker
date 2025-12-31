#importing the lib
import cv2
# with the help of cv2 i m importing aruco
import cv2.aruco as aruco
# aruco_gen is variable
aruco_gen= aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
# yaha pe hum predefined  dict use kr rahe hai
marker_id =3
marker_size=500#500 width , height

# abh image generate hogi
marker = aruco.generateImageMarker(aruco_gen , marker_id,marker_size)
cv2.imwrite("aruco_1(4X4).png",marker)