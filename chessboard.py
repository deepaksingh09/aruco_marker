import cv2
import numpy as np

# 🔹 Chessboard configuration
squares_x = 9   # number of squares horizontally
squares_y = 6   # number of squares vertically
square_size = 100  # pixels per square (increase for better print quality)

# 🔹 Image size
width = squares_x * square_size
height = squares_y * square_size

# 🔹 Create white image
chessboard = np.ones((height, width), dtype=np.uint8) * 255

# 🔹 Draw black squares
for y in range(squares_y):
    for x in range(squares_x):
        if (x + y) % 2 == 0:
            x_start = x * square_size
            y_start = y * square_size
            chessboard[y_start:y_start+square_size,
                       x_start:x_start+square_size] = 0

# 🔹 Save image
cv2.imwrite("chessboard_9x6_A4.png", chessboard)

print("Chessboard image s.png")
