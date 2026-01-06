import cv2
import numpy as np
import cv2.aruco as aruco

# =========================
# LOAD CALIBRATION DATA
# =========================
data = np.load("c270_calibration.npz")
camera_matrix = data["camera_matrix"]
dist_coeffs = data["dist_coeffs"]

# =========================
# ARUCO SETUP
# =========================
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
params = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, params)

marker_length = 0.05  # meters (5 cm)

# =========================
# 3D OBJECT POINTS (MARKER CORNERS)
# =========================
obj_points = np.array([
    [-marker_length / 2,  marker_length / 2, 0],
    [ marker_length / 2,  marker_length / 2, 0],
    [ marker_length / 2, -marker_length / 2, 0],
    [-marker_length / 2, -marker_length / 2, 0]
], dtype=np.float32)

# =========================
# OPEN CAMERA
# =========================
cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # =========================
    # DETECT MARKERS
    # =========================
    corners, ids, rejected = detector.detectMarkers(frame)

    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners, ids)

        for i in range(len(ids)):
            # 2D image points (pixel coordinates)
            img_points = corners[i][0].astype(np.float32)

            # =========================
            # POSE ESTIMATION (CORRECT)
            # =========================
            success, rvec, tvec = cv2.solvePnP(
                obj_points,
                img_points,
                camera_matrix,
                dist_coeffs,
                flags=cv2.SOLVEPNP_IPPE_SQUARE
            )

            if success:
                # Draw axis
                cv2.drawFrameAxes(
                    frame,
                    camera_matrix,
                    dist_coeffs,
                    rvec,
                    tvec,
                    0.03
                )

                x, y, z = tvec.flatten()
                print(f"ID {ids[i][0]} → X={x:.2f} m  Y={y:.2f} m  Z={z:.2f} m")

    cv2.imshow("Pose Estimation", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
