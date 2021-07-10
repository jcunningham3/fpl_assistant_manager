import requests

# when a user logs in
# GET request to https://fantasy.premierleague.com/api/my-team/ {user's team id} / endpoint for users current VI (no player web names included just player ids)
# GET request to https://fantasy.premierleague.com/api/bootstrap-static/ endpoint for all footballers and their stats (user this endpoint to match player ids from above to get names and other data)
# GET request to https://fantasy.premierleague.com/api/entry/ {user's team id} / for user's peronal info (ex: user's team name, overall rank in fantasy, overall rank in user's classic league, etc...)
# these 3 GET requests should provide enough information to create the user's profile
# create a user's profile and import it into app.py for use
user = {
    'team_name': '',
    'overall_points': '',
    'gameweek_points': '',
    'gameweek_rank': '',
    'overall_rank': '',
    'classic_league_name': '',
    'classic_league_rank': '',
    'classic_league_rank_previous': '',
    'transfers': {
        'cost': '',
        'status': '',
        'limit': '',
        'made': '',
        'bank': '',
        'value': '',
    },
    'players': [
        {
            'position': 1,
            'selling_price': 0,
            'purchase_price': 0,
            'is_captain': False,
            'is_vice_captain': False,
            'multiplier': 0,
            'element': 0,

            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 2,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 3,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 4,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 5,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 6,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 7,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 8,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 9,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 10,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 11,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 12,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 13,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 14,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',
            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        },
        {
            'position': 15,
            'selling_price': '',
            'purchase_price': '',
            'is_captain': '',
            'is_vice_captain': '',
            'multiplier': '',
            'element': '',

            "chance_of_playing_next_round": '',
            "chance_of_playing_this_round": '',
            "code": '',
            "cost_change_event": '',
            "cost_change_event_fall": '',
            "cost_change_start": '',
            "cost_change_start_fall": '',
            "dreamteam_count": '',
            "element_type": '',
            "ep_next": "",
            "ep_this": '',
            "event_points": '',
            "first_name": "",
            "form": "0.0",
            "id": '',
            "in_dreamteam": '',
            "news": "",
            "news_added": '',
            "now_cost": '',
            "photo": "",
            "points_per_game": "",
            "second_name": "",
            "selected_by_percent": "",
            "special": '',
            "squad_number": '',
            "status": "",
            "team": '',
            "team_code": '',
            "total_points": '',
            "transfers_in": '',
            "transfers_in_event": '',
            "transfers_out": '',
            "transfers_out_event": '',
            "value_form": "",
            "value_season": "",
            "web_name": "",
            "minutes": '',
            "goals_scored": '',
            "assists": '',
            "clean_sheets": '',
            "goals_conceded": '',
            "own_goals": '',
            "penalties_saved": '',
            "penalties_missed": '',
            "yellow_cards": '',
            "red_cards": '',
            "saves": '',
            "bonus": '',
            "bps": '',
            "influence": "",
            "creativity": "",
            "threat": "",
            "ict_index": "",
            "influence_rank": '',
            "influence_rank_type": '',
            "creativity_rank": '',
            "creativity_rank_type": '',
            "threat_rank": '',
            "threat_rank_type": '',
            "ict_index_rank": '',
            "ict_index_rank_type": ''
        }
    ]
}
starting_vi = []

def users_11(email, pwd, team_id):
    user = email
    user_password = pwd
    team_id = str(team_id)
    s = requests.Session()
   #request authorization from the app
    headers = {
       'authority': 'users.premierleague.com' ,
       'cache-control': 'max-age=0' ,
       'upgrade-insecure-requests': '1' ,
       'origin': 'https://fantasy.premierleague.com' ,
       'content-type': 'application/x-www-form-urlencoded' ,
       'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' ,
       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
       'sec-fetch-site': 'same-site' ,
       'sec-fetch-mode': 'navigate' ,
       'sec-fetch-user': '?1' ,
       'sec-fetch-dest': 'document' ,
       'referer': 'https://fantasy.premierleague.com/my-team' ,
       'accept-language': 'en-US,en;q=0.9,he;q=0.8' ,
    }
    data = {
        "login": user,
        "password": user_password,
        "app": "plfpl-web",
        "redirect_uri": "https://fantasy.premierleague.com/"
    }
    url = "https://users.premierleague.com/accounts/login/"
    res = s.post(url, data = data,  headers = headers)

    team_url = "https://fantasy.premierleague.com/api/my-team/" + team_id + "/"
    res = s.get(team_url)
    data = res.json()
    starting_vi.append(data['picks'])
