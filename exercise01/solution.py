import numpy as np
import cv2

def InterPolar(F, x0, y0, x1, y1, x, y):
    return F[x0,y0]*(1-x+x0)*(1-y+y0) + F[x0,y1]*(1-x+x0)*(y-y0) + F[x1,y0]*(1-y+y0)*(x-x0) + F[x1,y1]*(x-x0)*(y-y0)

def resize(InputImage,NEW_WIDTH,NEW_HEIGHT,PADDING_STRATEGY):
    d = {'ZEROS' : 'constant' , 'LAST_PIXEL' : 'edge'}
    if len(InputImage.shape) == 3:
        pad_img = np.pad(InputImage , ((1,1),(1,1),(0,0)),mode = d[PADDING_STRATEGY])
        ans = np.zeros((NEW_HEIGHT,NEW_WIDTH,3))
    else:
        pad_img = np.pad(InputImage , ((1,1),(1,1)),mode = d[PADDING_STRATEGY])
        ans = np.zeros((NEW_HEIGHT,NEW_WIDTH))
    HEIGHT,WIDTH = InputImage.shape[0] , InputImage.shape[1]
    
    for i in range(NEW_HEIGHT):
        for j in range(NEW_WIDTH):
            x = (i/(NEW_HEIGHT-1))*(HEIGHT -1)
            y = (j/(NEW_WIDTH-1))*(WIDTH-1)
            x0  , y0 = int(x) , int(y)
            x1 , y1 = x0 + 1 , y0 +1
           
            ans[i,j] = InterPolar(pad_img,x0,y0,x1,y1,x,y) 
    return ans

img = cv2.imread('lenna.png')
print(img.shape)
ans = resize(img,1080,1080,'ZEROS')
cv2.imwrite('ans.png',ans)