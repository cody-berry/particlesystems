
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
# v0.02 - Remove particles who are finished
# v0.03 - Make an emmiter



from Particle import *


def setup():
    global particles
    size(600, 600)
    colorMode(HSB, 360, 100, 100, 100)
    particles = []
    
def draw():
    global particles
    background(234, 84, 33)
    
    particle_emit_rate = 5
    
    for i in range(particle_emit_rate):
        particles.append(Particle(mouseX, mouseY))
    
    gravity = PVector(0, 9.8/frameRate) # 0.163 is an estimate of 9.8/60, the gravity on 
    # the planet divided by the frames per second.
    
    
    for i in range(len(particles)-1, 0, -1):
        p = particles[i]
        
        p.apply_force(gravity)
        p.edges()
        p.update()
        p.show()
        if p.finished():
            particles.pop(i)
    
    # I want the hue of the text to be related to the number of particles, 
    # indicating if the program is slow or not. I chose 270 just for a rough 
    # number that is a guess number of particles that makes the computer slow
    # down, and can be an interger random non-beginning average. 
    
    fill(map(len(particles), 0, 270, 180, 0), 50, 70)
    text(len(particles), width-50, height-50)
        
        