def all_footballers():
    res = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    data = res.json()

    # update the rest of the users player's info
    for x in data['elements']:
        for player in user['players']:
            if x['id'] == player['element']:
                player['chance_of_playing_this_round'] = x['chance_of_playing_this_round']
                player['chance_of_playing_next_round'] = x['chance_of_playing_next_round']
                player['code'] = x['code']
                player['cost_change_event'] = x['cost_change_event']
                player['cost_change_event_fall'] = x['cost_change_event_fall']
                player['cost_change_start'] = x['cost_change_start']
                player['cost_change_start_fall'] = x['cost_change_start_fall']
                player['dreamteam_count'] = x['dreamteam_count']
                player['element_type'] = x['element_type']
                player['ep_next'] = x['ep_next']
                player['ep_this'] = x['ep_this']
                player['event_points'] = x['event_points']
                player['first_name'] = x['first_name']
                player['second_name'] = x['second_name']
                player['form'] = x['form']
                player['id'] = x['id']
                player['in_dreamteam'] = x['in_dreamteam']
                player['news'] = x['news']
                player['news_added'] = x['news_added']
                player['now_cost'] = x['now_cost']
                player['points_per_game'] = x['points_per_game']
                player['selected_by_percent'] = x['selected_by_percent']
                player['special'] = x['special']
                player['squad_number'] = x['squad_number']
                player['status'] = x['status']
                player['team'] = x['team']
                player['team_code'] = x['team_code']
                player['total_points'] = x['total_points']
                player['transfers_in'] = x['transfers_in']
                player['transfers_in_event'] = x['transfers_in_event']
                player['transfers_out'] = x['transfers_out']
                player['transfers_out_event'] = x['transfers_out_event']
                player['value_form'] = x['value_form']
                player['value_season'] = x['value_season']
                player['web_name'] = x['web_name']
                player['minutes'] = x['minutes']
                player['goals_scored'] = x['goals_scored']
                player['assists'] = x['assists']
                player['clean_sheets'] = x['clean_sheets']
                player['goals_conceded'] = x['goals_conceded']
                player['own_goals'] = x['own_goals']
                player['penalties_saved'] = x['penalties_saved']
                player['penalties_missed'] = x['penalties_missed']
                player['yellow_cards'] = x['yellow_cards']
                player['red_cards'] = x['red_cards']
                player['saves'] = x['saves']
                player['bonus'] = x['bonus']
                player['bps'] = x['bps']
                player['influence'] = x['influence']
                player['creativity'] = x['creativity']
                player['threat'] = x['threat']
                player['ict_index'] = x['ict_index']
                player['influence_rank'] = x['influence_rank']
                player['influence_rank_type'] = x['influence_rank_type']
                player['creativity_rank'] = x['creativity_rank']
                player['creativity_rank_type'] = x['creativity_rank_type']
                player['threat_rank'] = x['threat_rank']
                player['threat_rank_type'] = x['threat_rank_type']
                player['ict_index_rank'] = x['ict_index_rank']
                player['ict_index_rank_type'] = x['ict_index_rank_type']
def user_personal_info(team_id):
    team_id = str(team_id)
    res = requests.get('https://fantasy.premierleague.com/api/entry/' + team_id + '/')
    data = res.json()

    # disect get response
    user['team_name'] = data['name']
    user['overall_points'] = data['summary_overall_points']
    user['gameweek_points'] = data['summary_event_points']
    user['gameweek_rank'] = data['summary_event_rank']
    user['overall_rank'] = data['summary_overall_rank']
    user['classic_league_name'] = data['leagues']['classic'][4]['name']
    user['classic_league_rank'] = data['leagues']['classic'][4]['entry_rank']
    user['classic_league_rank_previous'] = data['leagues']['classic'][4]['entry_last_rank']
def classic_league_standings(classic_league_id):
    id = str(classic_league_id)
    res = requests.get('https://fantasy.premierleague.com/api/leagues-classic/' + id + '/standings/')
    data = res.json()
    return data

