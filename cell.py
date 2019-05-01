import pyglet

class Tile:

    def __init__(self, x, y, w, bombValue):
        self.x = x
        self.y = y
        self.w = w
        self.revealed = False
        self.flagged = False
        self.image = pyglet.image.load('assets/concealed.png')
        self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
        if bombValue > 8:
            self.bomb = True
        else:
            self.bomb = False

    def reveal(self):
        self.revealed = True

    def drawSelf(self):
        self.tileSprite.draw()

    def updateSelf(self, bombCount):
        if not self.flagged:
            if bombCount == -1:
                self.image = pyglet.image.load('assets/revealedBomb.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
            elif bombCount == 1:
                self.image = pyglet.image.load('assets/revealedOne.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
            elif bombCount == 2:
                self.image = pyglet.image.load('assets/revealedTwo.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
            elif bombCount == 3:
                self.image = pyglet.image.load('assets/revealedThree.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
            elif bombCount == 4:
                self.image = pyglet.image.load('assets/revealedFour.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
            elif bombCount == 5:
                self.image = pyglet.image.load('assets/revealedFive.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
            elif bombCount == 6:
                self.image = pyglet.image.load('assets/revealedSix.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
            elif bombCount == 7:
                self.image = pyglet.image.load('assets/revealedSeven.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
            elif bombCount == 8:
                self.image = pyglet.image.load('assets/revealedEight.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
            else:
                self.image = pyglet.image.load('assets/revealed.png')
                self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
        else:
            self.flagged = False
            self.image = pyglet.image.load('assets/concealed.png')
            self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)

    def flagSelf(self):
        self.flagged = True
        self.image = pyglet.image.load('assets/flagged.png')
        self.tileSprite = pyglet.sprite.Sprite(self.image, self.x, self.y)

    def checkNum(self, board, x, y):
        if self.bomb:
            return -1
        else:
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    try:
                        if board[x + i][y + j].bomb:
                            count = count + 1
                            print('Bomb Found')
                    except IndexError:
                        continue
        return count
