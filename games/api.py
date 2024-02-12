"""This module is the API for the games' module."""
from games.model.latest_match import LatestMatch
from games.model.match import Match
from games.scrapper import get_matches, get_latest_matches
from utils import date_handler


def get_all_matches() -> list[Match]:
    """Get all the matches from the scrapper and return a json with all the games"""
    games = []
    matches = get_matches()
    for match in matches:
        game: Match = match_handler(match)
        games.append(game)

    return games


def get_recent_matches() -> list[LatestMatch]:
    """Get all the matches from the scrapper and return a json with the latest games"""
    games = []
    matches = get_latest_matches()
    print(matches)
    for match in matches:
        game: LatestMatch = latest_matches_handler(match)
        print(game)
        games.append(game)

    return games


def match_handler(game: list[str]) -> Match:
    """Handle the match and return a dictionary with the match's information."""
    match = Match(game[0], game[1], game[2], date_handler(game[3]), game[4].replace(' ', ''))
    return match


def latest_matches_handler(game: list[str]) -> LatestMatch:
    """Handle the latest and return a dictionary with the match's information."""
    match = LatestMatch(game[0], game[1], game[2], game[3], date_handler(game[4]))
    return match


def check_championship(game: list[str], championship: str):
    """ whenever a new championship is added, this function will be used to check if the championship is already in the list
	    if not, it will be added to the list ; if it is, the game will be added to the list of games of that championship"""

