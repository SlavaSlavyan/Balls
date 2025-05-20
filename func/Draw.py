from turtle import *

# Класс рисования
class Draw:
    
    def __init__(self,m):
        pass
    
    # рисование шара
    def ball(self,m,b):
        
        teleport(b.x,b.y-b.rad)
        pencolor(b.color)
        fillcolor(b.color)
        pensize(b.width)
        begin_fill()
        circle(b.rad)
        end_fill()