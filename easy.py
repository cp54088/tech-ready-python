import pygame
import sys
import math


class Paddle(object):
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = 0
        self.speed = 20
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        self.x += self.vx

    def key_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.vy = 10
            if event.key == pygame.K_2:
                self.vy = 20
            if event.key == pygame.K_LEFT:
                self.vx = -self.speed
            elif event.key == pygame.K_RIGHT:
                self.vx = self.speed
        elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.vx = 0

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)   


class Ball(object):
    def __init__(self, x, y, width, height, vx, vy, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy
        self.color = color

    def render(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Pong(object):
    def __init__(self):
        pygame.init()
        (WIDTH, HEIGHT) = (800, 600)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("BOUNCE")
        self.ball = Ball(5, 5, 25, 25, 5, 7, (  0,   0,   0))
        self.paddle = Paddle(WIDTH / 2, HEIGHT - 50, 140, 10, 3, (  0,   0,   0))
        self.score = 0
    
    

    def play(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    

                if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    self.paddle.key_handler(event)

            self.collision_handler()
            self.draw()
    

    def collision_handler(self):
        

        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.vy = -self.ball.vy
            self.score += 1

        if self.ball.x + self.ball.width >= self.screen.get_width():
            self.ball.vx = -(math.fabs(self.ball.vx))
        elif self.ball.x <= 0:
            self.ball.vx = math.fabs(self.ball.vx)

        if self.ball.y + self.ball.height >= self.screen.get_height():
            pygame.quit()
            sys.exit()
        elif self.ball.y <= 0:
            self.ball.vy = math.fabs(self.ball.vy)

        if self.paddle.x + self.paddle.width >= self.screen.get_width():
            self.paddle.x = self.screen.get_width() - self.paddle.width
        elif self.paddle.x <= 0:
            self.paddle.x = 0

    def draw(self):
        self.screen.fill((130,212,250))

        font = pygame.font.Font(None, 75)
        score_text = font.render("Score: " + str(self.score), True, (  0,   0,   0))
        self.screen.blit(score_text, (300, 20))

        

        self.ball.update()
        self.ball.render(self.screen)
        self.paddle.update()
        self.paddle.render(self.screen)
  
        pygame.display.update()


if True:
    Pong().play()