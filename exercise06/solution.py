import numpy as np
import cv2
import random
class Circle:
    def __init__(self,_h : int ,_k : int ,_r : int, vx : int, vy : int , _color : tuple[int]):
        self.center = np.array([_h,_k], dtype=np.float64)
        self.r = _r
        self.v = np.array([vx,vy] , dtype= np.float64)
        self.color = _color
    def intersect(self,other):
        return np.linalg.norm(self.center - other.center) <= self.r + other.r
    
    def display(self,img):
        center_int = (int(round(self.center[1])), int(round(self.center[0])))
        cv2.circle(img, center_int , self.r, self.color , -1)
    

def create_animation(num_circles : int,h : int,w : int , radius : int):
    r = radius
    circles = [Circle(random.randint(r,h-r),random.randint(r,w-r),r,random.randint(1,10),random.randint(1,10) , 
                      (random.randint(0,255) , random.randint(0,255) , random.randint(0,255))) for _ in range(num_circles)]

    def update(circle : Circle):
        circle.center[0] += circle.v[0]
        circle.center[1] += circle.v[1]
        if circle.center[0] + circle.r > h or circle.center[0] - circle.r < 0 :
            circle.v[0] = -circle.v[0]
            if circle.center[0] + circle.r > h:
                circle.center[0] -= 2*r
            else:
                circle.center[0] += 2*r
        if circle.center[1] + circle.r > w or circle.center[1] - circle.r < 0 :
            circle.v[1]  = -circle.v[1]
            if circle.center[1] + circle.r > w:
                circle.center[1] -= 2*r
            else:
                circle.center[1] += 2*r        

    def collision(circles : list[Circle]):
        for i in range(num_circles):
            for j in range(i+1,num_circles):
                if circles[i].intersect(circles[j]):
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
                    c1.center += c12*overlap
                    c2.center -= c12*overlap
    for _ in range(5000):
        img = 255*np.zeros((h,w,3),dtype=np.uint8)
        
        collision(circles)
        
        for c in circles:
            c.display(img)
        
        cv2.imshow('Animation.png',img)
        
        for c in circles:
            update(c)
        cv2.waitKey(20)
        
    
create_animation(30,1000,1000,10)