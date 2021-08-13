import requests

transfer_suggestions = {
    'keeper': {
        'players': [],
        'average_ppg': [],
        'average_cost': [],
        'minutes': [],
        'suggested_keepers': []
    },
    'defense': {
        'players': [],
        'average_ppg': [],
        'average_cost': [],
        'minutes': [],
        'suggested_defenders': []
    },
    'midfield': {
        'players': [],
        'average_ppg': [],
        'average_cost': [],
        'minutes': [],
        'suggested_midielders': []
    },
    'forwards': {
        'players': [],
        'average_ppg': [],
        'average_cost': [],
        'minutes': [],
        'suggested_forwards': []
    },
}
# GET all footballers in fpl
def assistant_suggestions():
    res = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    data = res.json()

    # collect team information
    teams = data['teams']

    # collect player information
    players = data['elements']

    # FIND THE PLAYERS WITH THE MOST POINTS/GM AND LOWEST AVERAGE PLAYER COST
    #1 put players into their respective positions (goalkeeper, defender ...)
    for player in players:
        # keepers
        if player['element_type'] == 1 and player['points_per_game'] != '0.0':
            transfer_suggestions['keeper']['players'].append(player)

        # defenders
        if player['element_type'] == 2 and player['points_per_game'] != '0.0':
            transfer_suggestions['defense']['players'].append(player)

        # midfielders
        if player['element_type'] == 3 and player['points_per_game'] != '0.0':
            transfer_suggestions['midfield']['players'].append(player)

        # forwards
        if player['element_type'] == 4 and player['points_per_game'] != '0.0':
            transfer_suggestions['forwards']['players'].append(player)

    #2 find the pts/gm - cost - minutes average for players with points

    # KEEPERS
    for player in transfer_suggestions['keeper']['players']:
        transfer_suggestions['keeper']['average_ppg'].append(float(player['points_per_game']))
        transfer_suggestions['keeper']['average_cost'].append(player['now_cost'])
        transfer_suggestions['keeper']['minutes'].append(player['minutes'])
    transfer_suggestions['keeper']['average_ppg'] = round(sum(transfer_suggestions['keeper']['average_ppg']) / len(transfer_suggestions['keeper']['average_ppg']), 1)
    transfer_suggestions['keeper']['average_cost'] = round(sum(transfer_suggestions['keeper']['average_cost']) / len(transfer_suggestions['keeper']['average_cost']), 1)
    transfer_suggestions['keeper']['average_cost'] = round((transfer_suggestions['keeper']['average_cost'] * 0.1),1)
    transfer_suggestions['keeper']['minutes'] = round(sum(transfer_suggestions['keeper']['minutes']) / len(transfer_suggestions['keeper']['minutes']))
    for player in transfer_suggestions['keeper']['players']:
        if float(player['points_per_game']) >= transfer_suggestions['keeper']['average_ppg'] and player['minutes'] >= transfer_suggestions['keeper']['minutes']:
             transfer_suggestions['keeper']['suggested_keepers'].append(player)

    # DEFNEDERS
    for player in transfer_suggestions['defense']['players']:
        transfer_suggestions['defense']['average_ppg'].append(float(player['points_per_game']))
        transfer_suggestions['defense']['average_cost'].append(player['now_cost'])
        transfer_suggestions['defense']['minutes'].append(player['minutes'])
    transfer_suggestions['defense']['average_ppg'] = round(sum(transfer_suggestions['defense']['average_ppg']) / len(transfer_suggestions['defense']['average_ppg']), 1)
    transfer_suggestions['defense']['average_cost'] = round(sum(transfer_suggestions['defense']['average_cost']) / len(transfer_suggestions['defense']['average_cost']), 1)
    transfer_suggestions['defense']['average_cost'] = round((transfer_suggestions['defense']['average_cost'] * 0.1),1)
    transfer_suggestions['defense']['minutes'] = round(sum(transfer_suggestions['defense']['minutes']) / len(transfer_suggestions['defense']['minutes']))
    for player in transfer_suggestions['defense']['players']:
        if float(player['points_per_game']) >= transfer_suggestions['defense']['average_ppg'] and player['minutes'] >= transfer_suggestions['defense']['minutes']:
             transfer_suggestions['defense']['suggested_defenders'].append(player)

    # MIDFIELDERS
    for player in transfer_suggestions['midfield']['players']:
        transfer_suggestions['midfield']['average_ppg'].append(float(player['points_per_game']))
        transfer_suggestions['midfield']['average_cost'].append(player['now_cost'])
        transfer_suggestions['midfield']['minutes'].append(player['minutes'])
    transfer_suggestions['midfield']['average_ppg'] = round(sum(transfer_suggestions['midfield']['average_ppg']) / len(transfer_suggestions['midfield']['average_ppg']), 1)
    transfer_suggestions['midfield']['average_cost'] = round(sum(transfer_suggestions['midfield']['average_cost']) / len(transfer_suggestions['midfield']['average_cost']), 1)
    transfer_suggestions['midfield']['average_cost'] = round((transfer_suggestions['midfield']['average_cost'] * 0.1),1)
    transfer_suggestions['midfield']['minutes'] = round(sum(transfer_suggestions['midfield']['minutes']) / len(transfer_suggestions['midfield']['minutes']))
    for player in transfer_suggestions['midfield']['players']:
        if float(player['points_per_game']) >= transfer_suggestions['midfield']['average_ppg'] and player['minutes'] >= transfer_suggestions['midfield']['minutes']:
             transfer_suggestions['midfield']['suggested_midielders'].append(player)

    # FORWARDS
    for player in transfer_suggestions['forwards']['players']:
        transfer_suggestions['forwards']['average_ppg'].append(float(player['points_per_game']))
        transfer_suggestions['forwards']['average_cost'].append(player['now_cost'])
        transfer_suggestions['forwards']['minutes'].append(player['minutes'])
    transfer_suggestions['forwards']['average_ppg'] = round(sum(transfer_suggestions['forwards']['average_ppg']) / len(transfer_suggestions['forwards']['average_ppg']), 1)
    transfer_suggestions['forwards']['average_cost'] = round(sum(transfer_suggestions['forwards']['average_cost']) / len(transfer_suggestions['forwards']['average_cost']), 1)
    transfer_suggestions['forwards']['average_cost'] = round((transfer_suggestions['forwards']['average_cost'] * 0.1),1)
    transfer_suggestions['forwards']['minutes'] = round(sum(transfer_suggestions['forwards']['minutes']) / len(transfer_suggestions['forwards']['minutes']))
    for player in transfer_suggestions['forwards']['players']:
        if float(player['points_per_game']) >= transfer_suggestions['forwards']['average_ppg'] and player['minutes'] >= transfer_suggestions['forwards']['minutes']:
             transfer_suggestions['forwards']['suggested_forwards'].append(player)





