import numpy as np
import cv2
import random
class Circle:
    def __init__(self,_h : np.float128 ,_k : np.float128 ,_r : int, vx : np.float128, vy : np.float128 , _color : tuple[int]):
        self.center = np.array([_h,_k], dtype=np.float128)
        self.r = _r
        self.v = np.array([vx,vy] , dtype= np.float128)
        self.color = _color
    def intersect(self,other):
        return np.linalg.norm(self.center - other.center) <= self.r + other.r
    
    def display(self,img):
        center_int = (int(round(self.center[1])), int(round(self.center[0])))
        cv2.circle(img, center_int , self.r, self.color , -1)
    

def create_animation(num_circles : int,h : int,w : int , radius : int):
    r = radius
    circles = [Circle(np.random.uniform(r,h-r),np.random.uniform(r,w-r),r,np.random.uniform(1,4.5),np.random.uniform(1,4.5) , 
                      (random.randint(0,255) , random.randint(0,255) , random.randint(0,255))) for _ in range(num_circles)]

    def update(circle : Circle):
        circle.center[0] += circle.v[0]
        circle.center[1] += circle.v[1]
        if circle.center[0] + circle.r > h or circle.center[0] - circle.r < 0 :
            circle.v[0] = -circle.v[0]
            if circle.center[0] + circle.r > h:
                circle.center[0] -= r/2
            else:
                circle.center[0] += r/2
        if circle.center[1] + circle.r > w or circle.center[1] - circle.r < 0 :
            circle.v[1]  = -circle.v[1]
            if circle.center[1] + circle.r > w:
                circle.center[1] -= r/2
            else:
                circle.center[1] += r/2    


    def collision(circles : list[Circle]):
        for i in range(num_circles):
            for j in range(i+1,num_circles):
                if circles[i].intersect(circles[j]):
                    ## source : Wikipedia (Elastic Collission)
                    ## suppose that all the circles have the same mass
                    c1, c2 = circles[i], circles[j]
                    c12 = c1.center - c2.center
                    c12_norm = np.linalg.norm(c12)
                    sum_radius = c1.r + c2.r
                    if c12_norm == 0:
                        c12 = np.random.randn(2) 
                        c12_norm = np.linalg.norm(c12)
                    c12 = c12/c12_norm
                    v12 = c1.v - c2.v
                    v_dir_c12 = np.dot(v12, c12)
                    c1.v -=  v_dir_c12 * c12
                    c2.v +=  v_dir_c12* c12
                    overlap = sum_radius - c12_norm
                    c1.center += c12*overlap/2
                    c2.center -= c12*overlap/2
    while 1:
        img = 255*np.zeros((h,w,3),dtype=np.uint8)
        
        collision(circles)
        
        for c in circles:
            c.display(img)
        
        cv2.imshow('Animation.png',img)
        
        for c in circles:
            update(c)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
    cv2.destroyAllWindows()

create_animation(10,800,800,25)


