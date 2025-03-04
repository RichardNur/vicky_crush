import re
import json
import random
from user_interface import menu
from data_handling import data_list
from colorama import Fore, Style



# Data:
candidate_list_full = data_list.candidate_list_full

def get_countries(path):
    ''' Returns a list of all countries from world-countries.json'''
    with open(path, 'r') as fileobj:
        data = json.load(fileobj)

        countries = []
        for country in data:
            countries.append(country['country'].lower())
    return countries

def get_us_states(path):
    ''' Returns a list of all us-states from world-countries.json '''
    with open(path, 'r') as fileobj:
        data = json.load(fileobj)

        us_states = []
        for state in data:
            us_states.append(state['name'].lower())
        return us_states

def get_professions(path):
    with open(path, 'r') as fileobj:
        data = json.load(fileobj)

        professions = []
        for profession in list(data.values()):
            professions.append(profession)
    return professions[0]


def get_random_person(data, countries, us_states):
    """ Pick a person at random from a list of celebrities """
    while True:
        data = candidate_list_full
        person = random.choice(data)
        return personv


def find_birth_year(text):
    """ finds the birth year in the birth_info string in results. """
    match = re.search(r'\b\d{4}\b', text) # Use regex to find 4-digit integers in the string
    if match:
        birth_year = int(match.group())
        return birth_year
    else:
        print('No integer found in wikipedia. Skipping that Question!!')
        return False

def get_answer_1(points, random_person):
    """ gets the answer for birth date from the user and compares with random_person
        returns the points gained in Q1. The closer the guess, the more points """

    print(f"Current Points: {points}\n")
    # Find birth year in random_person:
    name = random_person[0]
    birth_info = random_person[1]
    birth_year_result = find_birth_year(birth_info)

    # get user input, compare and give points:
    while True:
        try:
            birth_year_answer = int(input(Fore.CYAN + f"\nQUESTION 1: What year was {name} born?\n"+ Style.RESET_ALL))
            break
        except ValueError as v:
            print(f"Please just enter a valid year (XXXX), {v}")

    if birth_year_answer == birth_year_result: #correct answer
        print(f"{birth_year_result} is correct! You get 20 points!\n")
        points += 30
    elif birth_year_answer in range(birth_year_result - 11, birth_year_result + 11): # range 10 years
        print(f"{birth_year_answer} is in 10 year range! You get 15 points! Correct Answer: {birth_year_result}")
        points += 15
    elif birth_year_answer in range(birth_year_result - 51, birth_year_result + 51): # 50 year range
        print(f"{birth_year_answer} is in 50 year range! You get 10 points! Correct Answer: {birth_year_result}")
        points += 10
    elif birth_year_answer in range(birth_year_result - 101, birth_year_result + 101): # 100 year range
        print(f"{birth_year_answer} is in 100 year range! You get 5 points! Correct Answer: {birth_year_result}")
        points += 5
    else:
        print(f"{birth_year_answer} is more than 100 years apart! Correct Answer: {birth_year_result}. You get 0 points!")
    return points

def get_answer_2(points, random_person, countries, us_states):
    """Gets the answer for birth location from user and compares with random_person.
       Returns updated points for Question 2."""

    print(f"Current Points: {points}")
    # Find birth location in random_person:
    name = random_person[0]
    birth_info = random_person[1].lower()
    country = None
    state = None

    for county in us_states:
        if county in birth_info:
            country = "usa"
            state = county

    for land in countries:
        if land in birth_info:
            country = land

    if not country:
        print(f"Could not find a valid country/state in the data: {birth_info}")
        print("Skipping this question! You get 5 extra Points!")
        points += 5
        return points
    else:
        # Ask user for country input and check:
        location_answer = input(Fore.CYAN + f"\nQUESTION 2: Where was {name} born? " + Style.RESET_ALL).strip().lower()
        if location_answer == country or location_answer == state:
            print(f"Correct! {name} was born in {location_answer}. You get 10 points!")
            points += 10
        else:
            print(f"False! {name} was born in {state if state else country}.")

        # Optional Guess if a city was extracted:
        birth_city = random_person[1].split(",")[0].split()[-1]
        if len(birth_city) > 4:
            guess_city = input(f"Get 10 Bonus Points if you know the City {name} was born.\nGuess the city: ")

            if guess_city.lower() == birth_city.lower():
                points += 10
                print(f"Great Job, {birth_city} is correct!")
            else:
                print(f"False, {name} was born in {birth_city}.")

        return points

def get_answer_3(points, random_person, profession_keywords):
    """Gets the answer for birth location from user and compares with random_person.
       Returns updated points for Question 2."""
    print(f"Current Points: {points}")
    name = random_person[0]
    profession_info = random_person[2].split()

    # find professions of the random person
    professions = [word for word in profession_info]# if word in profession_keywords]

    # make a guess:
    profession_guess = input(Fore.CYAN +f"\nQUESTION 3: What is the profession of {name}, why are they famous? (Seperate with ',')\n"+ Style.RESET_ALL)
    guesses = [guess.strip().lower() for guess in profession_guess.split(',')]

    for guess in guesses:
        if guess in professions:
            print(f"Correct! {guess.upper()} is a profession of {name}! You get 10 Points!")
            points += 10
        else:
            print(f"{guess} is no profession of {name}. Sorry!")

    for profession in professions:
        print(f"{profession}", end=" ")
    return points


def main():

    ''' Print Welcome and Instructions:  '''
    menu.print_welcome()

    ''' SET NUMBER OF PLAYERS '''
    player_number = menu.set_player_number()
    players_and_points = {}

    ''' GAME PLAY'''
    for n, player in enumerate(range(player_number)):
        player_name = input("\n\n\t\t\t‼️NEW PLAYERS TURN‼️\n\n\t\t\t  Pass your name and hit Enter to enter the game mode \n").upper()

        ''' GET RELEVANT DATA: '''
        # Global variable: list of famous people (generated from wikipedia using beautifulsoup)
        countries = get_countries('data_handling/country-by-capital-city.json')
        us_states = get_us_states('data_handling/us-states.json')
        profession_keywords = get_professions('data_handling/professions.json')
        random_person = get_random_person(candidate_list_full, countries, us_states)


        ''' QUESTION 1: Birth Date '''
        menu.print_question_1(player_name, random_person)
        points = 0

        points = get_answer_1(points, random_person)
        input("\n\t\t\t\t\tPress Enter for the next question\n")


        ''' QUESTION 2: Birth Country and City '''
        menu.print_question_2(player_name)
        points = get_answer_2(points, random_person, countries, us_states)
        input("\n\t\t\t\t\t\t\tPress Enter for the next question\n")


        ''' QUESTION 3: Profession '''
        menu.print_question_3(player_name)

        #Q3: Profession/Fame
        points = get_answer_3(points, random_person, profession_keywords)
        print(f"\nYour Total Score is: {points}\nNEXT PLAYER's TURN!")

        # add points and player to dict:
        players_and_points[player_name] = points

    input(Fore.BLUE + "\n\t\t\t\t\t\t\t\t\tPress Enter to see the final score\n" + Style.RESET_ALL)
    menu.display_scoreboard(players_and_points)


if __name__ == "__main__":
    main()