def turn_right():
    turn_left()
    turn_left()
    turn_left()

#count the amount of rights made back to back
rights = 0
while not at_goal():
    if right_is_clear():
        #making a right turn increments the rights count
        #if more than 4 right turns made back to back, 
        #then try to move forward instead of going right
        if rights > 4 and front_is_clear():
            move()
        #if less than 4 rights made back to back, keep trying to go right
        else:
            turn_right()
            move()
        rights += 1
    elif front_is_clear():
        #if can't go right, try to go foreward
        rights = 0
        move()
    else:
        rights = 0
        turn_left()
