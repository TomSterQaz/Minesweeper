import pyglet
from random import randint
from math import floor
from cell import Tile

window = pyglet.window.Window(height = 750, width = 750)


board = []

for i in range(0, window.height, 50):
    tempList = []
    for j in range(0, window.width, 50):
        tempList.append(Tile(i, j, 50, randint(1, 10)))
    board.append(tempList)

def draw():
    window.clear()
    for item in board:
        for Tile in item:
            Tile.drawSelf()

def update(Tile, bombCount):
    Tile.updateSelf(bombCount)
    Tile.drawSelf()

def main():

    @window.event
    def on_draw():
        draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        x = floor(x / 50)
        y = floor(y / 50)
        print('x: {}, y: {}'.format(x, y))
        if button == pyglet.window.mouse.LEFT:
            board[x][y].reveal()
            if board[x][y].bomb:
                window.close()
            update(board[x][y], board[x][y].checkNum(board, x, y))

        elif button == pyglet.window.mouse.RIGHT:
            board[x][y].flagSelf()
            board[x][y].drawSelf()

    pyglet.app.run()
main()
