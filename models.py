from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    team_id = db.Column(db.Integer, nullable=False, unique=True)
    # user fantasy profile data
    team_name = db.Column(db.Text, nullable=True)
    overall_points = db.Column(db.Integer, nullable=True)
    overall_rank = db.Column(db.Integer, nullable=True)
    gameweek_points = db.Column(db.Integer, nullable=True)
    gameweek_rank = db.Column(db.Integer, nullable=True)
    classic_league_rank = db.Column(db.Integer, nullable=True)
    classic_league_rank_previous = db.Column(db.Integer, nullable=True)

    p1_chance_of_playing_next_round = db.Column(db.Text, nullable=True)
    p1_chance_of_playing_this_round = db.Column(db.Text, nullable=True)
    p1_code = db.Column(db.Integer, nullable=True)
    p1_cost_change_event = db.Column(db.Integer, nullable=True)
    p1_cost_change_event_fall = db.Column(db.Integer, nullable=True)
    p1_cost_change_start = db.Column(db.Integer, nullable=True)
    p1_cost_change_start_fall = db.Column(db.Integer, nullable=True)
    p1_dreamteam_count = db.Column(db.Integer, nullable=True)
    p1_element_type = db.Column(db.Integer, nullable=True)
    p1_ep_next = db.Column(db.Float, nullable=True)
    p1_ep_this = db.Column(db.Float, nullable=True)
    p1_event_points = db.Column(db.Integer, nullable=True)
    p1_first_name = db.Column(db.Text, nullable=True)
    p1_form = db.Column(db.Float, nullable=True)
    p1_player_id = db.Column(db.Integer, nullable=True)
    p1_in_dreamteam = db.Column(db.Text, nullable=True)
    p1_news = db.Column(db.Text, nullable=True)
    p1_news_added = db.Column(db.Text, nullable=True)
    p1_now_cost = db.Column(db.Integer, nullable=True)
    p1_photo = db.Column(db.Text, nullable=True)
    p1_points_per_game = db.Column(db.Float, nullable=True)
    p1_second_name = db.Column(db.Text, nullable=True)
    p1_selected_by_percent = db.Column(db.Float, nullable=True)
    p1_special = db.Column(db.Text, nullable=True)
    p1_squad_number = db.Column(db.Integer, nullable=True)
    p1_status = db.Column(db.Text, nullable=True)
    p1_team = db.Column(db.Integer, nullable=True)
    p1_team_code = db.Column(db.Integer, nullable=True)
    p1_total_points = db.Column(db.Integer, nullable=True)
    p1_transfers_in = db.Column(db.Integer, nullable=True)
    p1_transfers_in_event = db.Column(db.Integer, nullable=True)
    p1_transfers_out = db.Column(db.Integer, nullable=True)
    p1_transfers_out_event = db.Column(db.Integer, nullable=True)
    p1_value_form = db.Column(db.Float, nullable=True)
    p1_value_season = db.Column(db.Float, nullable=True)
    p1_web_name = db.Column(db.Text, nullable=True)
    p1_minutes = db.Column(db.Integer, nullable=True)
    p1_goals_scored = db.Column(db.Integer, nullable=True)
    p1_assists = db.Column(db.Integer, nullable=True)
    p1_clean_sheets = db.Column(db.Integer, nullable=True)
    p1_goals_conceded = db.Column(db.Integer, nullable=True)
    p1_own_goals = db.Column(db.Integer, nullable=True)
    p1_penalties_saved = db.Column(db.Integer, nullable=True)
    p1_penalties_missed = db.Column(db.Integer, nullable=True)
    p1_yellow_cards = db.Column(db.Integer, nullable=True)
    p1_red_cards = db.Column(db.Integer, nullable=True)
    p1_saves = db.Column(db.Integer, nullable=True)
    p1_bonus = db.Column(db.Integer, nullable=True)
    p1_bps = db.Column(db.Integer, nullable=True)
    p1_influence = db.Column(db.Float, nullable=True)
    p1_creativity = db.Column(db.Float, nullable=True)
    p1_threat = db.Column(db.Float, nullable=True)
    p1_ict_index = db.Column(db.Float, nullable=True)
    p1_influence_rank = db.Column(db.Integer, nullable=True)
    p1_influence_rank_type = db.Column(db.Integer, nullable=True)
    p1_creativity_rank = db.Column(db.Integer, nullable=True)
    p1_creativity_rank_type = db.Column(db.Integer, nullable=True)
    p1_threat_rank = db.Column(db.Integer, nullable=True)
    p1_threat_rank_type = db.Column(db.Integer, nullable=True)
    p1_ict_index_rank = db.Column(db.Integer, nullable=True)
    p1_ict_index_rank_type = db.Column(db.Integer, nullable=True)


    @classmethod
    def register(cls, email, pwd, team_id):
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")
        return cls(email=email, password=hashed_utf8, team_id=team_id)

    @classmethod
    def authenticate(cls, email, pwd):
        u = Users.query.filter_by(email=email).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False

class Chat(db.Model):
    __tablename__ = "chat"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('Users', backref='chat')
