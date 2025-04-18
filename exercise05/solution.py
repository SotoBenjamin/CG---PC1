import numpy as np
import cv2


def padding(image, k ,type):
    pad_width = k // 2
    padded_image = np.pad(image, ((pad_width, pad_width), (pad_width, pad_width), (0, 0)), mode=type)
    return padded_image


def filter(img,kernel,type):
    h,w,c = img.shape
    ans = np.zeros((h,w,c))
    k = kernel.shape[0]
    img_pad = padding(img,k,type)
    for i in range(h):
        for j in range(w):
            for l in range(c):
                ans[i,j,l] = np.sum(img_pad[i:i+k,j:j+k,l] * kernel)
    ans = np.clip(ans, 0, 255).astype(np.uint8)
    return ans

def box_kernel(n):
    ans = np.ones((n,n),np.float32) / (n*n)
    return ans

def bartlett_kernel(n):
    a = [0]*n
    a[n//2] = (n+1)//2
    a[0] = 1
    for i in range(1,n//2):
        a[i] = a[i-1] + 1
    for i in range(n//2 + 1 , n):
        a[i] = a[i-1] - 1
    
    m = np.zeros((n,n) , np.float32)
    for i in range(n):
        for j in range(n):
            m[i,j] = a[i]*a[j]
    m = m/np.sum(m)
    return m

def pascal_triangle(n):
    if n == 1:
            return [[1]]
    rows = [[1],[1,1]]
    if n == 2:
        return rows
    for i in range(2 ,n):
        sz = len(rows[i-1]) + 1
        row = [1]*sz
        for j in range(1,sz-1):
            row[j] = rows[i-1][j-1] + rows[i-1][j]
        rows.append(row)
    return rows[n-1]


def gaussian_kernel(n):
    a = pascal_triangle(n)
    m = np.zeros((n,n) , np.float32)
    for i in range(n):
        for j in range(n):
            m[i,j] = a[i]*a[j]
    return m/np.sum(m)


img = cv2.imread('lenna.png')    

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


kernel3 = np.array([
    [ 0, 1,  0],
    [1,  -4, 1],
    [ 0, 1,  0]
], dtype=np.float32)

kernel5 = np.array([
    [ 0,  0,  1,  0,  0],
    [ 0,  1,  2, 1,  0],
    [1, 2, -17, 2, 1],
    [ 0, 1, 2, 1,  0],
    [ 0,  0,  1,  0,  0]
], dtype=np.float32)


res3 = filter(gray3, kernel3, type='edge')
res5 = filter(gray3, kernel5, type='edge')

cv2.imwrite('lap3x3_custom.jpg', res3)
cv2.imwrite('lap5x5_custom.jpg', res5)


