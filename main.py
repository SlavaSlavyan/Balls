# Импорт необходимых библиотек
from turtle import *

# Импорт модулей
from func.Anim import Anim
from func.JsonManager import JsonManager

# Основной класс игры
class Main:
    
    def __init__(self):
        
        # Экземпляры классов
        self.JsonManager = JsonManager(self)
        self.Anim = Anim(self)
        
        # Настройка turtle
        setup(1200,800)
        hideturtle()
        bgcolor((0,0,0))
        tracer(0)
    
    # Функция для старта программы
    def start(self):
        
        try:
            while True:
                
                clear() # очистка прошлого кадра
                
                self.Anim.main(self) # отрисовка нового кадра
                
                update() # вывод\обновление кадра
                
        except:
            pass

# Создание экземпляра основного класса и запуск игры
Balls = Main()
Balls.start()