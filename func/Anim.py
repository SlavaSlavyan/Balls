import random
from turtle import *

from func.Draw import Draw
from func.Ball import Ball

class Anim:
    
    def __init__(self,m):
    
        self.Draw = Draw(m)
        self.balls = []

        for i in range(255):
            self.balls.append(Ball(m,[random.randint(-window_width()//2,window_width()//2),random.randint(-window_height()//2,window_height()//2)],
                                   (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255),
                                   random.randint(5,50),
                                   [random.randrange(-1,2,2),random.randrange(-1,2,2)],
                                   5,1))
    
    def main(self,m):
        
        for ball in self.balls:
            
            self.Draw.ball(m,ball)
            ball.x += ball.move[0]
            ball.y += ball.move[1]
            
            if ball.x-ball.rad < -window_width()//2:
                ball.move[0] = 1
            if ball.x+ball.rad > window_width()//2:
                ball.move[0] = -1
            
            if ball.y-ball.rad < -window_height()//2:
                ball.move[1] = 1
            if ball.y+ball.rad > window_height()//2:
                ball.move[1] = -1