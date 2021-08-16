from Particle import *

class Confetti(Particle):
    def __init__(self, x, y):
        super(Confetti, self).__init__(x, y)
        self.angle = random(0, TAU)
        
    def show(self):
        pushMatrix()
        fill(5, 99, 75, self.lifetime)
        translate(self.pos.x, self.pos.y)
        rotate(self.angle)
        noStroke() # If we don't do this, our confetti will be stroked.
        blendMode(ADD)
        square(0, 0, self.r)
        popMatrix()
        self.angle += 0.3
        
