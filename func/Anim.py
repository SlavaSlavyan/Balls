# Импорт необходимых библиотек
import random
from turtle import *

# Импорт модулей
from func.Draw import Draw
from func.Ball import Ball

class Anim:
    
    def __init__(self,m):
        
        # Настройка экрана
        self.screen_update(m)

        # Создание экземпляра класса рисования
        self.Draw = Draw(m)
        
        # Массив для всех шаров
        self.balls = []

        # Добавление в массив шаров с случайными значениями
        for i in range(255):
            self.balls.append(Ball(m,[random.randint(-window_width()//2,window_width()//2),random.randint(-window_height()//2,window_height()//2)],
                                   (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255),
                                   random.randint(5,50),
                                   [random.randrange(-1,2,2),random.randrange(-1,2,2)],
                                   5,1))
    
    # Основная функция отображения
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
    
    # Обновление экрана с учётом информации из конфигурации    
    def screen_update(self,m):
        
        if m.config['fullscreen']:
            
            screen = Screen().getcanvas().winfo_toplevel()
            screen.attributes('-fullscreen', True)
        
        else:
            
            setup(m.config["screen-size"][0],m.config["screen-size"][1])
        