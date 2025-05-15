from turtle import *

from func.Anim import Anim

class Main:
    
    def __init__(self):
        
        self.Anim = Anim(self)
        
        setup(1200,800)
        hideturtle()
        bgcolor((0,0,0))
        tracer(0)
    
    def start(self):
        
        while True:
            
            clear()
            
            self.Anim.main(self)
            
            update()
    
Balls = Main()
Balls.start()