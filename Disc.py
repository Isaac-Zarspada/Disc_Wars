from Disc_Wars.Main import WIDTH, HEIGHT, vectors 

class Disc: 
    def __init__(self, color,speedx, speedy, rect): # positionx, positiony
        self.rect = rect
        self.color = color
        # self.x = positionx
        # self.y = positiony
        self.speedx = speedx
        self.speedy = speedy

    def disc_animation(bluedisc_rect):
        bluedisc_rect.x += vectors[0]
        bluedisc_rect.y += vectors[1]

        if bluedisc_rect.top <= 0 or bluedisc_rect.bottom >= HEIGHT:
            vectors[1] *= -1
        if bluedisc_rect.left <= 0 or bluedisc_rect.right >= WIDTH:
            vectors[0] *= -1





bluedisc = Disc('blue', WIDTH/2, HEIGHT/2,speedx = 5, speedy = 5)