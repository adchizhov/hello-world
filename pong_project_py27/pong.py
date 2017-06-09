# By Alexander Chizhov
# Implementation of classic arcade game Pong

# import simpleguitk as simplegui
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
velocity_paddle = 8
# initialize ball_pos and ball_vel for new ball in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0,0]
score1 = 0
score2 = 0
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction == RIGHT:
        ball_vel = [random.randrange(2, 4),-(random.randrange(3, 6))]
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        ball_pos [0] += ball_vel [0]
        ball_pos [1] += ball_vel [1]
    elif direction == LEFT:
        ball_vel = [-(random.randrange(2, 4)),-(random.randrange(3, 6))]        
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        ball_pos [0] += ball_vel [0]
        ball_pos [1] += ball_vel [1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0	
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos [0] += ball_vel [0]
    ball_pos [1] += ball_vel [1]
    
    if ball_pos [1] >= HEIGHT - BALL_RADIUS:
        ball_vel [1] = - ball_vel [1]
    elif ball_pos [1] <= BALL_RADIUS:
        ball_vel [1] = - ball_vel [1]
    #elif ball_pos [0] < PAD_WIDTH + BALL_RADIUS:
        #score2 += 1
        #spawn_ball(LEFT)
    #elif ball_pos [0] > WIDTH - PAD_WIDTH - BALL_RADIUS:
        #score1 += 1
        #spawn_ball(LEFT)

    # draw ball
    canvas.draw_circle (ball_pos, BALL_RADIUS, 1, "Green", "Green")
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel) >= (HALF_PAD_HEIGHT) and (paddle1_pos + paddle1_vel) <= (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    if (paddle2_pos + paddle2_vel) >= (HALF_PAD_HEIGHT) and (paddle2_pos + paddle2_vel) <= (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    # draw paddles
    canvas.draw_polygon ([[0,paddle1_pos - HALF_PAD_HEIGHT],[PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],[0, paddle1_pos + HALF_PAD_HEIGHT]], 1, "#D72D47", "#D72D47")
    canvas.draw_polygon ([[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH, paddle2_pos + HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 1, "#4A44F2", "#4A44F2")
    # determine whether paddle and ball collide !!!!!!!!!!!!!!!!!   
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH - 1: # touch left
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos+HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]*1.2
        else:
            spawn_ball(RIGHT)
            score2 += 1
    else:
        if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH - 1: # touch right
            if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos+PAD_HEIGHT:
                ball_vel[0] = - ball_vel[0]*1.2
            else:
                spawn_ball(LEFT)
                score1 += 1
    # draw scores
    canvas.draw_text ("Player 1: " + str (score1), [90, 30], 25, "#D72D47")
    canvas.draw_text ("Player 2: " + str (score2), [390, 30], 25, "#4A44F2")
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel -= velocity_paddle
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel += velocity_paddle
    elif key == simplegui.KEY_MAP["w"]:
        paddle2_vel -= velocity_paddle
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel += velocity_paddle
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel += velocity_paddle
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel -= velocity_paddle
    elif key == simplegui.KEY_MAP["w"]:
        paddle2_vel += velocity_paddle
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel -= velocity_paddle
def stop ():
    frame.stop ()
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_canvas_background('#B5CE44')
frame.add_button ("Reset", new_game, 200)
frame.add_button ("Quit", stop, 200)
# start frame

frame.start()
