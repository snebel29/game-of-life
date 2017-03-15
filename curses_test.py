import curses

def fillwin(w, c):
    y, x = w.getmaxyx()
    s = c * (x - 1)
    for l in range(y):
        w.addstr(l, 0, s)

def main(stdscr):
    stdscr.clear()
    fillwin(stdscr, 'S')
    stdscr.refresh()
    stdscr.getch()

    newwin=curses.newwin(10,20,5,5)
    fillwin(newwin, 'w')
    newwin.touchwin()
    newwin.refresh()
    newwin.getch()
    del newwin

    stdscr.touchwin()
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
