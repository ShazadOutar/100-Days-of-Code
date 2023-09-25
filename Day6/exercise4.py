def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#while not at the goal, keep going
while not at_goal():
    #if there is space to move forward, do it
    if front_is_clear():
        move()
    #if theres a wall in front, jump over it
    if wall_in_front():
        jump()

