import cowsay
from colorama import Fore, Style

def print_welcome():
    """ Print Welcome and Instructions:  """
    print()
    head_line = f"\t\t\t{'*' * 10} WELCOME TO THE VICKY CRUSHES GAME {'*' * 10}"
    length_head_line = len(head_line)
    print(Fore.CYAN + f"\t\t\t{'*' * length_head_line}\n{head_line}\n\t\t\t{'*' * length_head_line}" + Fore.YELLOW)
    cowsay.ghostbusters(f"HELLO \nPlease read\ninstructions\ncarefully!!!")
    print()
    print_note_ghost = (Style.RESET_ALL + "\n\t\t\t\t\tTHE GAME WILL RANDOMLY PICK A CELEBRITY."
                        "\n\t\t\t  YOU HAVE TO ANSWER 3 QUESTIONS ABOUT THE CELEBRITY."
                        "\n\t\tYOU GET POINTS FOR EACH RIGHT ANSWER WHICH WILL SHOW AT THE END."
                        "\n\t\t  EACH QUESTION HAS A SLIGHTLY DIFFERENT POINTING SYSTEM."
                        )
    print(print_note_ghost)


def set_player_number():
    """ SET NUMBER OF PLAYERS """

    while True:
        try:
            how_many_players = int(input(Fore.GREEN + "\n\t\t\t\t\t  How many Players want to play?\n" + Style.RESET_ALL))
            break
        except ValueError as v:
            print(f"Please enter valid number (e.g. 1-4): {v}")

    return how_many_players

def print_question_1(user_input, random_person):

    cowsay.kitty(Fore.MAGENTA + f"{user_input}\nget ready\nto answer the\nfirst question")
    print_note_cat_1 = ("\n\t\t\t\t\tGUESS THE CELEBRETY'S BIRTH YEAR\n"
                        "\n\t\t\t  If you get the correct year you get 20 points."
                        "\n\t\tIf you guess within a range of 25 years + /- you get 10 points."
                        "\n\t\tIf you guess within a range of 100 years + / - you get 5 points."
                        )
    print(print_note_cat_1 + Style.RESET_ALL)
    print(Fore.BLUE + f"\nYour Random Person is: {Style.RESET_ALL + random_person[0].upper()}")


def print_question_2(user_input):

    cowsay.stegosaurus(f"{user_input}\nget ready\nto answer the\nsecond question")
    print_note_steg_2 = ("\n\t\t\t\t\t\t\tGUESS THE CELEBRETY'S BIRTH PLACE\n"
                         "\n\t\t\t\t\tIf you guess correct country you get 10 points."
                         )
    print(print_note_steg_2)


def print_question_3(user_input):

    cowsay.turtle(f"{user_input}\nget ready\nto answer the\nthird question")
    print_note_turtle_3 = ("\n\t\t\t\t\t\t\t\t\tGUESS THE CELEBRETY'S OCCUPATION\n"
                           "\n\t\t\t\t\t\t\t  If you get the correct occupation you get 20 points.")
    print(print_note_turtle_3)

def display_scoreboard(scoreboard):
    """Return the final scoreboard sorted by scores in descending order."""
    if not scoreboard:
        scoreboard_display =  "Scoreboard is empty."

    # Sort the scoreboard by score in descending order
    sorted_scores = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)

    # Construct the scoreboard string
    scoreboard_lines = [f"{rank}. {player}: {score} pts"
                        for rank, (player, score) in enumerate(sorted_scores, start=1)]
    scoreboard_display =  "\n".join(scoreboard_lines)  # Join lines into a single string

    ''' Display the Scoreboard:'''
    trex_speech = cowsay.get_output_string("trex", scoreboard_display)
    # ADD RED DINO T-REX
    print(Fore.RED + trex_speech + Style.RESET_ALL)  # Print the formatted message
