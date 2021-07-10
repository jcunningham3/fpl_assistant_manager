from flask import Flask, flash, request, redirect, render_template, session, g
from models import connect_db, db, Users, Chat
from forms import UserForm, ChatForm, LoginForm
from methods import user, make_user_profile, all_footballers, user_personal_info, starting_vi
from jersey_selection import jersey_list

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cap_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'crowBottom'

connect_db(app)

@app.route('/')
def home_route():
    return render_template('home.html')

# register a new user
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = UserForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        team_id = form.team_id.data

        #make the GET requests before password is hashed
        player = user
        make_user_profile(email, password, team_id)

        new_user = Users.register(email, password, team_id)
        new_user.team_name = user['team_name']
        new_user.overall_points = user['overall_points']
        new_user.gameweek_points = user['gameweek_points']
        new_user.classic_league_name = user['classic_league_name']
        new_user.classic_league_rank = user['classic_league_rank']
        new_user.classic_league_rank_previous = user['classic_league_rank_previous']

        # player 1
        new_user.p1_chance_of_playing_next_round = user['players'][0]['chance_of_playing_next_round']
        new_user.p1_chance_of_playing_this_round = user['players'][0]['chance_of_playing_this_round']
        new_user.p1_code = user['players'][0]['code']
        new_user.p1_cost_change_event = user['players'][0]['cost_change_event']
        new_user.p1_cost_change_event_fall = user['players'][0]['cost_change_event_fall']
        new_user.p1_cost_change_start = user['players'][0]['cost_change_start']
        new_user.p1_cost_change_start_fall = user['players'][0]['cost_change_start_fall']
        new_user.p1_dreamteam_count = user['players'][0]['dreamteam_count']
        new_user.p1_element_type = user['players'][0]['element_type']
        new_user.p1_ep_next = user['players'][0]['ep_next']
        new_user.p1_ep_this = user['players'][0]['ep_this']
        new_user.p1_event_points = user['players'][0]['event_points']
        new_user.p1_first_name = user['players'][0]['first_name']
        new_user.p1_form = user['players'][0]['form']
        new_user.p1_player_id = user['players'][0]['id']
        new_user.p1_in_dreamteam = user['players'][0]['in_dreamteam']
        new_user.p1_news = user['players'][0]['news']
        new_user.p1_news_added = user['players'][0]['news_added']
        new_user.p1_now_cost = user['players'][0]['now_cost']
        new_user.p1_photo = user['players'][0]['photo']
        new_user.p1_points_per_game = user['players'][0]['points_per_game']
        new_user.p1_second_name = user['players'][0]['second_name']
        new_user.p1_selected_by_percent = user['players'][0]['selected_by_percent']
        new_user.p1_special = user['players'][0]['special']
        new_user.p1_squad_number = user['players'][0]['squad_number']
        new_user.p1_status = user['players'][0]['status']
        new_user.p1_team = user['players'][0]['team']
        new_user.p1_team_code = user['players'][0]['team_code']
        new_user.p1_total_points = user['players'][0]['total_points']
        new_user.p1_transfers_in = user['players'][0]['transfers_in']
        new_user.p1_transfers_in_event = user['players'][0]['transfers_in_event']
        new_user.p1_transfers_out = user['players'][0]['transfers_out']
        new_user.p1_transfers_out_event = user['players'][0]['transfers_out_event']
        new_user.p1_value_form = user['players'][0]['value_form']
        new_user.p1_value_season = user['players'][0]['value_season']
        new_user.p1_web_name = user['players'][0]['web_name']
        new_user.p1_minutes = user['players'][0]['minutes']
        new_user.p1_goals_scored = user['players'][0]['goals_scored']
        new_user.p1_assists = user['players'][0]['assists']
        new_user.p1_clean_sheets = user['players'][0]['clean_sheets']
        new_user.p1_own_goals = user['players'][0]['own_goals']
        new_user.p1_penalties_saved = user['players'][0]['penalties_saved']
        new_user.p1_yellow_cards = user['players'][0]['yellow_cards']
        new_user.p1_red_cards = user['players'][0]['red_cards']
        new_user.p1_saves = user['players'][0]['saves']
        new_user.p1_bonus = user['players'][0]['bonus']
        new_user.p1_bps = user['players'][0]['bps']
        new_user.p1_influence = user['players'][0]['influence']
        new_user.p1_creativity = user['players'][0]['creativity']
        new_user.p1_threat = user['players'][0]['threat']
        new_user.p1_ict_index = user['players'][0]['ict_index']
        new_user.p1_influence_rank = user['players'][0]['influence_rank']
        new_user.p1_influence_rank_type = user['players'][0]['influence_rank_type']
        new_user.p1_creativity_rank = user['players'][0]['creativity_rank']
        new_user.p1_creativity_rank_type = user['players'][0]['creativity_rank_type']
        new_user.p1_threat_rank = user['players'][0]['threat_rank']
        new_user.p1_threat_rank_type = user['players'][0]['threat_rank_type']
        # player 2
        new_user.p2_chance_of_playing_next_round = user['players'][1]['chance_of_playing_next_round']
        new_user.p2_chance_of_playing_this_round = user['players'][1]['chance_of_playing_this_round']
        new_user.p2_code = user['players'][1]['code']
        new_user.p2_cost_change_event = user['players'][1]['cost_change_event']
        new_user.p2_cost_change_event_fall = user['players'][1]['cost_change_event_fall']
        new_user.p2_cost_change_start = user['players'][1]['cost_change_start']
        new_user.p2_cost_change_start_fall = user['players'][1]['cost_change_start_fall']
        new_user.p2_dreamteam_count = user['players'][1]['dreamteam_count']
        new_user.p2_element_type = user['players'][1]['element_type']
        new_user.p2_ep_next = user['players'][1]['ep_next']
        new_user.p2_ep_this = user['players'][1]['ep_this']
        new_user.p2_event_points = user['players'][1]['event_points']
        new_user.p2_first_name = user['players'][1]['first_name']
        new_user.p2_form = user['players'][1]['form']
        new_user.p2_player_id = user['players'][1]['id']
        new_user.p2_in_dreamteam = user['players'][1]['in_dreamteam']
        new_user.p2_news = user['players'][1]['news']
        new_user.p2_news_added = user['players'][1]['news_added']
        new_user.p2_now_cost = user['players'][1]['now_cost']
        new_user.p2_photo = user['players'][1]['photo']
        new_user.p2_points_per_game = user['players'][1]['points_per_game']
        new_user.p2_second_name = user['players'][1]['second_name']
        new_user.p2_selected_by_percent = user['players'][1]['selected_by_percent']
        new_user.p2_special = user['players'][1]['special']
        new_user.p2_squad_number = user['players'][1]['squad_number']
        new_user.p2_status = user['players'][1]['status']
        new_user.p2_team = user['players'][1]['team']
        new_user.p2_team_code = user['players'][1]['team_code']
        new_user.p2_total_points = user['players'][1]['total_points']
        new_user.p2_transfers_in = user['players'][1]['transfers_in']
        new_user.p2_transfers_in_event = user['players'][1]['transfers_in_event']
        new_user.p2_transfers_out = user['players'][1]['transfers_out']
        new_user.p2_transfers_out_event = user['players'][1]['transfers_out_event']
        new_user.p2_value_form = user['players'][1]['value_form']
        new_user.p2_value_season = user['players'][1]['value_season']
        new_user.p2_web_name = user['players'][1]['web_name']
        new_user.p2_minutes = user['players'][1]['minutes']
        new_user.p2_goals_scored = user['players'][1]['goals_scored']
        new_user.p2_assists = user['players'][1]['assists']
        new_user.p2_clean_sheets = user['players'][1]['clean_sheets']
        new_user.p2_own_goals = user['players'][1]['own_goals']
        new_user.p2_penalties_saved = user['players'][1]['penalties_saved']
        new_user.p2_yellow_cards = user['players'][1]['yellow_cards']
        new_user.p2_red_cards = user['players'][1]['red_cards']
        new_user.p2_saves = user['players'][1]['saves']
        new_user.p2_bonus = user['players'][1]['bonus']
        new_user.p2_bps = user['players'][1]['bps']
        new_user.p2_influence = user['players'][1]['influence']
        new_user.p2_creativity = user['players'][1]['creativity']
        new_user.p2_threat = user['players'][1]['threat']
        new_user.p2_ict_index = user['players'][1]['ict_index']
        new_user.p2_influence_rank = user['players'][1]['influence_rank']
        new_user.p2_influence_rank_type = user['players'][1]['influence_rank_type']
        new_user.p2_creativity_rank = user['players'][1]['creativity_rank']
        new_user.p2_creativity_rank_type = user['players'][1]['creativity_rank_type']
        new_user.p2_threat_rank = user['players'][1]['threat_rank']
        new_user.p2_threat_rank_type = user['players'][1]['threat_rank_type']
        # player 3
        new_user.p3_chance_of_playing_next_round = user['players'][2]['chance_of_playing_next_round']
        new_user.p3_chance_of_playing_this_round = user['players'][2]['chance_of_playing_this_round']
        new_user.p3_code = user['players'][2]['code']
        new_user.p3_cost_change_event = user['players'][2]['cost_change_event']
        new_user.p3_cost_change_event_fall = user['players'][2]['cost_change_event_fall']
        new_user.p3_cost_change_start = user['players'][2]['cost_change_start']
        new_user.p3_cost_change_start_fall = user['players'][2]['cost_change_start_fall']
        new_user.p3_dreamteam_count = user['players'][2]['dreamteam_count']
        new_user.p3_element_type = user['players'][2]['element_type']
        new_user.p3_ep_next = user['players'][2]['ep_next']
        new_user.p3_ep_this = user['players'][2]['ep_this']
        new_user.p3_event_points = user['players'][2]['event_points']
        new_user.p3_first_name = user['players'][2]['first_name']
        new_user.p3_form = user['players'][2]['form']
        new_user.p3_player_id = user['players'][2]['id']
        new_user.p3_in_dreamteam = user['players'][2]['in_dreamteam']
        new_user.p3_news = user['players'][2]['news']
        new_user.p3_news_added = user['players'][2]['news_added']
        new_user.p3_now_cost = user['players'][2]['now_cost']
        new_user.p3_photo = user['players'][2]['photo']
        new_user.p3_points_per_game = user['players'][2]['points_per_game']
        new_user.p3_second_name = user['players'][2]['second_name']
        new_user.p3_selected_by_percent = user['players'][2]['selected_by_percent']
        new_user.p3_special = user['players'][2]['special']
        new_user.p3_squad_number = user['players'][2]['squad_number']
        new_user.p3_status = user['players'][2]['status']
        new_user.p3_team = user['players'][2]['team']
        new_user.p3_team_code = user['players'][2]['team_code']
        new_user.p3_total_points = user['players'][2]['total_points']
        new_user.p3_transfers_in = user['players'][2]['transfers_in']
        new_user.p3_transfers_in_event = user['players'][2]['transfers_in_event']
        new_user.p3_transfers_out = user['players'][2]['transfers_out']
        new_user.p3_transfers_out_event = user['players'][2]['transfers_out_event']
        new_user.p3_value_form = user['players'][2]['value_form']
        new_user.p3_value_season = user['players'][2]['value_season']
        new_user.p3_web_name = user['players'][2]['web_name']
        new_user.p3_minutes = user['players'][2]['minutes']
        new_user.p3_goals_scored = user['players'][2]['goals_scored']
        new_user.p3_assists = user['players'][2]['assists']
        new_user.p3_clean_sheets = user['players'][2]['clean_sheets']
        new_user.p3_own_goals = user['players'][2]['own_goals']
        new_user.p3_penalties_saved = user['players'][2]['penalties_saved']
        new_user.p3_yellow_cards = user['players'][2]['yellow_cards']
        new_user.p3_red_cards = user['players'][2]['red_cards']
        new_user.p3_saves = user['players'][2]['saves']
        new_user.p3_bonus = user['players'][2]['bonus']
        new_user.p3_bps = user['players'][2]['bps']
        new_user.p3_influence = user['players'][2]['influence']
        new_user.p3_creativity = user['players'][2]['creativity']
        new_user.p3_threat = user['players'][2]['threat']
        new_user.p3_ict_index = user['players'][2]['ict_index']
        new_user.p3_influence_rank = user['players'][2]['influence_rank']
        new_user.p3_influence_rank_type = user['players'][2]['influence_rank_type']
        new_user.p3_creativity_rank = user['players'][2]['creativity_rank']
        new_user.p3_creativity_rank_type = user['players'][2]['creativity_rank_type']
        new_user.p3_threat_rank = user['players'][2]['threat_rank']
        new_user.p3_threat_rank_type = user['players'][2]['threat_rank_type']

        # player 3
        new_user.p4_chance_of_playing_next_round = user['players'][3]['chance_of_playing_next_round']
        new_user.p4_chance_of_playing_this_round = user['players'][3]['chance_of_playing_this_round']
        new_user.p4_code = user['players'][3]['code']
        new_user.p4_cost_change_event = user['players'][3]['cost_change_event']
        new_user.p4_cost_change_event_fall = user['players'][3]['cost_change_event_fall']
        new_user.p4_cost_change_start = user['players'][3]['cost_change_start']
        new_user.p4_cost_change_start_fall = user['players'][3]['cost_change_start_fall']
        new_user.p4_dreamteam_count = user['players'][3]['dreamteam_count']
        new_user.p4_element_type = user['players'][3]['element_type']
        new_user.p4_ep_next = user['players'][3]['ep_next']
        new_user.p4_ep_this = user['players'][3]['ep_this']
        new_user.p4_event_points = user['players'][3]['event_points']
        new_user.p4_first_name = user['players'][3]['first_name']
        new_user.p4_form = user['players'][3]['form']
        new_user.p4_player_id = user['players'][3]['id']
        new_user.p4_in_dreamteam = user['players'][3]['in_dreamteam']
        new_user.p4_news = user['players'][3]['news']
        new_user.p4_news_added = user['players'][3]['news_added']
        new_user.p4_now_cost = user['players'][3]['now_cost']
        new_user.p4_photo = user['players'][3]['photo']
        new_user.p4_points_per_game = user['players'][3]['points_per_game']
        new_user.p4_second_name = user['players'][3]['second_name']
        new_user.p4_selected_by_percent = user['players'][3]['selected_by_percent']
        new_user.p4_special = user['players'][3]['special']
        new_user.p4_squad_number = user['players'][3]['squad_number']
        new_user.p4_status = user['players'][3]['status']
        new_user.p4_team = user['players'][3]['team']
        new_user.p4_team_code = user['players'][3]['team_code']
        new_user.p4_total_points = user['players'][3]['total_points']
        new_user.p4_transfers_in = user['players'][3]['transfers_in']
        new_user.p4_transfers_in_event = user['players'][3]['transfers_in_event']
        new_user.p4_transfers_out = user['players'][3]['transfers_out']
        new_user.p4_transfers_out_event = user['players'][3]['transfers_out_event']
        new_user.p4_value_form = user['players'][3]['value_form']
        new_user.p4_value_season = user['players'][3]['value_season']
        new_user.p4_web_name = user['players'][3]['web_name']
        new_user.p4_minutes = user['players'][3]['minutes']
        new_user.p4_goals_scored = user['players'][3]['goals_scored']
        new_user.p4_assists = user['players'][3]['assists']
        new_user.p4_clean_sheets = user['players'][3]['clean_sheets']
        new_user.p4_own_goals = user['players'][3]['own_goals']
        new_user.p4_penalties_saved = user['players'][3]['penalties_saved']
        new_user.p4_yellow_cards = user['players'][3]['yellow_cards']
        new_user.p4_red_cards = user['players'][3]['red_cards']
        new_user.p4_saves = user['players'][3]['saves']
        new_user.p4_bonus = user['players'][3]['bonus']
        new_user.p4_bps = user['players'][3]['bps']
        new_user.p4_influence = user['players'][3]['influence']
        new_user.p4_creativity = user['players'][3]['creativity']
        new_user.p4_threat = user['players'][3]['threat']
        new_user.p4_ict_index = user['players'][3]['ict_index']
        new_user.p4_influence_rank = user['players'][3]['influence_rank']
        new_user.p4_influence_rank_type = user['players'][3]['influence_rank_type']
        new_user.p4_creativity_rank = user['players'][3]['creativity_rank']
        new_user.p4_creativity_rank_type = user['players'][3]['creativity_rank_type']
        new_user.p4_threat_rank = user['players'][3]['threat_rank']
        new_user.p4_threat_rank_type = user['players'][3]['threat_rank_type']



        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id

        flash(f'Welcome {email}! Successfully Created Your Account!')
        return redirect(f'/user/{new_user.id}')
    return render_template('/register.html', form=form)

# login
@app.route('/logon', methods=['GET','POST'])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = Users.authenticate(email, password)
        if user:
            session['user_id'] = user.id
            return redirect(f'/user/{user.id}')
        else:
            form.email.errors = ['Invalid username/password.']
    return render_template('login.html', form=form)

@app.route('/user/<int:user_id>')
def user_route(user_id):
    users = Users.query.get_or_404(user_id)
    jerseys = jersey_list
    return render_template('user.html', users=users, jerseys=jerseys)

@app.route('/logout')
def logout():
    session.pop('user_id')
    flash("Goodbye!")
    return redirect('/')
