import turtle, pandas

screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answers = []
score = 0


while len(answers) < 50:
    answer_state = (screen.textinput(title=f"{score}/50 States guessed", prompt="Guess the state name?")).title()
    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in answers:
                missed_states.append(state)
                missed_df = pandas.DataFrame(missed_states)
                missed_df.to_csv("missed_states.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        answer_row = data[data.state == answer_state]
        xpos = int(answer_row.x)
        ypos = int(answer_row.y)
        t.goto(xpos, ypos)
        t.write(answer_state)
        # t.write(answer_row.state.item())
        answers.append(answer_state)
        score = len(answers)
print(score)
