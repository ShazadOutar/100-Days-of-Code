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
        else:
            return False


def get_state_location(state_name):
    # from the state name, get it's x and y positions
    # x is the series of x values for states
    x = states_data.x
    print(type(x))
    # print(states_data.get(state_name))
    print(x.get(state_name))
    

print(f"State names list type is: {type(state_names_list)}")

states_data.index = state_names_list
print(states_data)
print(f"index is: {states_data.index}")
# Just for testing
state_names_list = ["Alabama", "Alaska", "Florida"]
while state_names_list:
    turtle.shape(image)
    answer_state = screen.textinput(title="Guess a state", prompt="Fill in another state name\t").title()
    print(f"Answer is: {answer_state}")
    if correct_guess(answer_state):
        print("Yes in main loop")
    else:
        print("No in main loop")
    get_state_location(answer_state)


screen.exitonclick()
