class Ball:
    
    def __init__(self,m,pos:list,color:tuple,rad:int,move:list,width:int,speed:int):
        
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.rad = round(rad)
        self.move = move
        self.width = width
        self.speed = speed