# assistant_suggestions()

#print("KEEPER STATS")
#print(transfer_suggestions['keeper']['average_ppg'])
#print(transfer_suggestions['keeper']['average_cost'])
#print(transfer_suggestions['keeper']['minutes'])
#print("Suggested Goalkeepers")
#print(transfer_suggestions['keeper']['suggested_keepers'][0]['web_name'])
#print(transfer_suggestions['keeper']['suggested_keepers'][1]['web_name'])
#print(transfer_suggestions['keeper']['suggested_keepers'][2]['web_name'])
#print(transfer_suggestions['keeper']['suggested_keepers'][3]['web_name'])
#print(transfer_suggestions['keeper']['suggested_keepers'][4]['web_name'])
#print(transfer_suggestions['keeper']['suggested_keepers'][5]['web_name'])
#print('')

#print("DEFENDERS STATS")
#print(transfer_suggestions['defense']['average_ppg'])
#print(transfer_suggestions['defense']['average_cost'])
#print(transfer_suggestions['defense']['minutes'])
#print("Suggested Defenders")
#print(transfer_suggestions['defense']['suggested_defenders'][0]['web_name'])
#print(transfer_suggestions['defense']['suggested_defenders'][1]['web_name'])
#print(transfer_suggestions['defense']['suggested_defenders'][2]['web_name'])
#print(transfer_suggestions['defense']['suggested_defenders'][3]['web_name'])
#print(transfer_suggestions['defense']['suggested_defenders'][4]['web_name'])
#print(transfer_suggestions['defense']['suggested_defenders'][5]['web_name'])
#print('')

#print("MIDFIELDERS STATS")
#print(transfer_suggestions['midfield']['average_ppg'])
#print(transfer_suggestions['midfield']['average_cost'])
#print(transfer_suggestions['midfield']['minutes'])
#print("Suggested Midfielders")
#print(transfer_suggestions['midfield']['suggested_midielders'][0]['web_name'])
#print(transfer_suggestions['midfield']['suggested_midielders'][1]['web_name'])
#print(transfer_suggestions['midfield']['suggested_midielders'][2]['web_name'])
#print(transfer_suggestions['midfield']['suggested_midielders'][3]['web_name'])
#print(transfer_suggestions['midfield']['suggested_midielders'][5]['web_name'])
#print(transfer_suggestions['midfield']['suggested_midielders'][4]['web_name'])
#print('')

#print("FORWARDS STATS")
#print(transfer_suggestions['forwards']['average_ppg'])
#print(transfer_suggestions['forwards']['average_cost'])
#print(transfer_suggestions['forwards']['minutes'])
#print("Suggested Midfielders")
#print(transfer_suggestions['forwards']['suggested_forwards'][0]['web_name'])
#print(transfer_suggestions['forwards']['suggested_forwards'][1]['web_name'])
#print(transfer_suggestions['forwards']['suggested_forwards'][2]['web_name'])
#print(transfer_suggestions['forwards']['suggested_forwards'][3]['web_name'])
#print(transfer_suggestions['forwards']['suggested_forwards'][4]['web_name'])
#print(transfer_suggestions['forwards']['suggested_forwards'][5]['web_name'])
#print('')
