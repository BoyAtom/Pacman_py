import pygame
import random
import sys


class Object():
    def __init__(self, x, y, image):
        self.img = pygame.image.load(image)
        self.objrect = self.img.get_rect()
        self.objrect.x = x
        self.objrect.y = y

    def draw(self, screen):
        screen.blit(self.img, self.objrect)


class Wall (Object):
    def __init__(self, x, y, image, scale):
        super().__init__(x, y, image)
        self.img = pygame.transform.scale(self.img, (8 * scale, 8 * scale))
        self.objrect = self.img.get_rect()
        self.objrect.x = x * 8 * scale
        self.objrect.y = y * 8 * scale

    def collision(object):
        return self.objrect.colliderect(object.objrect)


class Corn (Object):
    def __init__(self, x, y, image, scale):
        super().__init__(x, y, image)
        self.img = pygame.transform.scale(self.img, (8 * scale, 8 * scale))
        self.objrect = self.img.get_rect()
        self.objrect.x = x * 8 * scale
        self.objrect.y = y * 8 * scale


class Map:
    def __init__(self):
        self.map = [[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
                    [4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5],
                    [4, 9, 1, 2, 2, 2, 2, 2, 2, 3, 9, 1, 2, 2, 2, 3, 9, 1, 2, 2, 2, 2, 2, 2, 3, 9, 5],
                    [4, 9, 4, 9, 9, 9, 9, 9, 9, 5, 9, 6, 3, 9, 1, 8, 9, 4, 9, 9, 9, 9, 9, 9, 5, 9, 5],
                    [4, 9, 6, 3, 9, 1, 3, 9, 1, 8, 9, 9, 5, 9, 4, 9, 9, 6, 3, 9, 1, 3, 9, 1, 8, 9, 5],
                    [4, 9, 6, 8, 9, 4, 5, 9, 6, 7, 7, 7, 8, 9, 6, 7, 7, 7, 8, 9, 4, 5, 9, 6, 8, 9, 5],
                    [4, 9, 9, 9, 9, 4, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4, 5, 9, 9, 9, 9, 5],
                    [4, 9, 1, 3, 9, 4, 5, 9, 1, 2, 2, 2, 3, 9, 1, 2, 2, 2, 3, 9, 4, 5, 9, 1, 3, 9, 5],
                    [4, 9, 1, 8, 9, 6, 8, 9, 6, 3, 9, 9, 9, 9, 9, 9, 9, 1, 8, 9, 6, 8, 9, 6, 3, 9, 5],
                    [4, 9, 4, 9, 9, 9, 9, 9, 9, 5, 9, 1, 2, 2, 2, 3, 9, 4, 9, 9, 9, 9, 9, 9, 5, 9, 5],
                    [4, 9, 6, 7, 7, 7, 7, 7, 7, 8, 9, 6, 7, 7, 7, 8, 9, 6, 7, 7, 7, 7, 7, 7, 8, 9, 5],
                    [4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5],
                    [4, 9, 1, 3, 9, 1, 3, 9, 1, 2, 2, 2, 3, 9, 1, 2, 2, 2, 3, 9, 1, 3, 9, 1, 3, 9, 5],
                    [4, 9, 4, 5, 9, 4, 5, 9, 4, 0, 0, 0, 5, 9, 4, 0, 0, 0, 5, 9, 4, 5, 9, 4, 5, 9, 5],
                    [4, 9, 4, 5, 9, 4, 5, 9, 4, 0, 0, 0, 5, 9, 4, 0, 0, 0, 5, 9, 4, 5, 9, 4, 5, 9, 5],
                    [4, 9, 4, 5, 9, 4, 5, 9, 4, 1, 7, 7, 8, 9, 6, 7, 7, 3, 5, 9, 4, 5, 9, 4, 5, 9, 5],
                    [4, 9, 4, 6, 2, 8, 5, 9, 4, 5, 9, 9, 0, 0, 0, 9, 9, 4, 5, 9, 4, 6, 2, 8, 5, 9, 5],
                    [4, 9, 6, 7, 7, 7, 8, 9, 6, 8, 9, 1, 2, 0, 2, 3, 9, 6, 8, 9, 6, 7, 7, 7, 8, 9, 5],
                    [4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4, 0, 0, 0, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5],
                    [4, 9, 1, 2, 2, 2, 3, 9, 1, 3, 9, 6, 7, 7, 7, 8, 9, 1, 3, 9, 1, 2, 2, 2, 3, 9, 5],
                    [4, 9, 4, 1, 2, 3, 5, 9, 4, 5, 9, 9, 9, 9, 9, 9, 9, 4, 5, 9, 4, 1, 2, 3, 5, 9, 5],
                    [4, 9, 4, 5, 9, 4, 5, 9, 4, 6, 2, 2, 3, 9, 1, 2, 2, 8, 5, 9, 4, 5, 9, 4, 5, 9, 5],
                    [4, 9, 4, 5, 9, 4, 5, 9, 4, 0, 0, 0, 5, 0, 4, 0, 0, 0, 5, 9, 4, 5, 9, 4, 5, 9, 5],
                    [4, 9, 4, 5, 9, 4, 5, 9, 4, 0, 0, 0, 5, 0, 4, 0, 0, 0, 5, 9, 4, 5, 9, 4, 5, 9, 5],
                    [4, 9, 6, 8, 9, 6, 8, 9, 6, 7, 7, 7, 8, 0, 6, 7, 7, 7, 8, 9, 6, 8, 9, 6, 8, 9, 5],
                    [4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5],
                    [4, 9, 1, 2, 2, 2, 2, 3, 9, 1, 2, 2, 3, 9, 1, 2, 2, 3, 9, 1, 2, 2, 2, 2, 3, 9, 5],
                    [4, 9, 4, 0, 0, 0, 0, 5, 9, 6, 7, 7, 8, 9, 6, 7, 7, 8, 9, 4, 0, 0, 0, 0, 5, 9, 5],
                    [4, 9, 4, 0, 0, 0, 0, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4, 0, 0, 0, 0, 5, 9, 5],
                    [6, 7, 8, 0, 0, 0, 0, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 0, 0, 0, 0, 6, 7, 8]]

        self.main_menu = [[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
                          [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 1, 2, 2, 2, 3, 0, 0, 0, 0, 1, 2, 2, 2, 3, 0, 0, 0, 0, 1, 2, 2, 2, 3, 0, 5],
                          [4, 0, 4, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0, 0, 0, 4, 1, 7, 7, 8, 0, 5],
                          [4, 0, 4, 0, 5, 0, 5, 0, 0, 0, 0, 4, 0, 5, 0, 5, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 5],
                          [4, 0, 4, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 5],
                          [4, 0, 4, 1, 7, 7, 8, 0, 0, 0, 0, 4, 1, 7, 3, 5, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 5],
                          [4, 0, 4, 5, 0, 0, 0, 0, 0, 0, 0, 6, 8, 0, 6, 8, 0, 0, 0, 0, 4, 6, 2, 2, 3, 0, 5],
                          [4, 0, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7, 7, 7, 8, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 4, 0, 1, 2, 2, 2, 2, 2, 2, 2, 3, 0, 5, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 4, 0, 6, 7, 7, 7, 7, 7, 7, 7, 8, 0, 5, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                          [4, 0, 1, 7, 3, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 1, 3, 0, 5],
                          [4, 0, 4, 0, 6, 8, 0, 5, 0, 0, 0, 1, 2, 2, 2, 3, 0, 0, 0, 4, 6, 3, 0, 4, 5, 0, 5],
                          [4, 0, 4, 1, 3, 1, 3, 5, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0, 0, 4, 0, 6, 3, 4, 5, 0, 5],
                          [4, 0, 4, 5, 6, 8, 4, 5, 0, 0, 0, 4, 0, 5, 0, 5, 0, 0, 0, 4, 1, 3, 6, 8, 5, 0, 5],
                          [4, 0, 4, 5, 0, 0, 4, 5, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0, 0, 4, 5, 6, 3, 0, 5, 0, 5],
                          [4, 0, 4, 5, 0, 0, 4, 5, 0, 0, 0, 4, 1, 7, 3, 5, 0, 0, 0, 4, 5, 0, 6, 3, 5, 0, 5],
                          [4, 0, 6, 8, 0, 0, 6, 8, 0, 0, 0, 6, 8, 0, 6, 8, 0, 0, 0, 6, 8, 0, 0, 6, 8, 0, 5],
                          [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                          [6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8]]

        self.crossroads = [[10, 1], [16, 1], [1, 6], [4, 3], [7, 3], [19, 3], [22, 3], [4, 6], [7, 6], [13, 6], [19, 6], [22, 6], [25, 6],
                           [13, 8], [4, 9], [7, 9], [19, 9], [22, 9], [1, 11], [4, 11], [7, 11], [10, 11], [13, 11], [16, 11], [19, 11],
                           [22, 11], [25, 11], [1, 18], [7, 18], [10, 18], [13, 18], [16, 18], [19, 18], [25, 18], [13, 20], [1, 25], [4, 25],
                           [7, 25], [8, 25], [13, 25], [18, 25], [19, 25], [22, 25], [25, 25], [13, 28], [13, 16]]

        self.points = 0
        self.walls = []
        self.corns = []
        self.powerUps = []
        self.level = 1

    def clear_map(self):
        self.walls.clear()
        self.corns.clear()
        self.powerUps.clear()

    def createMap(self, screen, scale):
        for i in range(30):
            for j in range(27):
                if self.map[i][j] == 1:
                    self.walls.append(Wall(j, i, 'Tiles\Wall1.png', scale))
                elif self.map[i][j] == 2:
                    self.walls.append(Wall(j, i, 'Tiles\Wall2.png', scale))
                elif self.map[i][j] == 3:
                    self.walls.append(Wall(j, i, 'Tiles\Wall3.png', scale))
                elif self.map[i][j] == 4:
                    self.walls.append(Wall(j, i, 'Tiles\Wall4.png', scale))
                elif self.map[i][j] == 5:
                    self.walls.append(Wall(j, i, 'Tiles\Wall5.png', scale))
                elif self.map[i][j] == 6:
                    self.walls.append(Wall(j, i, 'Tiles\Wall6.png', scale))
                elif self.map[i][j] == 7:
                    self.walls.append(Wall(j, i, 'Tiles\Wall7.png', scale))
                elif self.map[i][j] == 8:
                    self.walls.append(Wall(j, i, 'Tiles\Wall8.png', scale))
                elif self.map[i][j] == 9:
                    self.corns.append(Corn(j, i, 'Tiles\Point.png', scale))

    def createMainMenu(self, screen, scale):
        for i in range(30):
            for j in range(27):
                if self.main_menu[i][j] == 1:
                    self.walls.append(Wall(j, i, 'Tiles\Wall1.png', scale))
                elif self.main_menu[i][j] == 2:
                    self.walls.append(Wall(j, i, 'Tiles\Wall2.png', scale))
                elif self.main_menu[i][j] == 3:
                    self.walls.append(Wall(j, i, 'Tiles\Wall3.png', scale))
                elif self.main_menu[i][j] == 4:
                    self.walls.append(Wall(j, i, 'Tiles\Wall4.png', scale))
                elif self.main_menu[i][j] == 5:
                    self.walls.append(Wall(j, i, 'Tiles\Wall5.png', scale))
                elif self.main_menu[i][j] == 6:
                    self.walls.append(Wall(j, i, 'Tiles\Wall6.png', scale))
                elif self.main_menu[i][j] == 7:
                    self.walls.append(Wall(j, i, 'Tiles\Wall7.png', scale))
                elif self.main_menu[i][j] == 8:
                    self.walls.append(Wall(j, i, 'Tiles\Wall8.png', scale))
                elif self.main_menu[i][j] == 9:
                    self.corns.append(Corn(j, i, 'Tiles\Point.png', scale))

    def drawMap(self, screen):
        for i in range(len(self.walls)):
            self.walls[i].draw(screen)
        for i in range(len(self.corns)):
            if self.corns[i] != 0:
                self.corns[i].draw(screen)

    def newLevel(self, scale, Pac):
        self.level += 1
        positionW = 0
        positionC = 0
        Pac.stop()
        Pac.objrect.x = 13 * 8 * scale
        Pac.objrect.y = 23 * 8 * scale
        for i in range(30):
            for j in range(27):
                if self.map[i][j] == 1:
                    self.walls[positionW] = (
                        Wall(j, i, 'Tiles\Wall1.png', scale))
                    positionW += 1
                elif self.map[i][j] == 2:
                    self.walls[positionW] = (
                        Wall(j, i, 'Tiles\Wall2.png', scale))
                    positionW += 1
                elif self.map[i][j] == 3:
                    self.walls[positionW] = (
                        Wall(j, i, 'Tiles\Wall3.png', scale))
                    positionW += 1
                elif self.map[i][j] == 4:
                    self.walls[positionW] = (
                        Wall(j, i, 'Tiles\Wall4.png', scale))
                    positionW += 1
                elif self.map[i][j] == 5:
                    self.walls[positionW] = (
                        Wall(j, i, 'Tiles\Wall5.png', scale))
                    positionW += 1
                elif self.map[i][j] == 6:
                    self.walls[positionW] = (
                        Wall(j, i, 'Tiles\Wall6.png', scale))
                    positionW += 1
                elif self.map[i][j] == 7:
                    self.walls[positionW] = (
                        Wall(j, i, 'Tiles\Wall7.png', scale))
                    positionW += 1
                elif self.map[i][j] == 8:
                    self.walls[positionW] = (
                        Wall(j, i, 'Tiles\Wall8.png', scale))
                    positionW += 1
                elif self.map[i][j] == 9:
                    self.corns[positionC] = (
                        Corn(j, i, 'Tiles\Point.png', scale))
                    positionC += 1


class Ghost (Object):
    def __init__(self, x, y, image, scale, color):
        super().__init__(x, y, image)
        self.img = pygame.transform.scale(self.img, (8 * scale, 8 * scale))
        self.objrect = self.img.get_rect()
        self.objrect.x = x * 8 * scale
        self.objrect.y = y * 8 * scale
        self.startx = x * 8 * scale
        self.starty = y * 8 * scale
        self.direction = 'left'
        self.speed = 1
        self.speedx = self.speed
        self.speedy = self.speed
        self.fear = False
        self.color = color
        self.cmb_speed = 0

    def move(self, Walls, PacMan, scale, crossroads):
        self.speedx = self.speed
        self.speedy = self.speed
        self.collide_pacman(PacMan, scale)
        self.check_crossroads(crossroads, scale)
        if self.direction == 'left':
            self.objrect.x -= self.speedx
        elif self.direction == 'right':
            self.objrect.x += self.speedx
        elif self.direction == 'top':
            self.objrect.y -= self.speedy
        elif self.direction == 'bottom':
            self.objrect.y += self.speedy
        self.collide_wall(Walls, scale)

    def stop(self):
        self.speedx = 0
        self.speedy = 0

    def check_crossroads(self, crossroads, scale):
        for i in range(len(crossroads)):
            if (crossroads[i][0] * 8 * scale == self.objrect.x) & (crossroads[i][1] * 8 * scale == self.objrect.y):
                self.random_direction()

    def random_direction(self):
        direction = random.randint(0, 3)
        if (direction == 0) & (self.direction != 'bottom'):
            self.direction = 'top'
            if self.color == 'red':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\RedTop.png'), (8 * scale, 8 * scale))
            elif self.color == 'yellow':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\YellowTop.png'), (8 * scale, 8 * scale))
            elif self.color == 'green':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\GreenTop.png'), (8 * scale, 8 * scale))
            elif self.color == 'pink':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\PinkTop.png'), (8 * scale, 8 * scale))
        elif (direction == 1) & (self.direction != 'left'):
            self.direction = 'right'
            if self.color == 'red':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\RedRight.png'), (8 * scale, 8 * scale))
            elif self.color == 'yellow':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\YellowRight.png'), (8 * scale, 8 * scale))
            elif self.color == 'green':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\GreenRight.png'), (8 * scale, 8 * scale))
            elif self.color == 'pink':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\PinkRight.png'), (8 * scale, 8 * scale))
        elif (direction == 2) & (self.direction != 'top'):
            self.direction = 'bottom'
            if self.color == 'red':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\RedBottom.png'), (8 * scale, 8 * scale))
            elif self.color == 'yellow':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\YellowBottom.png'), (8 * scale, 8 * scale))
            elif self.color == 'green':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\GreenBottom.png'), (8 * scale, 8 * scale))
            elif self.color == 'pink':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\PinkBottom.png'), (8 * scale, 8 * scale))
        elif (direction == 3) & (self.direction != 'right'):
            self.direction = 'left'
            if self.color == 'red':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\RedLeft.png'), (8 * scale, 8 * scale))
            elif self.color == 'yellow':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\YellowLeft.png'), (8 * scale, 8 * scale))
            elif self.color == 'green':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\GreenLeft.png'), (8 * scale, 8 * scale))
            elif self.color == 'pink':
                self.img = pygame.transform.scale(pygame.image.load(
                    'Tiles\PinkLeft.png'), (8 * scale, 8 * scale))

    def collide_wall(self, Walls, scale):
        for i in range(len(Walls)):
            if self.objrect.colliderect(Walls[i].objrect) == True:
                if self.direction == 'left':
                    self.stop()
                    self.objrect.x += self.speed
                    self.random_direction()
                    break
                elif self.direction == 'right':
                    self.stop()
                    self.objrect.x -= self.speed
                    self.random_direction()
                    break
                elif self.direction == 'top':
                    self.stop()
                    self.objrect.y += self.speed
                    self.random_direction()
                    break
                elif self.direction == 'bottom':
                    self.stop()
                    self.objrect.y -= self.speed
                    self.random_direction()
                    break

    def collide_pacman(self, pacman, scale):
        if self.objrect.colliderect(pacman.objrect):
            pacman.die(scale)
            self.objrect.x = self.startx
            self.objrect.y = self.starty


class PacMan(Object):
    def __init__(self, x, y, image, scale):
        super().__init__(x, y, image)
        self.img = pygame.transform.scale(self.img, (8 * scale, 8 * scale))
        self.objrect = self.img.get_rect()
        self.objrect.x = x * 8 * scale
        self.objrect.y = y * 8 * scale
        self.direction = 'left'
        self.speed = 2
        self.speedx = self.speed
        self.speedy = self.speed
        self.points = 0
        self.live = 3
        self.cmb_live = 0
        self.cmb_speed = 0
        self.img_num = 0

    def collide_wall(self, Walls):
        for i in range(len(Walls)):
            if self.objrect.colliderect(Walls[i].objrect) == True:
                if self.direction == 'left':
                    self.stop()
                    self.objrect.x += self.speed
                elif self.direction == 'right':
                    self.stop()
                    self.objrect.x -= self.speed
                elif self.direction == 'top':
                    self.stop()
                    self.objrect.y += self.speed
                elif self.direction == 'bottom':
                    self.stop()
                    self.objrect.y -= self.speed

    def collide_corn(self, Corns, Ghosts):
        for i in range(len(Corns)):
            if Corns[i] != 0:
                if self.objrect.colliderect(Corns[i].objrect) == True:
                    Corns[i] = 0
                    self.points += 10
                    self.cmb_live = 0
                    self.cmb_speed = 0
                    for i in range(len(Ghosts)):
                        Ghosts[i].cmb_speed = 0

    def animate(self):
        if (self.img_num >= 0) & (self.img_num < 7):
            self.img = pygame.transform.scale(pygame.image.load(
                'Tiles\PacMan.png'), (8 * scale, 8 * scale))
            self.turn_image()
            self.img_num += 1
        elif (self.img_num >= 7) & (self.img_num < 14):
            self.img = pygame.transform.scale(pygame.image.load(
                'Tiles\PacMan1.png'), (8 * scale, 8 * scale))
            self.turn_image()
            self.img_num += 1
        elif (self.img_num >= 14) & (self.img_num < 21):
            self.img = pygame.transform.scale(pygame.image.load(
                'Tiles\PacMan2.png'), (8 * scale, 8 * scale))
            self.turn_image()
            self.img_num += 1
        if self.img_num == 21:
            self.img_num = 0

    def turn_image(self):
        if self.direction == 'top':
            self.img = pygame.transform.rotate(self.img, 0)
        elif self.direction == 'right':
            self.img = pygame.transform.rotate(self.img, 270)
        elif self.direction == 'bottom':
            self.img = pygame.transform.rotate(self.img, 180)
        elif self.direction == 'left':
            self.img = pygame.transform.rotate(self.img, 90)

    def stop(self):
        self.speedx = 0
        self.speedy = 0

    def move(self, Walls, Corns, crossroads, scale, Ghosts):
        self.collide_corn(Corns, Ghosts)
        self.animate()
        if self.direction == 'left':
            self.objrect.x -= self.speedx
        elif self.direction == 'right':
            self.objrect.x += self.speedx
        elif self.direction == 'top':
            self.objrect.y -= self.speedy
        elif self.direction == 'bottom':
            self.objrect.y += self.speedy
        self.collide_wall(Walls)
        self.check_crossroads(crossroads, scale)

    def check_crossroads(self, crossroads, scale):
        for i in range(len(crossroads)):
            if (crossroads[i][0] * 8 * scale == self.objrect.x) & (crossroads[i][1] * 8 * scale == self.objrect.y):
                self.stop()

    def live_up(self):
        if (self.points % 3000 == 0) & (self.points != 0) & (self.cmb_live == 0):
            self.live += 1
            self.cmb_live += 1

    def die(self, scale):
        self.stop()
        self.live -= 1
        pygame.time.wait(1000)
        self.objrect.x = 13 * 8 * scale
        self.objrect.y = 24 * 8 * scale


def addGhost(Ghosts, scale):
    Ghosts.append(Ghost(13, 18, 'Tiles\YellowLeft.png', scale, 'yellow'))
    Ghosts.append(Ghost(13, 18, 'Tiles\YellowLeft.png', scale, 'yellow'))
    Ghosts.append(Ghost(13, 18, 'Tiles\YellowLeft.png', scale, 'yellow'))
    Ghosts.append(Ghost(13, 18, 'Tiles\YellowLeft.png', scale, 'yellow'))
    Ghosts.append(Ghost(13, 18, 'Tiles\YellowLeft.png', scale, 'yellow'))


width = 27 * 8
height = 30 * 8
blue = 0, 0, 255
scale = 3


def main():
    in_game = False
    cmb = 0
    pygame.init()
    gameover = False
    screen = pygame.display.set_mode((width * scale, height * scale))
    button = pygame.Rect(10 * 8 * scale, 14 * 8 * scale,
                         8 * 7 * scale, 8 * 3 * scale)
    map = Map()
    map.createMainMenu(screen, scale)
    font = pygame.font.Font('Font\PixelFont.ttf', 10)
    pointsText = font.render(('Points'), True, blue)
    livesText = font.render(('Lives'), True, blue)
    Ghosts = [Ghost(13, 18, 'Tiles\RedLeft.png', scale, 'red'), Ghost(12, 18, 'Tiles\GreenLeft.png', scale, 'green'),
              Ghost(14, 18, 'Tiles\PinkLeft.png', scale, 'pink'), Ghost(13, 18, 'Tiles\YellowLeft.png', scale, 'yellow')]
    Pac = PacMan(13, 24, 'Tiles\PacMan.png', scale)
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Pac.stop()
                    Pac.speedy = Pac.speed
                    Pac.direction = 'top'
                    Pac.animate()
                if event.key == pygame.K_s:
                    Pac.stop()
                    Pac.speedy = Pac.speed
                    Pac.direction = 'bottom'
                    Pac.animate()
                if event.key == pygame.K_a:
                    Pac.stop()
                    Pac.speedx = Pac.speed
                    Pac.direction = 'left'
                    Pac.animate()
                if event.key == pygame.K_d:
                    Pac.stop()
                    Pac.speedx = Pac.speed
                    Pac.direction = 'right'
                    Pac.animate()
            if (event.type == pygame.MOUSEBUTTONDOWN) & (in_game == False):
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    in_game = True
                    map.clear_map()
                    map.createMap(screen, scale)
                    for j in range(len(Ghosts)):
                        Ghosts[j].objrect.x = 13 * 8 * scale
                        Ghosts[j].objrect.y = 18 * 8 * scale
                    Pac.objrect.x = 13 * 8 * scale
                    Pac.objrect.y = 24 * 8 * scale

        nextLvl = 0
        for i in range(len(map.corns)):
            if map.corns[i] == 0:
                nextLvl += 1
            if nextLvl == len(map.corns):
                addGhost(Ghosts, scale)
                map.newLevel(scale, Pac)
                for j in range(len(Ghosts)):
                    Ghosts[j].objrect.x = 13 * 8 * scale
                    Ghosts[j].objrect.y = 18 * 8 * scale
                pygame.time.wait(1000)
        screen.fill((0, 0, 0))
        Pac.live_up()
        pointsNum = font.render(str(Pac.points), True, blue)
        livesNum = font.render(str(Pac.live), True, blue)
        if (in_game == False):
            pygame.draw.rect(screen, blue, button)
        map.drawMap(screen)
        for i in range(len(Ghosts)):
            Ghosts[i].draw(screen)
        if (in_game == True):
            Pac.draw(screen)
            Pac.move(map.walls, map.corns, map.crossroads, scale, Ghosts)
            screen.blit(pointsText, (8 * scale * 20, 8 * scale * 27))
            screen.blit(livesText, (8 * 3 * scale, 8 * 27 * scale))
            screen.blit(pointsNum, (8 * scale * 20, 8 * scale * 28))
            screen.blit(livesNum, (8 * 3 * scale, 8 * 28 * scale))
        for i in range(len(Ghosts)):
            Ghosts[i].move(map.walls, Pac, scale, map.crossroads)
        if Pac.live == 0:
            in_game = False
            Pac.cmb_speed = 0
            Pac.live = 3
            Pac.speed = 2
            Pac.points = 0
            map.level = 1
            map.clear_map()
            map.createMainMenu(screen, scale)
            for i in range(len(Ghosts)):
                Ghosts[i].cmb_speed = 0
                Ghosts[i].speed = 1
            for j in range(len(Ghosts)):
                Ghosts[j].objrect.x = 13 * 8 * scale
                Ghosts[j].objrect.y = 18 * 8 * scale
        pygame.display.flip()
        pygame.time.wait(1)
    sys.exit()


main()
