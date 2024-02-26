# monkey game
import curses
from curses import textpad
import time

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Define the boundaries of the game area
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Initialize the monkey position
    monkey = [sh // 2, sw // 2]
    w.addch(monkey[0], monkey[1], curses.ACS_DIAMOND)

    # Generate random position for the banana
    banana = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
    w.addch(banana[0], banana[1], curses.ACS_LANTERN)

    # Main game loop
    while True:
        # Get user input
        key = w.getch()
        if key in [curses.KEY_UP, ord('w')]:
            monkey[0] -= 1
        elif key in [curses.KEY_DOWN, ord('s')]:
            monkey[0] += 1
        elif key in [curses.KEY_LEFT, ord('a')]:
            monkey[1] -= 1
        elif key in [curses.KEY_RIGHT, ord('d')]:
            monkey[1] += 1

        # Check if monkey reaches the boundaries
        if monkey[0] in [0, sh - 1] or monkey[1] in [0, sw - 1]:
            message = "You lost! Monkey hit the boundary!"
            w.addstr(sh // 2, sw // 2 - len(message) // 2, message)
            w.refresh()
            break

        # Check if monkey catches the banana
        if monkey == banana:
            message = "You won! Monkey caught the banana!"
            w.addstr(sh // 2, sw // 2 - len(message) // 2, message)
            w.refresh()
            break

        # Update monkey position
        w.addch(monkey[0], monkey[1], curses.ACS_DIAMOND)

        # Refresh the screen
        w.refresh()

        # Delay for smooth animation
        time.sleep(0.1)

curses.wrapper(main)