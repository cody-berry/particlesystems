
from Particle import *


class Emitter:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.particles = [] # the list of particles
        
    def update(self):
        particle_emit_rate = 3
    
        for i in range(particle_emit_rate):
            self.particles.append(Particle(self.pos.x, self.pos.y))
        
        gravity = PVector(0, 9.8/frameRate)
        
        
        for i in range(len(self.particles)-1, 0, -1):
            p = self.particles[i]
            
            p.apply_force(gravity)
            p.edges()
            p.update()
            if p.finished():
                self.particles.pop(i)
                
    def show(self):
        for i in range(len(self.particles)):
            p = self.particles[i]
            p.show()
        
        # There's the emitter itself shown though.
        
        
        
            
        
