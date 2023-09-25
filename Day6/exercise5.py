def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    #climb up the wall
    while wall_on_right():
        move()
    #when at the top of the wall, move past it
    turn_right()
    move()
    turn_right()
    move()
    #start climbing down until the bottom of the wall
    while wall_on_right() and not wall_in_front():
        move()
    #turn left to fix orientation
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()
