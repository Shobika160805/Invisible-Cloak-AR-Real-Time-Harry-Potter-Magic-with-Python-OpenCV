import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

# Allow camera to warm up and capture the background
print("Capturing background. Please stay out of the frame for 3 seconds.")
for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)  # Mirror the background

print("Background captured. Bring in your LIGHT BLUE colored cloak!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = np.flip(frame, axis=1)

    # Convert the frame to HSV color space for color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define HSV range for LIGHT BLUE cloak
    lower_blue = np.array([90, 50, 70])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Remove noise using morphological operations
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

    mask_inv = cv2.bitwise_not(mask)

    # Segment out cloak area from saved background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    # Segment out non-cloak area from current frame
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
    # Combine cloak and non-cloak parts
    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)

    # Display invisible cloak effect
    cv2.imshow("Invisible Cloak", final_output)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
