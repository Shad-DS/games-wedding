from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired


class GameForm(FlaskForm):
    n_players = SelectField(
        label="How many players?", 
        choices=[(f"{i}", f"{i}") for i in range(1, 6)] + [("6", "6+")], 
        validators=[DataRequired()]
    )
    choice = SelectMultipleField(
        label="What kind of games do you like?",
        choices=[('Abstract Strategy', 'Abstract Strategy'),
                ('Party Game', 'Party Game'),
                ('Dice', 'Dice'),
                ('Maze', 'Maze'),
                ('Travel', 'Travel'),
                ('Cooperative', 'Cooperative'),
                ('Prehistoric', 'Prehistoric'),
                ('Deduction', 'Deduction'),
                ('Ecomonic', 'Ecomonic'),
                ('Renaissance', 'Renaissance'),
                ('Educational', 'Educational'),
                ('Horror', 'Horror'),
                ('Card Game', 'Card Game'),
                ('Pirates', 'Pirates'),
                ('Exploration', 'Exploration'),
                ('Number', 'Number'),
                ('Animals', 'Animals'),
                ('Negotiation', 'Negotiation'),
                ('Memory', 'Memory'),
                ('Bluffing', 'Bluffing'),
                ('Real-time', 'Real-time'),
                ('Video Game', 'Video Game'),
                ('Word Game', 'Word Game'),
                ('Trivia', 'Trivia'),
                ('Action / Dexterity', 'Action / Dexterity'),
                ('Humor', 'Humor'),
                ('Murder/Mystery', 'Murder/Mystery'),
                ('Card Games', 'Card Games'),
                ('Nautical', 'Nautical'),
                ('Mafia', 'Mafia'),
                ('Fantasy', 'Fantasy'),
                ('Political', 'Political'),
                ('Puzzle', 'Puzzle')],
        validators=[DataRequired()],
    )
    adults = SelectField(
        label="Are children (< 8 yrs old) playing?", 
        choices=[("False", "Yes"), ("True", "No")],
        validators=[DataRequired()]
    )
    playing_time = SelectField(
        label="How long would you like to play for?",
        choices=[("15", "15min"), ("30", "30min"), ("45", "45min"), ("60", "1hr")],
        validators=[DataRequired()]
    )
    submit = SubmitField("Find me a game!")

    def validate(self, extra_validators=None):                                                      

        rv = FlaskForm.validate(self)                                           

        if not rv:                                                              
            return False                                                                                                    

        if len(self.choice.data) > 1:                                          
            self.choice.errors.append('Please select no more than 1 category.')    
            return False                                                        

        return True 