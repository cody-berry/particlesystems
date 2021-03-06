
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
# v0.04 - Substitute texture in for particles
# v0.05 - Add confetti
# v0.06 - Add hammer and middle mouse click




from Particle import *
from Confetti import * 
from Hammer import *
from Emitter import *


def setup():
    global emitters
    size(1000, 1000)
    colorMode(HSB, 360, 100, 100, 100)
    emitters = []
    frameRate(1000)
    
def draw():
    global emitters
    background(234, 84, 33)
    
    for emitter in emitters:
        emitter.update()
        emitter.show()
    
    # I want the hue of the text to be related to the number of particles, 
    # indicating if the program is slow or not. I chose 270 just for a rough 
    # number that is a guess number of particles that makes the computer slow
    # down, and can be an interger random non-beginning average.
    
    total = 0
    
    for i in range(len(emitters)):
        total += len(emitters[i].particles)
    
    fill(map(total, 0, 300, 180, 360), 50, 70)
    text(total, width-50, height-50)
    fill(map(len(emitters), 0, 10, 180, 360), 50, 70)
    text(len(emitters), width-50, height-100)
    
def mousePressed():
    global emitters
    if mouseButton == LEFT:
        emitters.append(Emitter(mouseX, mouseY, "particle"))
    if mouseButton == CENTER:
        emitters.append(Emitter(mouseX, mouseY, "hammer"))
    if mouseButton == RIGHT:
        emitters.append(Emitter(mouseX, mouseY, "confetti"))
        
        
