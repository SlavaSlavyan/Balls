# Класс шара с определёнными свойствами
class Ball:
    
    def __init__(self,m,pos:list,color:tuple,rad:int,move:list,width:int,speed:int):
        
        # Позиция
        self.x = pos[0]
        self.y = pos[1]
        
        self.color = color    # цвет
        self.rad = round(rad) # радиус
        self.move = move      # вектор движения
        self.width = width    # ширина контура
        self.speed = speed    # скорость движения