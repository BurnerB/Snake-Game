import random
import curses

#Initialize the library. Return a WindowObject which represents the whole screen.
s = curses.initscr()

#Set the cursor state. visibility can be set to 0, 1, or 2, for invisible, normal, or very visible
curses.curs_set(0)

#height and width of screen object(s)
sh, sw = s.getmaxyx()

#restart game timeout 100sec or pressing 1
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

#size of snake
snk_x = sw/4
snk_y = sh/2
snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

#size of food
food = [sh/2, sw/2]
food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key
    
    #if snake hits windows object border or itself
    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    
    #new snake position
    new_head = [snake[0][0], snake[0][1]]


    #snake movement
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)
    
    #if snake occupies same spot as food
    if snake[0] == food:
        food = None
        while food is None:
            #new food position after eaten
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)\
    
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)