import numpy as np
import cv2

def contrast(original):
    min_pixels = np.min(original,axis=(0,1))
    max_pixels = np.max(original,axis=(0,1))
    original_float = original.astype(np.float32)
    ans = ((original_float - min_pixels)/(max_pixels-min_pixels))*255.0
    ans = ans.astype(np.uint8)
    return ans
def InterPolar(alpha,original,full_contrast):
    ans =  (1-alpha)*original.astype(np.float32) + alpha*full_contrast.astype(np.float32)
    ans = ans.astype(np.uint8)
    return ans

def f(c,original,full_contrast):
    alpha = c / 100.0
    current = InterPolar(alpha,original,full_contrast)
    cv2.imshow("Contrast", current)


original = cv2.imread('lowcontrast.png')
full_contrast = contrast(original)

cv2.namedWindow("Contrast", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Regulate", "Contrast", 0, 100, lambda c: f(c, original, full_contrast))

f(0,original,full_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()

