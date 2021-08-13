import requests

# when a user logs in
# GET request to https://fantasy.premierleague.com/api/my-team/ {user's team id} / endpoint for users current VI (no player web names included just player ids)
# GET request to https://fantasy.premierleague.com/api/bootstrap-static/ endpoint for all footballers and their stats (user this endpoint to match player ids from above to get names and other data)
# GET request to https://fantasy.premierleague.com/api/entry/ {user's team id} / for user's peronal info (ex: user's team name, overall rank in fantasy, overall rank in user's classic league, etc...)
# these 3 GET requests should provide enough information to create the user's profile
# create a user's profile and import it into app.py for use
user = {
    'team_name': '',
    'fav_team': '',
    'fav_team_ids': '',
    'fav_team_logo': '',
    'fav_team_colors': '',
    'fav_team_jersey': '',
    'fav_team_jersey_goal': '',
    'classic_league_id': '',
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
position1 = []
jersey_list = [
    {
        'id': 1,
        'name': 'Arsenal',
        'colors': '#EF0107',
        'logo': '\static\img\logos\ars.png',
        'jersey': '\static\img\jerseys\shirt_3-66_ars.webp',
        'jersey_goal': '\static\img\jerseys\arsg.webp'
    },
    {
        'id': 2,
        'name': 'Aston Villa',
        'colors': '#670E36',
        'logo': '\static\img\logos\logo_avl.png',
        'jersey': '\static\img\jerseys\shirt_7-66_avl.webp',
        'jersey_goal': '\static\img\jerseys\avlg.webp'
    },
    {
        'id': 3,
        'name': 'Brentford',
        'colors': '#e30613',
        'logo': '\static\img\logos\bre.png',
        'jersey': '\static\img\jerseys\bre.webp',
        'jersey_goal': '\static\img\jerseys\breg.webp'
    },
    {
        'id': 4,
        'name': 'Brigton Hove Albion',
        'colors': '#0057B8',
        'logo': '\static\img\logos\bha.png',
        'jersey': '\static\img\jerseys\shirt_36-66_bha.webp',
        'jersey_goal': '\static\img\jerseys\shirt_90_1-66_bur_g.webp'
    },
    {
        'id': 5,
        'name': 'Burnley',
        'colors': '#6C1D45',
        'logo': '\static\img\logos\bur.png',
        'jersey': '\static\img\jerseys\shirt_90-66_bur.webp',
        'jersey_goal': '\static\img\jerseys\shirt_90_1-66_burg.webp'
    },
    {
        'id': 6,
        'name': 'Chelsea',
        'colors': '#034694',
        'logo': '\static\img\logos\che.png',
        'jersey': '\static\img\jerseys\che.webp',
        'jersey_goal': '\static\img\jerseys\cheg.webp',
        'fixtures': [
            {
                'status': 'next',
                'opponent': 'CRY',
                'location': 'H'
            },
            {
                'status': 'pending',
                'opponent': 'ARS',
                'location': 'A'
            },
            {
                'status': 'pending',
                'opponent': 'LIV',
                'location': 'A'
            },
            {
                'status': 'pending',
                'opponent': 'AVL',
                'location': 'H'
            },
            {
                'status': 'pending',
                'opponent': 'TOT',
                'location': 'A'
            },
            {
                'status': 'pending',
                'opponent': 'MCY',
                'location': 'H'
            },
            {
                'status': 'pending',
                'opponent': 'SOU',
                'location': 'H'
            },
            {
                'status': 'pending',
                'opponent': 'BRE',
                'location': 'A'
            },
            {
                'status': 'pending',
                'opponent': 'NOR',
                'location': 'H'
            },

        ]
    },
    {
        'id': 7,
        'name': 'Crystal Palace',
        'colors': '#1B458F',
        'logo': '\static\img\logos\cry.png',
        'jersey': '\static\img\jerseys\cry.webp',
        'jersey_goal': '\static\img\jerseys\cryg.webp'
    },
    {
        'id': 8,
        'name': 'Everton',
        'colors': '#003399',
        'logo': '\static\img\logos\eve.png',
        'jersey': '\static\img\jerseys\eve.webp',
        'jersey_goal': '\static\img\jerseys\eveg.webp'
    },
    {
        'id': 9,
        'name': 'Leicester City',
        'colors': '#003090',
        'logo': '\static\img\logos\lei.png',
        'jersey': '\static\img\jerseys\lei.webp',
        'jersey_goal': '\static\img\jerseys\leig.webp'
    },
    {
        'id': 10,
        'name': 'Leeds United',
        'colors': '#FFCD00',
        'logo': '\static\img\logos\lee.png',
        'jersey': '\static\img\jerseys\lee.webp',
        'jersey_goal': '\static\img\jerseys\leeg.webp'
    },
    {
        'id': 11,
        'name': 'Liverpool',
        'colors': '#C8102E',
        'logo': '\static\img\logos\liv.png',
        'jersey': '\static\img\jerseys\liv.webp',
        'jersey_goal': '\static\img\jerseys\livg.webp'
    },
    {
        'id': 12,
        'name': 'Manchester City',
        'colors': '#6CABDD',
        'logo': '\static\img\logos\mcy.png',
        'jersey': '\static\img\jerseys\mci.webp',
        'jersey_goal': '\static\img\jerseys\mcig.webp'
    },
    {
        'id': 13,
        'name': 'Manchester United',
        'colors': '#DA291C',
        'logo': '\static\img\logos\mnu.png',
        'jersey': '\static\img\jerseys\mun.webp',
        'jersey_goal': '\static\img\jerseys\mung.webp'
    },
    {
        'id': 14,
        'name': 'Newcastle United',
        'colors': '#41B6E6',
        'logo': '\static\img\logos\new.png',
        'jersey': '\static\img\jerseys\shirt_4-66_new.webp',
        'jersey_goal': '\static\img\jerseys\newg.webp'
    },
    {
        'id': 15,
        'name': 'Norwich City',
        'colors': '#00A650',
        'logo': '\static\img\logos\nor.png',
        'jersey': '\static\img\jerseys\nor.webp',
        'jersey_goal': '\static\img\jerseys\norg.webp'
    },
    {
        'id': 16,
        'name': 'Southampton',
        'colors': '#D71920',
        'logo': '\static\img\logos\sou.png',
        'jersey': '\static\img\jerseys\sou.webp',
        'jersey_goal': '\static\img\jerseys\soug.webp'
    },
    {
        'id': 17,
        'name': 'Tottenham',
        'colors': '#132257',
        'logo': '\static\img\logos\spurs.png',
        'jersey': '\static\img\jerseys\shirt_6-66_tot.webp',
        'jersey_goal': '\static\img\jerseys\totg.webp'
    },
    {
        'id': 18,
        'name': 'Watford',
        'colors': '#FBEE23',
        'logo': '\static\img\logos\wat.png',
        'jersey': '\static\img\jerseys\wat.webp',
        'jersey_goal': '\static\img\jerseys\watg.webp'
    },
    {
        'id': 19,
        'name': 'West Ham United',
        'colors': '#4F0E0E',
        'logo': '\static\img\logos\whu.png',
        'jersey': '\static\img\jerseys\whu.webp',
        'jersey_goal': '\static\img\jerseys\whug.webp'
    },
    {
        'id': 20,
        'name': 'Wolverhampton',
        'colors': '#F9B208',
        'logo': '\static\img\logos\wol.png',
        'jersey': '\static\img\jerseys\wol.webp',
        'jersey_goal': '\static\img\jerseys\wolg.webp'
    }
]


def users_11(email, password, team_id):
    team_id = str(team_id)
    # put the cookies received in session to be remembered
    session = requests.session()

    # url needed to make the post request
    url = 'https://users.premierleague.com/accounts/login/'

    # data needed for the post request
    payload = {
     'password': password,
     'login': email,
     'redirect_uri': 'https://fantasy.premierleague.com/a/login',
     'app': 'plfpl-web'
    }
    session.post(url, data=payload)

    # Get response sent with authorization cookies
    res = session.get('https://fantasy.premierleague.com/api/my-team/' + team_id + '/')

    # setting the response to a var called 'data' and making the response json
    data = res.json()

    starting_vi.append(data['picks'])
    #starting_vi = data['picks']

    #return data['picks']

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

    # filter the best players for transfers suggestions
    # position 1
    for x in data['elements']:
        if x['element_type'] == 1:
            if x['total_points'] > user['players'][0]['total_points'] and x['web_name'] != user['players'][0]['web_name'] and x['web_name'] != user['players'][12]['web_name']:
                position1.append(x['web_name'])
            else:
                position1.append("No Suggestions at this time")


def user_personal_info(team_id):
    team_id = str(team_id)
    res = requests.get('https://fantasy.premierleague.com/api/entry/' + team_id + '/')
    data = res.json()

    # disect get response
    user['team_name'] = data['name']
    user['fav_team'] = data['leagues']['classic'][0]["name"]
    user['fav_team_id'] = data['leagues']['classic'][0]["id"]
    user['overall_points'] = data['summary_overall_points']
    user['gameweek_points'] = data['summary_event_points']
    user['gameweek_rank'] = data['summary_event_rank']
    user['overall_rank'] = data['summary_overall_rank']
    user['classic_league_id'] = data['leagues']['classic'][4]["id"]
    user['classic_league_name'] = data['leagues']['classic'][4]["name"]
    user['classic_league_rank'] = data['leagues']['classic'][4]['entry_rank']
    user['classic_league_rank_previous'] = data['leagues']['classic'][4]['entry_last_rank']

    for x in jersey_list:
        if x['id'] == user['fav_team_id']:
            user['fav_team_logo'] = x['logo']
            user['fav_team_colors'] = x['colors']
            user['fav_team_jersey'] = x['jersey']
            user['fav_team_jersey_goal'] = x['jersey_goal']


def classic_league_standings(cl_id):
    id = str(cl_id)
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

# run method
make_user_profile('cunheez3@gmail.com', 'Tottenham7', 307976)
# make_user_profile('jan6person@hotmail.com', 'Winter2011', 709137)
#make_user_profile('fplexampleman@gmail.com', 'Tottenham7', 1583773)
# 'fplexampleman@gmail.com', 'Tottenham7', 1583773
# classic league id -- 71437
print(user['fav_team'])
print(user['fav_team_id'])
