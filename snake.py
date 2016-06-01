import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import random
from random import randint


def start(snake_y=[], snake_x=[], direction=""):
    direction = "right"
    snake_y = [20, 20, 20]
    snake_x = [20, 19, 18]
    return [snake_y, snake_x, direction]


def main(scr):
    curses.noecho()
    curses.curs_set(0)
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    win_size=[curses.LINES, curses.COLS]
    win.keypad(1)
    win.border(0)
    win.nodelay(1)
    title = ' Snake '
    win.addstr(0, (curses.COLS - len(title)) // 2, title)
    gammeover = True

    turn = 0
    key = 0
    start_output = start()
    food = [randint(5, 20), randint(5, 75)]

    while gammeover != False:


        win.clear()
        win.keypad(1)
        win.border(0)
        win.nodelay(1)
        title = ' Snake '
        win.addstr(0, (curses.COLS - len(title)) // 2, title)
        score = 0
        win.addstr(0, 1, "Score: " + str(-3+len(start_output[0])) + " ")

        win.addch(food[0], food[1], "*")
        if start_output[0][0] == food[0] and start_output[1][0] == food[1]:
            food = [randint(5, 20), randint(5, 75)]
            start_output[0].insert(0, start_output[0][0])
            start_output[1].insert(1, start_output[1][0])

        if key == KEY_RIGHT:
            start_output[2] = "right"
            turn = len(start_output[0])
        elif key == KEY_LEFT:
            start_output[2] = "left"
            turn = len(start_output[0])
        elif key == KEY_UP:
            start_output[2] = "up"
            turn = len(start_output[0])
        elif key == KEY_DOWN:
            start_output[2] = "down"
            turn = len(start_output[0])

        if turn > 0:
            if start_output[2] == "up":
                start_output[0].pop()
                start_output[1].pop()
                start_output[0].insert(0, start_output[0][0]-1)
                start_output[1].insert(0, start_output[1][0])
                turn -= 1

            if start_output[2] == "right":
                start_output[0].pop()
                start_output[1].pop()
                start_output[0].insert(0, start_output[0][0])
                start_output[1].insert(0, start_output[1][0]+1)
                turn -= 1

            if start_output[2] == "down":
                start_output[0].pop()
                start_output[1].pop()
                start_output[0].insert(0, start_output[0][0]+1)
                start_output[1].insert(0, start_output[1][0])
                turn -= 1

            if start_output[2] == "left":
                start_output[0].pop()
                start_output[1].pop()
                start_output[0].insert(0, start_output[0][0])
                start_output[1].insert(0, start_output[1][0]-1)
                turn -= 1

        for i in range(len(start_output[1])):
            if start_output[0][0]==0 or start_output[1][0] == 0 or start_output[0][0] == 23 or start_output[1][0] == 79:
                gammeover = False
                #curses.endwin()
                #win.clear()

            elif start_output[2] == "right" and turn == 0:
                start_output[1][i] = start_output[1][i]+1

            elif start_output[2] == "left" and turn == 0:
                start_output[1][i] = start_output[1][i]-1

            elif start_output[2] == "up" and turn == 0:
                start_output[0][i] = start_output[0][i]-1

            elif start_output[2] == "down" and turn == 0:
                start_output[0][i] = start_output[0][i]+1

            win.addstr(start_output[0][i], start_output[1][i], "O")
        win.timeout(500)
        key = win.getch()

        win.refresh()

curses.wrapper(main)
