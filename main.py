import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from sqlalchemy.sql.expression import func

from form import GameForm
from models import Game, db

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key" # os.environ.get("FLASK_KEY") # Should be a random string, as env variable
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", 'sqlite:///games.db')
db.init_app(app)

with app.app_context():
    db.create_all()
    # We will add the games to the table if the table is empty
    if len(db.session.execute(db.select(Game)).scalars().all()) == 0:
        with open("database/data/games.csv", "r") as f:
            games = f.readlines()
        headers = games[0].split(",")
        games_to_add = []
        for game in games[1:]:
            g = game.strip().split(",")
            games_to_add.append(
                # I am sure there is a better way of doing this
                Game(
                    name=g[0],
                    min_players=g[2],
                    max_players=g[3],
                    avg_playing_time=g[4],
                    adult_only=False if g[5] == "No" else True,
                    categories=g[6],
                    difficulty=g[7],
                    tutorial=g[8],
                    image_url=g[9]
                )
            )
        db.session.bulk_save_objects(games_to_add)
        db.session.commit()

@app.route("/", methods=["GET", "POST"])
def welcome():
    form = GameForm()
    if form.validate_on_submit():
        games = db.session.execute(
            db.select(Game).where(
                (Game.min_players <= int(form.n_players.data)) &
                (Game.max_players >= int(form.n_players.data)) &
                (Game.avg_playing_time <= int(form.playing_time.data)) &
                (Game.categories.like(f"%{form.choice.data[0]}%"))
            ).order_by(func.random()).limit(3)
        )
        results = games.scalars().all()
        filtered_results = []
        if len(form.choice.data) == 2:
            for game in results:
                if form.choice.data[1] in game.categories:
                    filtered_results.append(game)
        return render_template("game.html", games=filtered_results if len(filtered_results) > 0 else results)
    return render_template("index.html", form=form)

@app.route("/all-games")
def all_games():
    result = db.session.execute(db.select(Game))
    games = result.scalars().all()
    return render_template("game.html", games=games)

# Add a POST method to redirect to a game info page
@app.route("/game/<int:game_id>", methods=["GET", "POST"])
def show_game(game_id):
    requested_game = db.get_or_404(Game, game_id)
    return render_template(
        "game.html", 
        game=requested_game
    )

@app.route("/random")
def random_game():
    random_game = db.session.execute(
        db.select(Game).order_by(func.random()).limit(1)
    ).scalars().all()[0]
    """
    Game template:
    
    +---------+
    |         |
    |  Game   |
    |  image  |
    |         |
    +---------+
    
    Info
    """
    return render_template("game.html", games=[random_game])