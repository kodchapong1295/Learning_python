import turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


import pandas
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        x = int(data[data["state"] == answer_state].x)
        y = int(data[data["state"] == answer_state].y)
        tim.goto(x,y)
        tim.write(answer_state)
        correct_guesses.append(answer_state)
