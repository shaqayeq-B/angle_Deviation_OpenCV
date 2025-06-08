import cv2
import numpy as np

image = cv2.imread("metal_part.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = image.copy()

for contour in contours:
    if cv2.contourArea(contour) > 100:
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.intp(box)
        angle = rect[2]
        if angle < -45:
            angle += 90
        cv2.drawContours(output, [box], 0, (0, 255, 0), 2)
        center = tuple(np.int0(rect[0]))
        cv2.putText(output, f"{angle:.1f} deg", center, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow("Angle Detection", output)
cv2.waitKey(0)
cv2.destroyAllWindows()