import cv2
import numpy as np

# =========================
# 🔹 LOAD CALIBRATION DATA
# =========================
data = np.load("c270_calibration.npz")
camera_matrix = data["camera_matrix"]
dist_coeffs = data["dist_coeffs"]

# =========================
# 🔹 OPEN CAMERA
# =========================
cap = cv2.VideoCapture(2)   # 0 / 1 / 2 try karo

if not cap.isOpened():
    print("❌ Camera open nahi ho raha")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # =========================
    # 🔹 UNDISTORT IMAGE
    # =========================
    new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(
        camera_matrix,
        dist_coeffs,
        (w, h),
        1,
        (w, h)
    )

    undistorted = cv2.undistort(
        frame,
        camera_matrix,
        dist_coeffs,
        None,
        new_camera_matrix
    )

    # =========================
    # 🔹 SHOW BOTH
    # =========================
    cv2.imshow("Original", frame)
    cv2.imshow("Undistorted", undistorted)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
