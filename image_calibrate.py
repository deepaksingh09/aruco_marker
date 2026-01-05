import cv2
import os

# 🔹 Camera open karo
cap = cv2.VideoCapture(2)   # agar feed na aaye to 0 ya 1 try karo

# 🔹 Folder jahan images save hongi
save_dir = "calib_images"
os.makedirs(save_dir, exist_ok=True)

count = 0

print("Instructions:")
print("👉 Chessboard camera ke saamne rakho")
print("👉 'c' dabao image capture karne ke liye")
print("👉 'ESC' dabao exit ke liye")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera frame nahi mil raha")
        break

    # Live camera feed
    cv2.imshow("Calibration Image Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    # 🔹 Image capture
    if key == ord('c'):
        img_name = f"{save_dir}/img_{count}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Saved: {img_name}")
        count += 1

    # 🔹 Exit
    elif key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print(f"Total images captured: {count}")
