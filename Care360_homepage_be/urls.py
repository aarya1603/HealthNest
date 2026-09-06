from django.urls import path
from .views import (
    home,
    games,
    rps,
    sudoku,
    guessthenum,
    tictactoe,
)


urlpatterns = [

    # Home
    path(
        "",
        home,
        name="home"
    ),

    # Games
    path(
        "games/",
        games,
        name="games"
    ),

    path(
        "games/rps/",
        rps,
        name="rps"
    ),

    path(
        "games/sudoku/",
        sudoku,
        name="sudoku"
    ),

    path(
        "games/guess/",
        guessthenum,
        name="guessthenum"
    ),

    path(
        "games/tictactoe/",
        tictactoe,
        name="tictactoe"
    ),

]