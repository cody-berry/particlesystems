

from Confetti import *
class Hammer(Confetti):
    def __init__(self, x, y):
        super(Hammer, self).__init__(x, y)
        self.vel = PVector(random(-3, 3), random(-3, 0))
        self.r = 70
        
    def show(self):
        pushMatrix()
        fill(20, 89, 20, self.lifetime*0.7)
        noStroke() # If we don't do this, our hammers will be
        # stroked.
        translate(self.pos.x, self.pos.y)
        rotate(self.angle)
        # The point that I'm translating to is the center of the hammer itself, 
        # not the center of the square of the hammer.
        rectMode(CENTER)
        rect(self.r/2, self.r/2, self.r, self.r/2)
        rect(self.r/2, self.r*5/4, self.r/5, self.r)
        popMatrix()
        self.angle += 0.003
        
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc = PVector(0, 0)
        self.lifetime -= random(1)
