# Write your code here.

def get_number_of_teams():
    while True:
        num_of_team = int(input("Enter the number of teams in the tournament: "))
        if num_of_team >= 2:
            return num_of_team
            break
        else:
            print('The minimum number of teams is 2, try again')
def get_team_names(num_teams):
    count = 0
    team_names = []
    while True:
        count = count +1
        team_name = input(f"Enter the name for team #{count}: ")
        valid_words = len(team_name.split()) > 2 
        valid_char = len(team_name) < 2
        
        if valid_words or valid_char:
            while True:
                if valid_words:
                    print("Team name may have at most 2 words, try again.")
                elif valid_char:
                    print("Team names must have at least 2 characters, try again.")

                team_name = input(f"Enter the name for team #{count}: ")
                if len(team_name.split()) <= 2 and len(team_name) >= 2:
                    break

        team_names.append(team_name)
        if count == num_teams:
            break
    return team_names

def get_number_of_games_played(num_teams):
    num_of_played_games = int(input("Enter The number of games Played by each team: "))
    if num_of_played_games < num_teams -1:
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        while True:
            num_of_played_games = int(input("Enter The number of games Played by each team: "))
            if num_of_played_games >= num_teams -1:
                break
            else:
                print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
    return num_of_played_games


num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)

print("Generating the games to be played in the first round of the tournament...")
