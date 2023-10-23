import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# create the pandas dataframe the csv file
states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state
print(state_names)
print(type(f"States names is type: {state_names}"))
turtle.shape(image)

answer_state = screen.textinput(title="Guess a state", prompt="Fill in another state name\t")

# check if the users guess was correct
def correct_guess(user_guess):
    # read all the states
    for state in state_names:
        # print(state)
        if user_guess.lower() == state.lower():
            return True


if correct_guess(answer_state):
    print("Yes")
else:
    print("No")

screen.exitonclick()
