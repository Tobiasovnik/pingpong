from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global speed_x, speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


speed_x = 5
speed_y = 5

widnow = True
game = True
back = (0, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = Ball("tenis_ball.png", 200, 200, 4, 50, 50)
font.init()
font1 = font.Font(None, 35)

lose1 = font1.render("player 1 loses!!!", True, (180, 0, 0))
lose2 = font1.render("player 2 loses!!!", True, (180, 0, 0))


finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.y > win_width:
            finish = True
            window.blit(lose2, (200, 200))
    




    

    racket1.reset()
    racket2.reset()
    ball.reset()
    




    display.update()
    clock.tick(fps)
