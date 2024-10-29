from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Boolean

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# CONFIGURE TABLES
class Game(db.Model):
    __tablename__ = "games"
    game_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    min_players: Mapped[int] = mapped_column(Integer, nullable=False)
    max_players: Mapped[int] = mapped_column(Integer, nullable=False)
    avg_playing_time: Mapped[int] = mapped_column(Integer, nullable=False)
    adult_only: Mapped[bool] = mapped_column(Boolean, nullable=False)
    categories: Mapped[str] = mapped_column(Text, nullable=True)
    difficulty: Mapped[int] = mapped_column(Integer, nullable=True)
    tutorial: Mapped[str] = mapped_column(Text, nullable=True)
    image_url: Mapped[str] = mapped_column(Text, nullable=True)