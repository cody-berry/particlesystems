# -*- coding: utf-8 -*-
# With Daniel Shiffman
# Paper by William Reeves
# Created in 1983
# Particle Systems - A Technique for Modeling a Class of Fuzzy Objects
# Particles have:
#     Initial Velocity
#     Lifetime
#     Transparency
#     Force
#     And... More!


class Particle:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        # if only multiply by a constant, then it would look like a ring and we want
        # it to look more chaotic.
        self.vel = PVector.random2D().mult(random(1, 5)) 
        self.acc = PVector(0, 0)
        self.r = random(5, 16)
        # self.lifetime equals the transparency.
        self.lifetime = 100
        
    # When we show many and one particle is about to die, we want to remove the 
    # dead particles because of course it's going not show up anymore.
    def finished(self):
        return self.lifetime < 0
    
    def apply_force(self, force): # Force is a PVector.
        # f = ma, so a = F/m. we assume that m = 1.
        self.acc.add(force)
        
    def edges(self):
        if self.pos.x + self.r > width:
            self.vel.x *= -1
        if self.pos.x - self.r < 0:
            self.vel.x *= -1
            
        if self.pos.y + self.r > height:
            self.vel.y *= -1
        if self.pos.y - self.r < 0:
            self.vel.y *= -1
            
    # Next up is show. In __init__(self), remember that I said the self.lifetime is
    # the transparency?
    def show(self):
        stroke(0, 0, 100, self.lifetime)
        fill(0, 0, 100, self.lifetime)
        circle(self.pos.x, self.pos.y, self.r)
        
    # Last is update. δ/δx(position) = velocity. δ/δ(velocity) = acceleration. 
    # δ/δx(acceleration) = -acceleration. Life also decreases.
    
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc = PVector(0, 0)
        
        self.lifetime -= random(1)
    
    