# build the users profile
def make_user_profile(email, password, team_id):

    # get users's 15 players
    users_11( email, password, team_id)

    # get users profile info
    user_personal_info(team_id)

    # update user's player info with all data from this endpoint
    for x in starting_vi[0]:
        # position 1
        if x['position'] == 1:
            user['players'][0]['element'] = x['element']
            user['players'][0]['purchase_price'] = x['purchase_price']
            user['players'][0]['selling_price'] = x['selling_price']
            user['players'][0]['multiplier'] = x['multiplier']
            user['players'][0]['is_captain'] = x['is_captain']
            user['players'][0]['is_vice_captain'] = x['is_vice_captain']
        # position 2
        if x['position'] == 2:
            user['players'][1]['element'] = x['element']
            user['players'][1]['purchase_price'] = x['purchase_price']
            user['players'][1]['selling_price'] = x['selling_price']
            user['players'][1]['multiplier'] = x['multiplier']
            user['players'][1]['is_captain'] = x['is_captain']
            user['players'][1]['is_vice_captain'] = x['is_vice_captain']
        # position 3
        if x['position'] == 3:
            user['players'][2]['element'] = x['element']
            user['players'][2]['purchase_price'] = x['purchase_price']
            user['players'][2]['selling_price'] = x['selling_price']
            user['players'][2]['multiplier'] = x['multiplier']
            user['players'][2]['is_captain'] = x['is_captain']
            user['players'][2]['is_vice_captain'] = x['is_vice_captain']
        # position 4
        if x['position'] == 4:
            user['players'][3]['element'] = x['element']
            user['players'][3]['purchase_price'] = x['purchase_price']
            user['players'][3]['selling_price'] = x['selling_price']
            user['players'][3]['multiplier'] = x['multiplier']
            user['players'][3]['is_captain'] = x['is_captain']
            user['players'][3]['is_vice_captain'] = x['is_vice_captain']
        # position 5
        if x['position'] == 5:
            user['players'][4]['element'] = x['element']
            user['players'][4]['purchase_price'] = x['purchase_price']
            user['players'][4]['selling_price'] = x['selling_price']
            user['players'][4]['multiplier'] = x['multiplier']
            user['players'][4]['is_captain'] = x['is_captain']
            user['players'][4]['is_vice_captain'] = x['is_vice_captain']
        # position 6
        if x['position'] == 6:
            user['players'][5]['element'] = x['element']
            user['players'][5]['purchase_price'] = x['purchase_price']
            user['players'][5]['selling_price'] = x['selling_price']
            user['players'][5]['multiplier'] = x['multiplier']
            user['players'][5]['is_captain'] = x['is_captain']
            user['players'][5]['is_vice_captain'] = x['is_vice_captain']
        # position 7
        if x['position'] == 7:
            user['players'][6]['element'] = x['element']
            user['players'][6]['purchase_price'] = x['purchase_price']
            user['players'][6]['selling_price'] = x['selling_price']
            user['players'][6]['multiplier'] = x['multiplier']
            user['players'][6]['is_captain'] = x['is_captain']
            user['players'][6]['is_vice_captain'] = x['is_vice_captain']
        # position 8
        if x['position'] == 8:
            user['players'][7]['element'] = x['element']
            user['players'][7]['purchase_price'] = x['purchase_price']
            user['players'][7]['selling_price'] = x['selling_price']
            user['players'][7]['multiplier'] = x['multiplier']
            user['players'][7]['is_captain'] = x['is_captain']
            user['players'][7]['is_vice_captain'] = x['is_vice_captain']
        # position 9
        if x['position'] == 9:
            user['players'][8]['element'] = x['element']
            user['players'][8]['purchase_price'] = x['purchase_price']
            user['players'][8]['selling_price'] = x['selling_price']
            user['players'][8]['multiplier'] = x['multiplier']
            user['players'][8]['is_captain'] = x['is_captain']
            user['players'][8]['is_vice_captain'] = x['is_vice_captain']
        # position 10
        if x['position'] == 10:
            user['players'][9]['element'] = x['element']
            user['players'][9]['purchase_price'] = x['purchase_price']
            user['players'][9]['selling_price'] = x['selling_price']
            user['players'][9]['multiplier'] = x['multiplier']
            user['players'][9]['is_captain'] = x['is_captain']
            user['players'][9]['is_vice_captain'] = x['is_vice_captain']
        # position 11
        if x['position'] == 11:
            user['players'][10]['element'] = x['element']
            user['players'][10]['purchase_price'] = x['purchase_price']
            user['players'][10]['selling_price'] = x['selling_price']
            user['players'][10]['multiplier'] = x['multiplier']
            user['players'][10]['is_captain'] = x['is_captain']
            user['players'][10]['is_vice_captain'] = x['is_vice_captain']
        # position 12
        if x['position'] == 12:
            user['players'][11]['element'] = x['element']
            user['players'][11]['purchase_price'] = x['purchase_price']
            user['players'][11]['selling_price'] = x['selling_price']
            user['players'][11]['multiplier'] = x['multiplier']
            user['players'][11]['is_captain'] = x['is_captain']
            user['players'][11]['is_vice_captain'] = x['is_vice_captain']
        # position 13
        if x['position'] == 13:
            user['players'][12]['element'] = x['element']
            user['players'][12]['purchase_price'] = x['purchase_price']
            user['players'][12]['selling_price'] = x['selling_price']
            user['players'][12]['multiplier'] = x['multiplier']
            user['players'][12]['is_captain'] = x['is_captain']
            user['players'][12]['is_vice_captain'] = x['is_vice_captain']
        # position 14
        if x['position'] == 14:
            user['players'][13]['element'] = x['element']
            user['players'][13]['purchase_price'] = x['purchase_price']
            user['players'][13]['selling_price'] = x['selling_price']
            user['players'][13]['multiplier'] = x['multiplier']
            user['players'][13]['is_captain'] = x['is_captain']
            user['players'][13]['is_vice_captain'] = x['is_vice_captain']
        # position 15
        if x['position'] == 15:
            user['players'][14]['element'] = x['element']
            user['players'][14]['purchase_price'] = x['purchase_price']
            user['players'][14]['selling_price'] = x['selling_price']
            user['players'][14]['multiplier'] = x['multiplier']
            user['players'][14]['is_captain'] = x['is_captain']
            user['players'][14]['is_vice_captain'] = x['is_vice_captain']

    # update the rest of the user's player info with all data from this endpoint
    all_footballers()

    print(user['team_name'])
    print(user['players'][0]['web_name'])

# run method
#make_user_profile('cunheez3@gmail.com', 'Tottenham7', 307976)
#make_user_profile('jan6person@hotmail.com', 'Winter2011', 709137)
#print(user['players'][1]['web_name'])
