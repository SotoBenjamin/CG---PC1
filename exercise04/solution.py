import numpy as np
import cv2

def create_mask(n):
    ans = 255*np.ones((n,n,3),dtype=np.uint8)
    h,k = n//2,n//2
    r = n//2
    for i in range(n):
        for j in range(n):
            if (i-h)**2 + (j-k)**2 <= r**2:
                ans[i,j] = (255,0,0)
    return ans

def f(img,i,j,t):
    a = max(img[i,j])
    b = max(t)
    return (int((t[0]/b)*a) , int( (t[1]/b)*a ) , int(  (t[2]/b)*a ))


def change_sacle(img,scale_img):
    h = img.shape[0]
    w = img.shape[1]
    ans = np.zeros((h,w,3) , dtype= np.uint8)
    for i in range(h):
        for j in range(w):
            ans[i,j] = f(img,i,j,scale_img[i,j])
    return ans



img = cv2.imread('lenna.png')
mask = create_mask(img.shape[0])
ans = change_sacle(img,mask)
cv2.imwrite('exercise04/output/lenna-colorscale.png',ans)
