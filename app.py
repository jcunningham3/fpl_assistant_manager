from flask import Flask, flash, request, redirect, render_template, session, g
from models import connect_db, db, Users, Chat
from forms import UserForm, ChatForm, LoginForm
from methods import user, make_user_profile, all_footballers, user_personal_info, starting_vi

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
    return render_template('user.html', users=users)

@app.route('/logout')
def logout():
    session.pop('user_id')
    flash("Goodbye!")
    return redirect('/')
