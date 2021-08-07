
# Cody --- Particle systems 1
# August 6, 1 day over Winry's 7/12 birthday, 2021.
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
#
# v0.00 - Add empty processing files *
# v0.01 - Make Particle.py, create some particles
# v0.02 - Make an emmiter



from Particle import *


def setup():
    global particles
    size(600, 600)
    colorMode(HSB, 360, 100, 100, 100)
    particles = []
    for i in range(30):
        particles.append(Particle(random(width/4), random(height/4)))
    
def draw():
    global particles
    background(168, 80, 50)
    
    gravity = PVector(0, 0.163) # 0.163 is an estimate of 9.8/60, the gravity on 
    # the planet divided by the frames per second.
    
    
    for p in particles:
        p.apply_force(gravity)
        p.edges()
        p.update()
        p.show()
        print(p.finished())
        
        
