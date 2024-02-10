"""This module is the API for the games module."""
from games.scrapper import get_matches
from utils import date_handler


def get_all_matches() -> dict[str, str]:
	"""Get all the matches from the scrapper and return a json with all the games"""
	games = []
	game = {}
	matches = get_matches()
	for match in matches:
		game = match_handler(match)
		games.append(game)

	return games


def match_handler(game: list[str]) -> dict[str, str]:
		"""Handle the match and return a dictionary with the match's information."""
		match = {
				'championship': game[0],
				'home': game[1],
				'away': game[2],
				'date': date_handler(game[3]),
				'hour': game[4].replace(' ', '')
		}
		return match

def check_championship(game: list[str], championship: str):
	""" whenever a new championship is added, this function will be used to check if the championship is already in the list
	if not, it will be added to the list
	if it is, the game will be added to the list of games of that championship
	"""