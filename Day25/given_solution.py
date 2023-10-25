import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# states_left = all_states
guessed_states = []
# def get_missed_states():
#     print(states_left)
#     with open("states_to_learn.csv", mode="w") as file:
#         for state in states_left:
#             file.write(f"{state}, ")


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Fill in another state name").title()
    print(answer_state)
    if answer_state == "Exit":
        # get_missed_states()
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # get the row at the state name
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # Or could use
        # t.write(state_data.state.item())
        # states_left.remove(answer_state)

# screen.exitonclick()
# generate a new file of the states the user didn't guess, states_to_learn.csv
