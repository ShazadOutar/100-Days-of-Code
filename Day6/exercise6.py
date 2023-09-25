def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    #try to go right if you can
    if right_is_clear():
        turn_right()
        move()
    #try to go stright if you can't go right
    elif not wall_in_front():
        move()
    #turn left and re-run the loop
    else:
        turn_left()
