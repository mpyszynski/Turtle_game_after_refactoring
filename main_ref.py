import turtle
import background
import buttons
import dice_image
import random

turtle.title("Racing turtle")
s = turtle.Screen()
s.setup(700, 700)

step_size = 20

player_num = []
players_names = []
rematch_calls = 0


dice_results = []
dice_dict = {
    '1': dice_image.res_one,
    '2': dice_image.res_two,
    '3': dice_image.res_three,
    '4': dice_image.res_four,
    '5': dice_image.res_five,
    '6': dice_image.res_six
    }

color_dict = {
    'b': 'black',
    'g': 'green',
    'p': 'pink',
    'r': 'red',
    'y': 'yellow',
    'o': '#fabd2f'
    }


def players_settings():
    global players_dict
    global num
    global number_of_players
    
    number_of_players = s.textinput("Number of players", "Enter number of players: 1-5")

    while number_of_players not in {'1', '2', '3', '4', '5'}:
        number_of_players = s.textinput("Number of players", "Enter CORRECT NUMBER of players: 1-5")
        if number_of_players in {'1', '2', '3', '4', '5'}:
            number_of_players = int(number_of_players)
            break
    number_of_players = int(number_of_players)
        
    for i in range(1, number_of_players+1):
        player_num.append('player_'+str(i))
        player_name = s.textinput("Player "+str(i), "Name of first player:")

        if player_name:
            if player_name == "":
                players_names.append('Anonymous_'+str(i))
            else:
                players_names.append(player_name.capitalize())
        else:
            players_names.append('Anonymous_'+str(i))

    players_dict = {player_num[i]: players_names[i] for i in range(len(player_num))}

    num = []
    for i in range(number_of_players):
        num.append(turtle.Turtle())


def turtle_starting_pos():
    global rematch_calls
    # turtle starting position Y coordinates
    x = [0, -75, 75, -150, 150]
    
    s.tracer(0)
    
    for i in range(number_of_players):
        
        if rematch_calls == 0:            
            color = s.textinput(players_names[i]+", choose color!", "Enter letter:\n\nb - black \ng - green \np - pink"
                                                                    " \nr - red \ny - yellow \no - orange\n")
            while color not in {'b', 'g', 'p', 'r', 'y', 'o'}:
                color = s.textinput(players_names[i]+", choose color!", "Enter correct letter:\n\nb - black \ng - green"
                                                                        " \np - pink \nr - red \ny - yellow "
                                                                        "\no - orange\n")
                if color in {'b', 'g', 'p', 'r', 'y', 'o'}:
                    break                
            num[i].fillcolor(color_dict[color])
            
        num[i].clear()
        num[i].shape("turtle")
        num[i].shapesize(3, 3, 3)
        num[i].penup()
        num[i].goto(-300, x[i])
        num[i].pendown()
        
    s.update()
    s.tracer(1)
    rematch_calls += 1


def dice_result(_, __):

    dice_image.res_reset()
    
    result = str(random.choice([1, 2, 3, 4, 5, 6]))
    dice_dict[result]()
    
    s.listen()
    dice_results.append(result)

    a = len(dice_results) % number_of_players
    if a == 0:
        a = number_of_players

    num[a-1].fd(int(result)*step_size)

    for i in range(number_of_players):
        if num[i].xcor() >= 250:
            buttons.match_result.write(str(players_names[i])+' wins!', font=("Verdana", 20, "normal"), align='center')
            replay()
        

def replay():
    replay = s.textinput("Play again?", "Type 'Y' to play again, type 'N' to exit")

    if replay:
        if replay in {'y', 'Y'}:
            turtle_starting_pos()
            dice_image.res_reset()
            buttons.match_result.clear()
                    
        elif replay.capitalize() == 'N':
            s.bye()
        else:
            while replay not in {'Y', 'y', 'N', 'n'}:
                replay = s.textinput("I don't understand...", "Type 'Y' to play again, type 'N' to exit")
                if replay.capitalize() == 'Y':
                    turtle_starting_pos()
                    dice_image.res_reset()
                    buttons.match_result.clear()
                elif replay.capitalize() == 'N':
                    s.bye()
    elif replay == '':
        turtle_starting_pos()
        dice_image.res_reset()
        buttons.match_result.clear()
    else:
        s.bye()   


players_settings()
turtle_starting_pos()
buttons.roll_button.onclick(dice_result)

turtle.done()
