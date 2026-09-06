from django.shortcuts import render


def home(request):
    return render(request, "Care360.html")


def games(request):
    return render(request, "games.html")


def rps(request):
    return render(request, "rps.html")


def sudoku(request):
    return render(request, "sudoku.html")


def guessthenum(request):
    return render(request, "guessthenum.html")


def tictactoe(request):
    return render(request, "tictactoe.html")


def contact(request):
    return render(request, "contact.html")