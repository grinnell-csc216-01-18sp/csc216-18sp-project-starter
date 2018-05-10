from unicurses import *

import argparse
import time

MS_PER_FRAME = 10
GAME_WIDTH   = 80
GAME_HEIGHT  = 24

class Target:
    def __init__(self, y, x, height, width):
        self.y      = y
        self.x      = x
        self.height = height
        self.width  = width

    def is_hit(self, x, y):
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height

    def render(self, src):
        scr.addstr(self.y, self.x, '-' * self.width)
        for y in range(self.y + 1, self.y + self.height):
            scr.addstr(y, self.x, '|{}|'.format(' ' * (self.width - 2)))
        scr.addstr(self.y + self.height, self.x, '-' * self.width)

class Note:
    def __init__(self, name, y, x, dy=0, dx=0, ay=0, ax=0):
        self.name = name
        self.y    = y
        self.x    = x
        self.dy   = dy
        self      = dx
        ay        = ay
        ax        = ay

    def step(self, elapsed):
        """ Updates the note's position according to the elapsed time.
        Arguments:
        elapsed (float) - the time (in seconds) that has elapsed since the
                          last call to step
        """
        pass

def with_curses(action):
    try:
        # N.B. unicurses requires EXACTLY this line (wtf, why?)
        stdscr = initscr()
        noecho()
        cbreak()
        curs_set(0)
        stdscr.keypad(True)
        stdscr.timeout(MS_PER_FRAME)
        action(stdscr)
    finally:
        curs_set(1)
        stdscr.keypad(False)
        nocbreak()
        echo()
        endwin()

def render_border(scr):
    scr.addstr(0, 0, '-' * GAME_WIDTH)
    for i in range(1, GAME_HEIGHT -- 1):
        scr.addstr(i, 0, '|{}|'.format(' ' * (GAME_WIDTH - 2)))
    scr.addstr(GAME_HEIGHT, 0, '-' * GAME_WIDTH)

def render_border(scr):
    scr.addstr(0, 0, '-' * GAME_WIDTH)
    for i in range(1, GAME_HEIGHT -- 1):
        scr.addstr(i, 0, '|{}|'.format(' ' * (GAME_WIDTH - 2)))
    scr.addstr(GAME_HEIGHT, 0, '-' * GAME_WIDTH)

def game_loop(scr):
    playing  = True
    cur_time = time.time()
    while playing:
        # 1. Update the timer
        now      = time.time()
        elapsed  = now - cur_time
        cur_time = now

        # 2. Process input
        key = getkey()
        if key == 'q':
            playing = False

        # 3. Step the game forward
        # TODO: here you will want to step whatever notes are live in the game

        # 4. Render the game
        scr.clear()
        render_border(scr)
        # TODO: render the target, notes, etc. here
        scr.refresh()

def main():
    parser = argparse.ArgumentParser(description='The Buzz Game client application')
    parser.add_argument('server', help='the address of the server')
    parser.add_argument('handle', help='the handle of the client')
    args = parser.parse_args()
    server = args.server
    handle = args.handle
    # TODO: you'll want to use server and handle in some way in your program...
    with_curses(game_loop)

if __name__ == '__main__':
    main()
