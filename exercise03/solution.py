import numpy as np
import cv2

def contrast(original):
    min_pixels = np.min(original,axis=(0,1))
    max_pixels = np.max(original,axis=(0,1))
    original_float = original.astype(np.float32)
    ans = ((original_float - min_pixels)/(max_pixels-min_pixels))*255.0
    ans = ans.astype(np.uint8)
    return ans
def InterPolar(c,original,full_contrast):
    ### c = 0  f(c) = original
    ### c = 100 f(c) = full_contrast
    ### para un c e [0,100]
    ### f(c) = f(0) + (c/100)*(f(100) - f(0))
    ## f(c) = (1-c/100)*f(0) + + (c/100)*f(100) 
    ans =  (1-c/100)*original + (c/100)*full_contrast
    ans = ans.astype(np.uint8)
    return ans

def f(c,original,full_contrast):
    current = InterPolar(c,original,full_contrast)
    cv2.imshow("Contrast", current)


original = cv2.imread('lowcontrast.png')
full_contrast = contrast(original)

cv2.namedWindow("Contrast", cv2.WINDOW_NORMAL)
cv2.createTrackbar("Change", "Contrast", 0, 100, lambda c: f(c, original, full_contrast))

f(0,original,full_contrast)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    if cv2.getWindowProperty("Contrast", cv2.WND_PROP_VISIBLE) < 1:
        break
cv2.destroyAllWindows()

