
from Particle import *
from Confetti import *
from Hammer import *

class Emitter:
    def __init__(self, x, y, type):
        self.pos = PVector(x, y)
        self.particles = [] # the list of particles
        self.type = type
        self.particle_emit_rate = 1
        
    def update(self):
        for i in range(self.particle_emit_rate):
            if self.type == "particle":
                self.particles.append(Particle(self.pos.x, self.pos.y))
            if self.type == "hammer":
                self.particles.append(Hammer(self.pos.x, self.pos.y))
            if self.type == "confetti":
                self.particles.append(Confetti(self.pos.x, self.pos.y))
        
        gravity = PVector(0, 9.8/frameRate)
        
        
        for i in range(len(self.particles)-1, 0, -1):
            p = self.particles[i]
            p.edges()
            p.update()
            if p.finished():
                self.particles.pop(i)
                
    def show(self):
        for i in range(len(self.particles)):
            p = self.particles[i]
            p.show()
        
        # There's the emitter itself shown though.
        stroke(0, 0, 100, 100)
        fill(234, 84, 33, 20)
        circle(self.pos.x, self.pos.y, 64)
        
        
        
            
        
