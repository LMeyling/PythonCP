class Line():
    def __init__(self,x1,y1,x2,y2):
        self.bx = x1
        self.by = y1
        self.mx = x2-x1
        self.my = y2-y1
    def on_line(self,x,y):
        vx = x-self.bx
        vy = y-self.by
        return (vx*self.my == vy*self.mx)
    # Intersection Funktion wäre cool
