"""
Project Requirements:
1. Convert the guess to title case ✔️
2. Check if the guess is in the 50 states ✔️
3. Write correct guesses onto the map ✔️
4. Use a loop to allow the user to keep guessing ✔️
5. Record the correct guesses in a list ✔️
6. Keep track of the score ✔️
"""

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# create the pandas dataframe the csv file
states_data = pandas.read_csv("50_states.csv")
print(f"states data is {states_data}")
print(f"index is: {states_data.index}")
state_names_series = states_data.state
# state_x_location_series = states_data.x
# state_y_location_series = states_data.y
# print(state_x_location_series)
# print(state_names_series)
# print(f"States names is type: {type(state_names_series)}")
state_names_list = state_names_series.to_list()
print(state_names_list)

# this puts the image of the map on screen
# turtle.shape(image)

# answer_state = screen.textinput(title="Guess a state", prompt="Fill in another state name\t")

# check if the users guess was correct


def correct_guess(user_guess):
    # read all the states
    for state in state_names_list:
        # print(state)
        if user_guess == state:
            # If correct, remove that option from the state_names_list
            print(f"Correct: {user_guess}")
            state_names_list.remove(state)
            print(state_names_list)
            return True
        # else:
    return False


def get_state_location(state_name):
    # from the state name, get it's x and y positions
    # x is the series of x values for states
    x = states_data.x.get(state_name)
    y = states_data.y.get(state_name)
    # print(type(x))
    # print(states_data.get(state_name))
    # print(x.get(state_name))
    # print(y.get(state_name))
    return [x, y]


FONT = ("Arial", 8, "normal")


def write_state_name(state_name, location):
    # use a turtle to write the name on the map
    writing_turtle = turtle.Turtle()
    writing_turtle.penup()
    writing_turtle.goto(location)
    writing_turtle.write(state_name, move=False, align="center", font=FONT)


def get_score(states_left):
    print(f"states left: {states_left}")
    current_score = 50 - len(states_left)
    return current_score


print(f"State names list type is: {type(state_names_list)}")

states_data.index = state_names_list
print(states_data)
print(f"index is: {states_data.index}")
# Just for testing
# state_names_list = ["Alabama", "Alaska", "Florida"]
while state_names_list:
    turtle.shape(image)
    score = get_score(state_names_list)
    # answer_state = screen.textinput(title="Guess a state", prompt="Fill in another state name\t").title()
    answer_state = screen.textinput(title=f"Score: {score}/50", prompt="Fill in another state name\t").title()
    print(f"Answer is: {answer_state}")
    if correct_guess(answer_state):
        print("Yes in main loop")
        location = get_state_location(answer_state)
        print(location)
        write_state_name(answer_state, location)
    else:
        print("No in main loop")

print("You win")
# screen.bye()
# screen.exitonclick()
