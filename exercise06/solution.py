import numpy as np
import cv2
import random
class Circle:
    def __init__(self,_h : int ,_k : int ,_r : int, vx : int,vy : int):
        self.center = np.array([_h,_k])
        self.r = _r
        self.vx = vx
        self.vy = vy
    def intersect(self,other):
        return np.linalg.norm(self.center - other.center) <= self.r + other.r
    
    def display(self,img):
        cv2.circle(img, (self.center[1], self.center[0]), self.r, (255, 0, 0), -1)
    

def create_animation(num_circles : int,h : int,w : int):
    r = 30
    circles = [Circle(random.randint(r,h-r),random.randint(r,w-r),r,random.randint(1,10),random.randint(1,10)) for _ in range(num_circles)]
    
    
    def update(circle : Circle):
        circle.center[0] += circle.vx
        circle.center[1] += circle.vy
        if circle.center[0] + circle.r > h or circle.center[0] - circle.r < 0 :
            circle.vx  = -circle.vx
        if circle.center[1] + circle.r > w or circle.center[1] - circle.r < 0 :
            circle.vy  = -circle.vy

    def collision(circles : list[Circle]):
        is_collision = [False]*num_circles
        for i in range(num_circles):
            for j in range(i+1,num_circles):
                if circles[i].intersect(circles[j]):
                    if not is_collision[i]:
                        circles[i].vx *= -1
                        circles[i].vy *= -1
                        is_collision[i] = True
                    if not is_collision[j]:
                        circles[j].vx *= -1
                        circles[j].vy *= -1
                        is_collision[j] = True
    for _ in range(5000):
        img = 255*np.zeros((h,w,3),dtype=np.uint8)
        
        collision(circles)
        
        for c in circles:
            c.display(img)
        
        cv2.imshow('Animation.png',img)
        
        for c in circles:
            update(c)
        cv2.waitKey(20)
    
    
create_animation(10,600,1000)