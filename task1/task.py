players_path = './data/test_A/players.txt'
teams_path = './data/test_A/teams.txt'
result_path = './data/test_A/test_A_pairs.txt'


def read_players_from_file(file_path):
    players = {}
    with open(file_path, 'r') as file:
        for line in file:
            items = line.split()
            player_id = items[0]
            player_score = int(items[1])
            players[player_id] = player_score
    return players


def read_teams_from_file(file_path):
    teams = {}
    with open(file_path, 'r') as file:
        for line in file:
            items = line.split()
            team_id = items[0]
            player_ids = items[1:]
            teams[team_id] = player_ids
    return teams


def write_scores_to_file(filepath, scores):
    with open(filepath, 'w') as file:
        for index in range(len(scores)//2):
            file.write("{} {}".format(scores[index*2][0], scores[index*2 + 1][0]))

def calculate_team_scores(teams, players):
    team_scores = {}
    for team_id, player_ids in teams.items():
        team_scores[team_id] = sum([players[player_id] for player_id in player_ids])
    return team_scores


players = read_players_from_file(players_path)
teams = read_teams_from_file(teams_path)
team_scores = calculate_team_scores(teams, players)
sorted_team_scores = sorted(team_scores.items(), key=lambda x: x[1], reverse=True)
write_scores_to_file(result_path, sorted_team_scores)